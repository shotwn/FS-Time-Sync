from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Qt
from qtgenerated.settingswindow import Ui_Dialog

from gui.guicommon import GUICommon

import webbrowser


class SettingsWindow(QDialog, GUICommon):
    def __init__(self, gui_root):
        QDialog.__init__(self)
        GUICommon.__init__(self)
        self.gui_root = gui_root
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Settings")
        self.setWindowIcon(self.gui_root.icons["logo"])
        self.ui.github.setIcon(self.gui_root.icons["github"])

        self.settings = self.gui_root.root.settings
        self.changes = {}

        self.ui.button_box.accepted.connect(self.save)
        self.ui.github.clicked.connect(self.github)

        self.ui.auto_sync.stateChanged.connect(self.set_auto_sync)
        if self.settings.get('startup', 'auto_sync'):
            self.ui.auto_sync.setCheckState(Qt.Checked)

        self.ui.start_minimized.stateChanged.connect(self.set_start_minimized)
        if self.settings.get('startup', 'tray'):
            self.ui.start_minimized.setCheckState(Qt.Checked)

        self.ui.minimize_to_tray.stateChanged.connect(self.set_minimize_to_tray)
        if self.settings.get('minimize_to_tray'):
            self.ui.minimize_to_tray.setCheckState(Qt.Checked)

    def set_change(self, value, *keys):
        inner = self.changes
        keys = list(keys)

        last_key = keys.pop()
        for key in keys:
            try:
                inner = inner[key]
            except KeyError:
                inner[key] = {}
                inner = inner[key]

        inner[last_key] = value

    def set_auto_sync(self, value):
        self.set_change(bool(value), "startup", "auto_sync")

    def set_start_minimized(self, value):
        self.set_change(bool(value), "startup", "tray")

    def set_minimize_to_tray(self, value):
        self.set_change(bool(value), "minimize_to_tray")

    def save(self):
        self.settings.set(self.changes)

    def github(self):
        webbrowser.open_new_tab('https://github.com/shotwn/FS-Time-Sync')
