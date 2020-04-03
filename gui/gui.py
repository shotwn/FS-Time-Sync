import os
import sys

from PySide2.QtWidgets import QApplication
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
        }

        self.main_window = MainWindow(self)
        self.offset_window = None
        self.messages = [[], []]
        self.section_labels = [
            self.main_window.ui.right_status,
            self.main_window.ui.right_status_2
        ]

    def main_window_act(self, func, *args, **kwargs):
        self.main_window.act.emit([func, args, kwargs])

    def start(self):
        self.main_window.show()
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

    def show_offset_window(self):
        return True
