from PySide2.QtCore import QFile, QObject
from PySide2.QtCore import Slot, Signal


class GUICommon():
    act = Signal(dict)

    def __init__(self):
        self.act.connect(self._act)
        print("init success")

    @Slot()
    def _act(self, params):
        length = len(params)
        if length == 0:
            raise ValueError

        action = params[0]
        args = []
        kwargs = {}

        if length > 1:
            if isinstance(params[1], tuple) or isinstance(params[1], list):
                args = params[1]
            else:
                args = [params[1]]

        if length > 2:
            kwargs = params[2]

        if length > 3:
            raise ValueError

        action(*args, **kwargs)
