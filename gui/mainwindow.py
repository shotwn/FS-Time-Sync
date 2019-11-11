from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, QSize, Qt

import gui.common
from qtgenerated.scenerycontainer import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, gui_root):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.gui_root = gui_root
        # Icons
        self.setWindowIcon(self.gui_root.icons["logo"])
        self.setWindowTitle("FS Time Sync")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.ui.sync_button.setIcon(self.gui_root.icons["timelapse"])
        self.ui.sync_button.setIconSize(QSize(60, 60))
        self.ui.live_button.setIcon(self.gui_root.icons["sync_disabled"])
        self.ui.live_button.setIconSize(QSize(60, 60))
        # Signals
        self.ui.source_button.clicked.connect(self.switch_now_source)
        self.ui.sync_button.clicked.connect(self.sync_forced)
        self.ui.live_button.clicked.connect(self.toggle_live_sync)

    @Slot()
    def switch_now_source(self):
        self.gui_root.root.switch_now_source()

    @Slot()
    def sync_forced(self):
        self.gui_root.root.sync_sim(force=True)

    @Slot()
    def toggle_live_sync(self):
        self.gui_root.root.toggle_live_sync()
