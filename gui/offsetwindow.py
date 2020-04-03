from datetime import datetime
from copy import deepcopy

from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Slot, Signal

from qtgenerated.offsetwindow import Ui_Dialog
from gui.guicommon import GUICommon
from shotwn import BasicTimeDelta

class OffsetWindow(QDialog, GUICommon):
    def __init__(self, gui_root):
        QDialog.__init__(self)
        GUICommon.__init__(self)
        self.gui_root = gui_root
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Set Offset")
        self.setWindowIcon(self.gui_root.icons["logo"])

        self.temp_offset = deepcopy(self.gui_root.root.offset)

        self.delta_selectors_no_update = False
        self.update_delta_selectors()

        self.datetime_no_update = False
        self.delta_to_datetime()

        # Signal
        self.ui.button_box.accepted.connect(self.apply_offset)
        self.ui.button_box.clicked.connect(self.button_box_clicked)

        self.ui.offset_minutes.valueChanged.connect(self.delta_value_changed)
        self.ui.offset_hours.valueChanged.connect(self.delta_value_changed)
        self.ui.offset_days.valueChanged.connect(self.delta_value_changed)
        self.ui.offset_months.valueChanged.connect(self.delta_value_changed)
        self.ui.offset_years.valueChanged.connect(self.delta_value_changed)
        self.ui.utc_datetimeedit.dateTimeChanged.connect(self.datetime_to_delta)

    def signals_connect(self):
        self.ui.offset_minutes.valueChanged.connect(self.delta_value_changed)
        self.ui.offset_hours.valueChanged.connect(self.delta_value_changed)
        self.ui.offset_days.valueChanged.connect(self.delta_value_changed)
        self.ui.offset_months.valueChanged.connect(self.delta_value_changed)
        self.ui.offset_years.valueChanged.connect(self.delta_value_changed)
        self.ui.utc_datetimeedit.dateTimeChanged.connect(self.datetime_to_delta)

    def signals_disconnect(self):
        self.ui.offset_minutes.valueChanged.disconnect(self.delta_value_changed)
        self.ui.offset_hours.valueChanged.disconnect(self.delta_value_changed)
        self.ui.offset_days.valueChanged.disconnect(self.delta_value_changed)
        self.ui.offset_months.valueChanged.disconnect(self.delta_value_changed)
        self.ui.offset_years.valueChanged.disconnect(self.delta_value_changed)
        self.ui.utc_datetimeedit.dateTimeChanged.disconnect(self.datetime_to_delta)

    def delta_to_datetime(self):
        now = datetime.utcnow()
        self.ui.utc_datetimeedit.setDateTime(self.temp_offset + now)

    def datetime_to_delta(self):  # SLOT
        now = datetime.utcnow()
        selected = self.ui.utc_datetimeedit.dateTime().toPython()
        self.temp_offset.ingest(selected, now)
        self.signals_disconnect()
        self.update_delta_selectors()
        self.signals_connect()

    def update_delta_selectors(self):
        self.ui.offset_minutes.setValue(self.temp_offset.minute)
        self.ui.offset_hours.setValue(self.temp_offset.hour)
        self.ui.offset_days.setValue(self.temp_offset.day)
        self.ui.offset_months.setValue(self.temp_offset.month)
        self.ui.offset_years.setValue(self.temp_offset.year)

    def delta_value_changed(self):  # SLOT
        self.temp_offset.minute = self.ui.offset_minutes.value()
        self.temp_offset.hour = self.ui.offset_hours.value()
        self.temp_offset.day = self.ui.offset_days.value()
        self.temp_offset.month = self.ui.offset_months.value()
        self.temp_offset.year = self.ui.offset_years.value()
        self.signals_disconnect()
        self.delta_to_datetime()
        self.signals_connect()

    def apply_offset(self):
        self.gui_root.root.offset = self.temp_offset
        if bool(self.temp_offset):
            self.gui_root.main_window.ui.offset_button.setStyleSheet('QPushButton {color: green}')
            self.gui_root.main_window.ui.offset_button.setText('Offset Active')
        else:
            self.gui_root.main_window.ui.offset_button.setStyleSheet('')
            self.gui_root.main_window.ui.offset_button.setText('Set Offset')

    def button_box_clicked(self, button):
        if self.ui.button_box.buttonRole(button) == self.ui.button_box.ButtonRole.ResetRole:
            print("self.ui.button_box.buttonRole(button)")
            self.temp_offset = BasicTimeDelta()
            self.signals_disconnect()
            self.update_delta_selectors()
            self.delta_to_datetime()
            self.signals_connect()
