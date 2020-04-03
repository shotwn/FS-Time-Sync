from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, QSize, Qt

from qtgenerated.mainwindow import Ui_MainWindow

from gui.guicommon import GUICommon
from gui.offsetwindow import OffsetWindow


class MainWindow(QMainWindow, GUICommon):
    def __init__(self, gui_root):
        QMainWindow.__init__(self)
        GUICommon.__init__(self)
        self.gui_root = gui_root
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        self.ui.offset_button.clicked.connect(self.show_offset_window)

    @Slot()
    def switch_now_source(self):
        self.gui_root.root.switch_now_source()

    @Slot()
    def sync_forced(self):
        self.gui_root.root.sync_sim(force=True)

    @Slot()
    def toggle_live_sync(self):
        self.gui_root.root.toggle_live_sync()

    @Slot()
    def show_offset_window(self):
        self.gui_root.offset_window = OffsetWindow(self.gui_root)
        self.gui_root.offset_window.show()
