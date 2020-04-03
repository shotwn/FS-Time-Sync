# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Works\Dev\FSUTCSync\ui\offsetwindow.ui',
# licensing of 'D:\Works\Dev\FSUTCSync\ui\offsetwindow.ui' applies.
#
# Created: Fri Apr  3 13:28:04 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(259, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(259, 180))
        Dialog.setStyleSheet("QDialog {\n"
"    background-color: #151515;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QToolButton {\n"
"    color: #ffffff;\n"
"    background-color: #151515;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #ffffff;\n"
"    top: -10px;\n"
"    left: 5px;\n"
"    padding:2px;\n"
"}")
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setGeometry(QtCore.QRect(10, 145, 241, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.button_box.setCenterButtons(False)
        self.button_box.setObjectName("button_box")
        self.utc = QtWidgets.QGroupBox(Dialog)
        self.utc.setGeometry(QtCore.QRect(10, 80, 241, 61))
        self.utc.setObjectName("utc")
        self.utc_datetimeedit = QtWidgets.QDateTimeEdit(self.utc)
        self.utc_datetimeedit.setGeometry(QtCore.QRect(10, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.utc_datetimeedit.setFont(font)
        self.utc_datetimeedit.setCursor(QtCore.Qt.SizeVerCursor)
        self.utc_datetimeedit.setCalendarPopup(False)
        self.utc_datetimeedit.setTimeSpec(QtCore.Qt.UTC)
        self.utc_datetimeedit.setObjectName("utc_datetimeedit")
        self.offset = QtWidgets.QGroupBox(Dialog)
        self.offset.setGeometry(QtCore.QRect(10, 10, 241, 61))
        self.offset.setObjectName("offset")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.offset)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 10, 241, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, -1, 5, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(40, 0))
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.offset_hours = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.offset_hours.setMaximumSize(QtCore.QSize(35, 16777215))
        self.offset_hours.setCursor(QtCore.Qt.SizeVerCursor)
        self.offset_hours.setWrapping(False)
        self.offset_hours.setFrame(False)
        self.offset_hours.setAlignment(QtCore.Qt.AlignCenter)
        self.offset_hours.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.offset_hours.setAccelerated(False)
        self.offset_hours.setMinimum(-24)
        self.offset_hours.setMaximum(24)
        self.offset_hours.setObjectName("offset_hours")
        self.verticalLayout.addWidget(self.offset_hours)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(60, 0))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.offset_minutes = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.offset_minutes.setMaximumSize(QtCore.QSize(35, 16777215))
        self.offset_minutes.setCursor(QtCore.Qt.SizeVerCursor)
        self.offset_minutes.setWrapping(False)
        self.offset_minutes.setFrame(False)
        self.offset_minutes.setAlignment(QtCore.Qt.AlignCenter)
        self.offset_minutes.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.offset_minutes.setAccelerated(False)
        self.offset_minutes.setMinimum(-60)
        self.offset_minutes.setMaximum(60)
        self.offset_minutes.setObjectName("offset_minutes")
        self.verticalLayout_2.addWidget(self.offset_minutes)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(40, 0))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.offset_days = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.offset_days.setMaximumSize(QtCore.QSize(35, 16777215))
        self.offset_days.setCursor(QtCore.Qt.SizeVerCursor)
        self.offset_days.setWrapping(False)
        self.offset_days.setFrame(False)
        self.offset_days.setAlignment(QtCore.Qt.AlignCenter)
        self.offset_days.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.offset_days.setAccelerated(False)
        self.offset_days.setMinimum(-31)
        self.offset_days.setMaximum(31)
        self.offset_days.setObjectName("offset_days")
        self.verticalLayout_3.addWidget(self.offset_days)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(40, 0))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.offset_months = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.offset_months.setMaximumSize(QtCore.QSize(35, 16777215))
        self.offset_months.setCursor(QtCore.Qt.SizeVerCursor)
        self.offset_months.setWrapping(False)
        self.offset_months.setFrame(False)
        self.offset_months.setAlignment(QtCore.Qt.AlignCenter)
        self.offset_months.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.offset_months.setAccelerated(False)
        self.offset_months.setMinimum(-12)
        self.offset_months.setMaximum(12)
        self.offset_months.setObjectName("offset_months")
        self.verticalLayout_4.addWidget(self.offset_months)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.offset_years = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.offset_years.setMaximumSize(QtCore.QSize(35, 16777215))
        self.offset_years.setCursor(QtCore.Qt.SizeVerCursor)
        self.offset_years.setWrapping(False)
        self.offset_years.setFrame(False)
        self.offset_years.setAlignment(QtCore.Qt.AlignCenter)
        self.offset_years.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.offset_years.setAccelerated(False)
        self.offset_years.setMinimum(-99)
        self.offset_years.setObjectName("offset_years")
        self.verticalLayout_5.addWidget(self.offset_years)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout.setStretch(1, 1)
        self.sun_position = QtWidgets.QGroupBox(Dialog)
        self.sun_position.setGeometry(QtCore.QRect(260, 10, 91, 131))
        self.sun_position.setObjectName("sun_position")
        self.sun_dial = QtWidgets.QDial(self.sun_position)
        self.sun_dial.setGeometry(QtCore.QRect(0, 21, 91, 91))
        self.sun_dial.setObjectName("sun_dial")
        self.sun_angle = QtWidgets.QLabel(self.sun_position)
        self.sun_angle.setGeometry(QtCore.QRect(10, 106, 71, 20))
        self.sun_angle.setAlignment(QtCore.Qt.AlignCenter)
        self.sun_angle.setObjectName("sun_angle")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.utc.setTitle(QtWidgets.QApplication.translate("Dialog", "UTC", None, -1))
        self.utc_datetimeedit.setDisplayFormat(QtWidgets.QApplication.translate("Dialog", "HH:mm dd.MM.yyyy", None, -1))
        self.offset.setTitle(QtWidgets.QApplication.translate("Dialog", "Offset", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Dialog", "Hours", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Dialog", "Minutes", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "Days", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "Months", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Dialog", "Years", None, -1))
        self.sun_position.setTitle(QtWidgets.QApplication.translate("Dialog", "Sun Position", None, -1))
        self.sun_angle.setText(QtWidgets.QApplication.translate("Dialog", "50\'", None, -1))

