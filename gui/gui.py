import os
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide2.QtGui import QIcon

from gui.mainwindow import MainWindow


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/7675014#7675014
    """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)


class GUI:
    def __init__(self, root):
        self.root = root
        self.app = QApplication([])
        self.icons = {
            "timelapse": QIcon(resource_path('icons/timelapse.png')),
            "sync": QIcon(resource_path('icons/sync.png')),
            "sync_disabled": QIcon(resource_path('icons/sync_disabled.png')),
            "logo": QIcon(resource_path('icons/logo.png')),
            "settings": QIcon(resource_path('icons/settings.png')),
            "github": QIcon(resource_path('icons/github.png'))
        }

        self.main_window = MainWindow(self)
        self.offset_window = None
        self.settings_window = None
        self.messages = [[], []]
        self.section_labels = [
            self.main_window.ui.right_status,
            self.main_window.ui.right_status_2
        ]

        menu = QMenu('FS Time Sync')
        menu.setStyleSheet("""
        QMenu {
            background-color: #151515;
            color: #ffffff;
        }
        QMenu::item {
            padding: 5px 10px 5px 10px;
        }
        QMenu::item:selected {
            background-color: #ffffff;
            color: #151515;
        }
        """)
        self.tray_actions = {}
        self.tray_actions["hide_show"] = menu.addAction("Hide")
        self.tray_actions["hide_show"].triggered.connect(self.hide)
        self.tray_actions["exit"] = menu.addAction("Exit")
        self.tray_actions["exit"].triggered.connect(self.exit)

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icons['logo'])
        self.tray.setToolTip("FS Time Sync")
        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.trayActivated)
        self.tray.show()

    def main_window_act(self, func, *args, **kwargs):
        self.main_window.act.emit([func, args, kwargs])

    def hide(self):
        self.tray_actions["hide_show"].setText("Show")
        self.tray_actions["hide_show"].triggered.connect(self.show)
        if self.offset_window:
            self.offset_window.close()
        self.main_window.saveState()
        self.main_window.hide()

    def trayActivated(self, reason):
        if reason == self.tray.ActivationReason.Trigger:
            self.show()

    def single_instance_triggered(self):
        self.tray.showMessage("FS Time Sync", "FS Time Sync is already running.")
        self.show()

    def show(self):
        self.tray_actions["hide_show"].setText("Hide")
        self.tray_actions["hide_show"].triggered.connect(self.hide)
        self.main_window.show()
        # Brings window forward, but doesn't force it to stay active.
        self.main_window.setWindowState(Qt.WindowActive)
        self.main_window.setWindowState(Qt.WindowNoState)

    def exit(self):
        self.app.quit()

    def start(self):
        # Add single instance trigger.
        self.root.si.add_trigger(self.single_instance_triggered)

        # Settings are triggered here.
        if not self.root.settings.get("startup", "tray"):  # Start regularly or as tray icon
            self.main_window.show()
        else:
            self.tray.showMessage("FS Time Sync", "FS Time Sync Started in Tray.")
            self.tray_actions["hide_show"].setText("Show")
            self.tray_actions["hide_show"].triggered.connect(self.show)

        if self.root.settings.get("startup", "auto_sync"):
            self.root.enable_live_sync()

        self.app.exec_()

    def add_message(self, section, code, msg):
        for message in self.messages[section]:
            if message["code"] == code:
                message["msg"] = msg
                break
        else:
            self.messages[section].append({
                "code": code,
                "msg": msg
            })

        self.main_window.act.emit([self.section_labels[section].setText, msg])

    def remove_message(self, section, code):
        for message in self.messages[section]:
            if message["code"] == code:
                self.messages[section].remove(message)
                break
        else:
            return  # No action just return

        if len(self.messages[section]) > 0:
            print(self.messages[section])
            self.main_window.act.emit([self.section_labels[section].setText, self.messages[section][-1]["msg"]])
        else:
            self.main_window.act.emit([self.section_labels[section].setText, ""])
