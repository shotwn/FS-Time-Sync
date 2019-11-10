from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon

from gui.mainwindow import MainWindow


class GUI:
    def __init__(self, root):
        self.root = root
        self.app = QApplication([])
        self.icons = {
            "timelapse": QIcon('icons/timelapse.png'),
            "sync": QIcon('icons/sync.png'),
            "sync_disabled": QIcon('icons/sync_disabled.png'),
        }

        self.main_window = MainWindow(self)
        self.messages = [[], []]
        self.section_labels = [
            self.main_window.ui.right_status,
            self.main_window.ui.right_status_2
        ]

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

        self.section_labels[section].setText(msg)

    def remove_message(self, section, code):
        for message in self.messages[section]:
            if message["code"] == code:
                self.messages[section].remove(message)
                break
        else:
            return  # No action just return

        if len(self.messages[section]) > 0:
            print(self.messages[section])
            self.section_labels[section].setText(self.messages[section][-1]["msg"])
        else:
            self.section_labels[section].setText("")
