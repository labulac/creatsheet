# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\python\pyqt\first\creatsheet.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_4)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_5)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.yiyan_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.yiyan_label.setFont(font)
        self.yiyan_label.setText("")
        self.yiyan_label.setAlignment(QtCore.Qt.AlignCenter)
        self.yiyan_label.setObjectName("yiyan_label")
        self.gridLayout.addWidget(self.yiyan_label, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu11 = QtWidgets.QMenu(self.menubar)
        self.menu11.setObjectName("menu11")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu11.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "新建账单小助手v2.0         完成于2021年6月18日"))
        self.label.setText(_translate("MainWindow", "新的账单名："))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "输入想要创建的账单名称"))
        self.label_2.setText(_translate("MainWindow", ".xlsx"))
        self.pushButton.setText(_translate("MainWindow", "生成账单"))
        self.label_3.setText(_translate("MainWindow", "工期段："))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "2021"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2022"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2023"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "2024"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "2025"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "2026"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "2027"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "2028"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "2029"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "2030"))
        self.label_11.setText(_translate("MainWindow", "年"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "01"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "02"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "03"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "04"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "05"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "06"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "07"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "08"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "09"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "12"))
        self.label_12.setText(_translate("MainWindow", "月"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "01"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "02"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "03"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "04"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "05"))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "06"))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "07"))
        self.comboBox_1.setItemText(7, _translate("MainWindow", "08"))
        self.comboBox_1.setItemText(8, _translate("MainWindow", "09"))
        self.comboBox_1.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_1.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_1.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox_1.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox_1.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox_1.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox_1.setItemText(15, _translate("MainWindow", "16"))
        self.comboBox_1.setItemText(16, _translate("MainWindow", "17"))
        self.comboBox_1.setItemText(17, _translate("MainWindow", "18"))
        self.comboBox_1.setItemText(18, _translate("MainWindow", "19"))
        self.comboBox_1.setItemText(19, _translate("MainWindow", "20"))
        self.comboBox_1.setItemText(20, _translate("MainWindow", "21"))
        self.comboBox_1.setItemText(21, _translate("MainWindow", "22"))
        self.comboBox_1.setItemText(22, _translate("MainWindow", "23"))
        self.comboBox_1.setItemText(23, _translate("MainWindow", "24"))
        self.comboBox_1.setItemText(24, _translate("MainWindow", "25"))
        self.comboBox_1.setItemText(25, _translate("MainWindow", "26"))
        self.comboBox_1.setItemText(26, _translate("MainWindow", "27"))
        self.comboBox_1.setItemText(27, _translate("MainWindow", "28"))
        self.comboBox_1.setItemText(28, _translate("MainWindow", "29"))
        self.comboBox_1.setItemText(29, _translate("MainWindow", "30"))
        self.comboBox_1.setItemText(30, _translate("MainWindow", "31"))
        self.label_10.setText(_translate("MainWindow", "日-"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "2021"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2022"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "2023"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "2024"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "2025"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "2026"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "2027"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "2028"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "2029"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "2030"))
        self.label_8.setText(_translate("MainWindow", "年"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "01"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "02"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "03"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "04"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "05"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "06"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "07"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "08"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "09"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_5.setItemText(11, _translate("MainWindow", "12"))
        self.label_9.setText(_translate("MainWindow", "月"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "01"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "02"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "03"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "04"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "05"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "06"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "07"))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "08"))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "09"))
        self.comboBox_6.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_6.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_6.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox_6.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox_6.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox_6.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox_6.setItemText(15, _translate("MainWindow", "16"))
        self.comboBox_6.setItemText(16, _translate("MainWindow", "17"))
        self.comboBox_6.setItemText(17, _translate("MainWindow", "18"))
        self.comboBox_6.setItemText(18, _translate("MainWindow", "19"))
        self.comboBox_6.setItemText(19, _translate("MainWindow", "20"))
        self.comboBox_6.setItemText(20, _translate("MainWindow", "21"))
        self.comboBox_6.setItemText(21, _translate("MainWindow", "22"))
        self.comboBox_6.setItemText(22, _translate("MainWindow", "23"))
        self.comboBox_6.setItemText(23, _translate("MainWindow", "24"))
        self.comboBox_6.setItemText(24, _translate("MainWindow", "25"))
        self.comboBox_6.setItemText(25, _translate("MainWindow", "26"))
        self.comboBox_6.setItemText(26, _translate("MainWindow", "27"))
        self.comboBox_6.setItemText(27, _translate("MainWindow", "28"))
        self.comboBox_6.setItemText(28, _translate("MainWindow", "29"))
        self.comboBox_6.setItemText(29, _translate("MainWindow", "30"))
        self.comboBox_6.setItemText(30, _translate("MainWindow", "31"))
        self.label_7.setText(_translate("MainWindow", "日"))
        self.pushButton_2.setText(_translate("MainWindow", "写入工期"))
        self.pushButton_3.setText(_translate("MainWindow", "退出"))
        self.menu11.setTitle(_translate("MainWindow", "检查更新"))
