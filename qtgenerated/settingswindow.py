# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Works\Dev\FSUTCSync\ui\settingswindow.ui',
# licensing of 'D:\Works\Dev\FSUTCSync\ui\settingswindow.ui' applies.
#
# Created: Sat Apr  4 17:58:34 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 126)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(390, 126))
        Dialog.setMaximumSize(QtCore.QSize(390, 126))
        Dialog.setStyleSheet("QDialog {\n"
"    background-color: #151515;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #ffffff;\n"
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
        self.button_box.setGeometry(QtCore.QRect(40, 91, 341, 31))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.button_box.setObjectName("button_box")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 71))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 161, 42))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.auto_sync = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.auto_sync.setObjectName("auto_sync")
        self.verticalLayout.addWidget(self.auto_sync)
        self.start_minimized = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.start_minimized.setObjectName("start_minimized")
        self.verticalLayout.addWidget(self.start_minimized)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 10, 181, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 161, 21))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.minimize_to_tray = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.minimize_to_tray.setObjectName("minimize_to_tray")
        self.verticalLayout_2.addWidget(self.minimize_to_tray)
        self.github = QtWidgets.QToolButton(Dialog)
        self.github.setGeometry(QtCore.QRect(10, 95, 24, 24))
        self.github.setCursor(QtCore.Qt.PointingHandCursor)
        self.github.setStyleSheet("QToolButton {\n"
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
        self.github.setText("")
        self.github.setObjectName("github")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "Startup", None, -1))
        self.auto_sync.setText(QtWidgets.QApplication.translate("Dialog", "Enable auto-sync at startup", None, -1))
        self.start_minimized.setText(QtWidgets.QApplication.translate("Dialog", "Start minimized to tray", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Dialog", "Behaviour", None, -1))
        self.minimize_to_tray.setText(QtWidgets.QApplication.translate("Dialog", "Minimize to tray", None, -1))

