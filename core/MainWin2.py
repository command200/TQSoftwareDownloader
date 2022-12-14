# -*- coding: utf-8 -*-

import os
import re

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QApplication, QAction, QDialog

from core import func

import sys
import requests
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1196, 640)
        MainWindow.setFixedSize(1196, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 40, 131, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 231, 50))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(520, 40, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 40, 54, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 290, 251, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(440, 290, 37, 21))
        self.toolButton.setObjectName("toolButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 280, 91, 41))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 70, 1190, 210))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 360, 1190, 250))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 320, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 320, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 320, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 320, 120, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(740, 325, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        #self.menu.setObjectName("menu")
        # self.menu_2 = QtWidgets.QMenu(self.menubar)
        # self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        # self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????????"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "??????????????????"))
        self.label.setText(_translate("MainWindow", "???????????????"))
        self.comboBox.setCurrentText(_translate("MainWindow", "??????"))
        self.comboBox.setItemText(0, _translate("MainWindow", "??????"))
        self.comboBox.setItemText(1, _translate("MainWindow", "360"))
        self.comboBox.setItemText(2, _translate("MainWindow", "??????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "???????????????"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "????????????"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "??????"))
        # ????????????
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 350)
        self.tableWidget.setColumnWidth(5, 50)
        self.tableWidget.setColumnWidth(6, 60)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "????????????"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "??????"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "??????"))
        # ????????????
        self.tableWidget_2.setColumnWidth(0, 275)
        self.tableWidget_2.setColumnWidth(1, 120)
        self.tableWidget_2.setColumnWidth(2, 80)
        self.tableWidget_2.setColumnWidth(3, 100)
        self.tableWidget_2.setColumnWidth(4, 350)
        self.tableWidget_2.setColumnWidth(5, 50)
        self.tableWidget_2.setColumnWidth(6, 60)
        self.tableWidget_2.setColumnWidth(7, 150)
        self.label_4.setText(_translate("MainWindow", "???????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "????????????"))
        self.pushButton_5.setText(_translate("MainWindow", "??????????????????"))
        self.label_5.setText(_translate("MainWindow", "????????????0?????????"))
        #self.menu.setTitle(_translate("MainWindow", "??????"))
        self.localfile_action = QAction(MainWindow)
        self.localfile_action.setCheckable(False)
        self.localfile_action.setObjectName('aboutAction')
        self.localfile_action.triggered.connect(MainWin.menuButton)
        self.localfile_action.setText('??????')
        self.menubar.addAction(self.localfile_action)
        # self.menu_2.setTitle(_translate("MainWindow", "??????"))


class MainWin(QtWidgets.QMainWindow, Ui_MainWindow):
    data = {}
    entryText = ''
    selectBox = ''
    txt = ''
    row = -1
    infoBox = {}
    table2list = []
    table2num = 0
    line_2 = ""
    downEnd = 0
    is_done = 0

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.searchAppInfo)
        self.lineEdit.returnPressed.connect(self.searchAppInfo)
        # ????????????????????????????????????
        application_path = os.path.dirname(__file__)
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        self.lineEdit_2.setText(str(application_path))
        self.toolButton.clicked.connect(self.get_directory)
        # ????????????
        self.pushButton_2.clicked.connect(self.cleantableWidget_2)
        # ????????????
        self.pushButton_3.clicked.connect(self.clickButton_3)
        # ????????????
        self.pushButton_4.clicked.connect(self.clickButton_4)
        # ??????????????????
        self.pushButton_5.clicked.connect(self.clickButton_5)

    # ??????????????????????????????????????????
    def searchAppInfo(self):
        # ????????????????????????
        MainWin.selectBox = self.comboBox.currentText()

        # ???????????????????????????
        MainWin.entryText = self.lineEdit.text()
        # ???????????????
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        if MainWin.entryText == '':
            return
        else:
            self.tableWidget.clearContents()
            self.searchThread = SearchThread()
            self.searchThread.signalInfo.connect(self.flushTableWidget)
            # self.searchThread.signalTotal.connect(self.flushTipLabel)
            self.searchThread._signalIsRunning.connect(lambda: self.pushButton.setEnabled(True))
            self.pushButton.setEnabled(False)
            self.searchThread.start()

    def flushTableWidget(self, lst):
        MainWin.row += 1
        k = []
        v = []

        for key, value in lst.items():
            k.append(key)
            v.append(value)
        # print(k)
        # print(v)
        # print(int(MainWin.txt))
        # if MainWin.row <= int(MainWin.txt):
        row_count = self.tableWidget.rowCount()  # ??????????????????(??????)
        self.tableWidget.insertRow(row_count)  # ??????????????????

        # row_count -= 1
        # print(row_count)
        # return
        self.downloadButton = QtWidgets.QPushButton()
        # ????????????????????????
        # self.downloadButton.setIcon(QtGui.QIcon("./src/images/download.png"))
        self.downloadButton.setText("??????")
        font = QFont()
        font.setPointSize(20)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("background-color: #5A9BB3")

        try:
            # ??????????????????
            self.headWidget = QtWidgets.QWidget()
            # ????????????????????????
            self.imgLabel = QtWidgets.QLabel()
            # ????????????logo?????????????????????
            self.imgLabel.setScaledContents(True)
            self.imgLabel.setPixmap(v[6])
            # print(v)
            # ??????????????????
            self.textLabel = QtWidgets.QLabel()
            # ?????????????????????????????????
            self.textLabel.setText(k[0])
            # ???????????????????????????????????????????????????
            self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
            # ????????????????????????????????????????????????????????????
            self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
            # ?????????????????????????????????????????????
            self.hLayout.addWidget(self.textLabel)
            # ????????????????????????????????????????????????
            self.tableWidget.setCellWidget(row_count, 0, self.headWidget)
            # ?????????????????????
            self.tableWidget.setRowHeight(row_count, 60)
            # print(v[1])
            self.tableWidget.setItem(row_count, 1, v[1])
            self.tableWidget.setItem(row_count, 2, v[2])
            self.tableWidget.setItem(row_count, 3, v[3])
            self.tableWidget.setItem(row_count, 4, v[4])
            self.tableWidget.setItem(row_count, 5, v[5])
            self.tableWidget.setCellWidget(row_count, 6, self.downloadButton)
            # ??????????????????????????????
            self.downloadButton.clicked.connect(self.addDownloadList)
            self.tableWidget.setItem(row_count, 7, v[8])

        except:
            self.tableWidget.hideRow(MainWin.row)

    def addDownloadList(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Critical, '??????', '????????????????????????????????????')
            msg_box.exec_()
            return
        rowLine = self.tableWidget.currentRow()
        print(rowLine)
        # print(self.tableWidget.item(rowLine, 3).text())

        row_count = self.tableWidget_2.rowCount()  # ??????????????????(??????)
        # ?????????????????????
        for i in range(0, row_count):
            if self.tableWidget.item(rowLine, 4).text() == self.tableWidget_2.item(i, 4).text():
                msg_box = QMessageBox(QMessageBox.Information, '??????', '?????????')
                msg_box.exec_()
                return

        self.tableWidget_2.insertRow(row_count)  # ??????????????????
        # print(row_count)

        # print(MainWin.infoBox[0])
        # return
        MainWin.data = {}
        #print(MainWin.infoBox)
        if self.tableWidget.item(rowLine, 7).text() == '??????':
            photo = QtGui.QPixmap()
            photo.loadFromData(
                requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(
                    MainWin.infoBox[0][rowLine][9].lower())).content)
            MainWin.data['img'] = photo
            # print(MainWin.infoBox[0][rowLine][7])
            MainWin.data['url'] = MainWin.infoBox[0][rowLine][7]
            MainWin.data['name'] = MainWin.infoBox[0][rowLine][0]
        else:

            if 'https:' not in MainWin.infoBox[0][rowLine]['logo']:
                logUrl = 'https:' + MainWin.infoBox[0][rowLine]['logo']
            else:
                logUrl = MainWin.infoBox[0][rowLine]['logo']
            imgData = requests.get(logUrl).content
            photo = QtGui.QPixmap()
            photo.loadFromData(imgData)
            photo.scaled(32, 32, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            MainWin.data['img'] = photo
            MainWin.data['url'] = MainWin.infoBox[0][rowLine]['soft_download']
            MainWin.data['name'] = MainWin.infoBox[0][rowLine]['softname']

        # ??????????????????
        self.headWidget = QtWidgets.QWidget()
        # ????????????????????????
        self.imgLabel = QtWidgets.QLabel()
        # ????????????logo?????????????????????
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setPixmap(MainWin.data['img'])
        # ??????????????????
        self.textLabel = QtWidgets.QLabel()
        # ?????????????????????????????????
        self.textLabel.setText(MainWin.data['name'])
        # ???????????????????????????????????????????????????
        self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
        # ????????????????????????????????????????????????????????????
        self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
        # ?????????????????????????????????????????????
        self.hLayout.addWidget(self.textLabel)
        # ????????????????????????????????????????????????
        self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
        # ?????????????????????
        self.tableWidget_2.setRowHeight(row_count, 70)

        for i in range(1, 6):
            name = QtWidgets.QTableWidgetItem(self.tableWidget.item(rowLine, i).text())
            name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
            self.tableWidget_2.setItem(row_count, i, name)
        self.deleteButton = QtWidgets.QPushButton()
        self.deleteButton.setText("??????")
        font = QFont()
        font.setPointSize(20)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("background-color: #e74f4f")
        self.tableWidget_2.setCellWidget(row_count, 6, self.deleteButton)
        self.deleteButton.clicked.connect(self.deleteClicked)

        name = QtWidgets.QTableWidgetItem(MainWin.data['url'])
        name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
        self.tableWidget_2.setItem(row_count, 7, name)
        # ??????
        MainWin.table2num += 1
        self.label_5.setText("????????????" + str(MainWin.table2num) + "?????????")

    def deleteClicked(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Critical, '??????', '????????????????????????????????????')
            msg_box.exec_()
            return
        button = self.sender()
        if button:
            row = self.tableWidget_2.indexAt(button.pos()).row()
            self.tableWidget_2.removeRow(row)
        MainWin.table2num -= 1
        self.label_5.setText("????????????" + str(MainWin.table2num) + "?????????")

    def cleantableWidget_2(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Critical, '??????', '????????????????????????????????????')
            msg_box.exec_()
            return
        MainWin.table2num = 0
        self.label_5.setText("????????????0?????????")
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.clearContents()

    def get_directory(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "?????????????????????",
                                                              self.lineEdit_2.text()) or self.lineEdit_2.text()
        self.lineEdit_2.setText(str(get_directory_path))

    def addRecommendList(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Critical, '??????', '????????????????????????????????????')
            msg_box.exec_()
            return
        self.cleantableWidget_2()
        # ????????? ??????????????????????????????
        DeRecommendList = [["QQ", 1, "??????"],
                           ["360????????????", 1, "360"],
                           ["??????", 1, "??????"],
                           ["????????????", 1, "??????"],
                           ["WPS", 1, "??????"], ]

        try:
            application_path = os.path.dirname(__file__)
            if getattr(sys, 'frozen', False):
                application_path = os.path.dirname(sys.executable)
            with open(str(application_path) + "\\????????????.ini", "r", encoding='UTF-8')as f:
                res = f.read()
                pattern = re.compile(
                    r"???????????????--------------------(.*?)--------------???????????????",
                    re.I | re.S)
                RecommendList = pattern.findall(res.replace(' ', '').replace('\n', '').replace('\r', ''))
                pattern = re.compile(
                    r"\[\"(.*?)\",(.*?),\"(.*?)\"\]",
                    re.I | re.S)
                RecommendList = pattern.findall(RecommendList[0])
            f.close()
        except:
            RecommendList = DeRecommendList
            msg_box = QMessageBox(QMessageBox.Critical, '??????', '????????????????????????????????????')
            msg_box.exec_()

        # print(RecommendList)
        for lis in RecommendList:
            if lis[2] == "??????":
                infoBox = func.Tencent(lis[0]).getInfo()
                # print(list(infoBox[0].values())[0])
                item = list(infoBox[0].values())[int(lis[1]) - 1]
                info = {}
                # item[2] == osbit(????????????)
                # ????????????2??????64???
                if item[2] == '2':
                    item[1] += '64???'

                # ?????????????????????????????????????????????
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[0]] = name
                version = QtWidgets.QTableWidgetItem(item[1])
                version.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[1]] = version
                fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3] or 0) / (1024 * 1024))) + "M")
                fileSize.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[3]] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(item[4])
                publishDate.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[4]] = publishDate
                desc = QtWidgets.QTableWidgetItem(item[5])
                desc.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[5]] = desc
                rank = QtWidgets.QTableWidgetItem(str(int(item[6] or 0) / 10) + "???")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[6]] = rank
                photo = QtGui.QPixmap()
                photo.loadFromData(
                    requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(item[9].lower())).content)
                info['img'] = photo
                dUrl = item[7]
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("??????")
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info['sou'] = sou

                # print(info)
                # ????????????
                row_count = self.tableWidget_2.rowCount()  # ??????????????????(??????)
                self.tableWidget_2.insertRow(row_count)  # ??????????????????

                # ??????????????????
                self.headWidget = QtWidgets.QWidget()
                # ????????????????????????
                self.imgLabel = QtWidgets.QLabel()
                # ????????????logo?????????????????????
                self.imgLabel.setScaledContents(True)
                self.imgLabel.setPixmap(info['img'])
                # ??????????????????
                self.textLabel = QtWidgets.QLabel()
                # ?????????????????????????????????
                self.textLabel.setText(item[0])
                # ???????????????????????????????????????????????????
                self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
                # ????????????????????????????????????????????????????????????
                self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
                # ?????????????????????????????????????????????
                self.hLayout.addWidget(self.textLabel)
                # ????????????????????????????????????????????????
                self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
                # ?????????????????????
                self.tableWidget_2.setRowHeight(row_count, 70)

                for i in range(1, 6):
                    name = QtWidgets.QTableWidgetItem(list(info.values())[i])
                    name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                    self.tableWidget_2.setItem(row_count, i, name)
                self.deleteButton = QtWidgets.QPushButton()
                self.deleteButton.setText("??????")
                font = QFont()
                font.setPointSize(20)
                self.deleteButton.setFont(font)
                self.deleteButton.setStyleSheet("background-color: #e74f4f")
                self.tableWidget_2.setCellWidget(row_count, 6, self.deleteButton)
                self.deleteButton.clicked.connect(self.deleteClicked)

                name = QtWidgets.QTableWidgetItem(info['url'])
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                self.tableWidget_2.setItem(row_count, 7, name)
                # ??????
                MainWin.table2num += 1
                # self.label_5.setText("????????????" + str(MainWin.table2num) + "?????????")

            elif lis[2] == "360":
                infoBox = func.QiHu(lis[0]).getInfo()
                value = list(infoBox[0].values())[int(lis[1]) - 1]
                info = {}
                # ?????????????????????????????????????????????
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['softname']] = name
                version = QtWidgets.QTableWidgetItem(value['version'])
                version.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['version']] = version
                fileSize = QtWidgets.QTableWidgetItem(value['size'])
                fileSize.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['size']] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(value['date'])
                publishDate.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['date']] = publishDate
                desc = QtWidgets.QTableWidgetItem(value['desc'])
                desc.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['desc']] = desc
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "???")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['poll']] = rank
                if 'https:' not in value['logo']:
                    logUrl = 'https:' + value['logo']
                else:
                    logUrl = value['logo']
                if not value['logo']:
                    logUrl = "http://img.product.it168.com/product/1402364.jpg"
                imgData = requests.get(logUrl).content
                photo = QtGui.QPixmap()
                photo.loadFromData(imgData)
                photo.scaled(32, 32, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                info['img'] = photo
                dUrl = value['soft_download']
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("360")
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info['sou'] = sou

                # ????????????
                row_count = self.tableWidget_2.rowCount()  # ??????????????????(??????)
                self.tableWidget_2.insertRow(row_count)  # ??????????????????

                # ??????????????????
                self.headWidget = QtWidgets.QWidget()
                # ????????????????????????
                self.imgLabel = QtWidgets.QLabel()
                # ????????????logo?????????????????????
                self.imgLabel.setScaledContents(True)
                self.imgLabel.setPixmap(info['img'])
                # ??????????????????
                self.textLabel = QtWidgets.QLabel()
                # ?????????????????????????????????
                self.textLabel.setText(value['softname'])
                # ???????????????????????????????????????????????????
                self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
                # ????????????????????????????????????????????????????????????
                self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
                # ?????????????????????????????????????????????
                self.hLayout.addWidget(self.textLabel)
                # ????????????????????????????????????????????????
                self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
                # ?????????????????????
                self.tableWidget_2.setRowHeight(row_count, 70)

                for i in range(1, 6):
                    name = QtWidgets.QTableWidgetItem(list(info.values())[i])
                    name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                    self.tableWidget_2.setItem(row_count, i, name)
                self.deleteButton = QtWidgets.QPushButton()
                self.deleteButton.setText("??????")
                font = QFont()
                font.setPointSize(20)
                self.deleteButton.setFont(font)
                self.deleteButton.setStyleSheet("background-color: #e74f4f")
                self.tableWidget_2.setCellWidget(row_count, 6, self.deleteButton)
                self.deleteButton.clicked.connect(self.deleteClicked)

                name = QtWidgets.QTableWidgetItem(info['url'])
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                self.tableWidget_2.setItem(row_count, 7, name)
                # ??????
                MainWin.table2num += 1

        self.label_5.setText("????????????" + str(MainWin.table2num) + "?????????")

    def click(self):
        return

    def menuButton(self):
        from core import about
        dialog = QDialog()
        dialog_help = about.Ui_Dialog()
        dialog_help.setupUi(dialog)
        dialog.exec_()

    def clickButton_5(self):
        os.startfile(self.lineEdit_2.text())

    def clickButton_4(self):
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setText("?????????")
        QApplication.processEvents()
        self.addRecommendList()
        self.pushButton_4.setText("????????????")
        self.pushButton_4.setEnabled(True)

    def clickButton_3(self):
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setText("?????????")
        QApplication.processEvents()

        MainWin.line_2 = self.lineEdit_2.text()
        if not self.tableWidget_2.rowCount():
            self.pushButton_3.setText("????????????")
            self.pushButton_3.setEnabled(True)
            return
        # ???????????????
        #print(self.tableWidget_2.rowCount())
        i = 1
        while i == 1:
            if self.tableWidget_2.rowCount() and self.tableWidget_2.item(0, 4).text() == "????????????":
                self.tableWidget_2.removeRow(0)
            else:
                i = 2

        row_count = self.tableWidget_2.rowCount()
        MainWin.table2num = row_count
        self.label_5.setText("????????????"+str(MainWin.table2num)+"?????????")
        if not row_count:
            self.pushButton_3.setText("????????????")
            self.pushButton_3.setEnabled(True)
            return

        for row in range(0, row_count):
            MainWin.table2list.append(self.tableWidget_2.item(row, 7).text())
            font = QFont()
            font.setPointSize(15)
            self.tableWidget_2.item(row, 4).setFont(font)
            self.tableWidget_2.item(row, 4).setText("????????????")
        # QApplication.processEvents()
        self.downloadThread = DownloadThread()
        self.downloadThread.signal.connect(self.flushValue)
        self.downloadThread.start()

    def flushValue(self, value):
            #print(value)

            if value[0] == -1:
                print('done')
                row_count = self.tableWidget_2.rowCount()
                print(row_count)
                self.tableWidget_2.item(row_count-1, 4).setText("????????????")
                self.downloadThread.exit(0)
                MainWin.is_done = 0
                self.pushButton_3.setText("????????????")
                self.pushButton_3.setEnabled(True)
                QMessageBox.information(self, "??????", "??????????????????", QMessageBox.Yes, QMessageBox.Yes)
                return

            #print(str(value[1]))
            self.tableWidget_2.item(int(value[0]), 4).setText(str(value[1])+'%')
            #QApplication.processEvents()
            if MainWin.is_done != int(value[0]):
                self.tableWidget_2.item(int(value[0])-1, 4).setText("????????????")
            MainWin.is_done = int(value[0])



class DownloadThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)
    def run(self):
        data = MainWin.table2list
        MainWin.downEnd = 1
        for row, url in enumerate(data):

            try:
                res = requests.get(url, stream=True)

                # ??????????????????
                fileSize = res.headers['Content-Length']
                chunk_size = 102400
                chunk_temp = 0
                name = url.split('/')[-1]
                #print(MainWin.line_2 + "\\" + name)
                with open(MainWin.line_2 + "\\" + name, 'wb') as f:
                    for chunk in res.iter_content(chunk_size=chunk_size):
                        if chunk:
                            temp = "%.2f" % (chunk_temp / float(fileSize) * 100)
                            f.write(chunk)
                        chunk_temp += chunk_size
                        #print([row, temp])
                        self.signal.emit([row, temp])
                f.close()
            except:
                continue
            time.sleep(0.5)
        self.signal.emit([-1, 1])
        MainWin.table2list = []
        MainWin.downEnd = 0


class SearchThread(QtCore.QThread):
    signalTotal = QtCore.pyqtSignal(str)
    signalInfo = QtCore.pyqtSignal(dict)
    _signalIsRunning = QtCore.pyqtSignal()

    def run(self):
        MainWin.infoBox = {}
        if MainWin.selectBox == "??????":
            # ??????????????????????????????
            MainWin.infoBox = func.Tencent(MainWin.entryText).getInfo()

            # ??????????????????????????????
            # infoBox[1][0] = ????????????????????????
            self.signalTotal.emit(MainWin.infoBox[1][0])
            # ??????????????????????????????
            # print(MainWin.infoBox[0].items())
            for key, item in MainWin.infoBox[0].items():
                info = {}
                # item[2] == osbit(????????????)
                # ????????????2??????64???
                if item[2] == '2':
                    item[1] += '64???'

                # ?????????????????????????????????????????????
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[0]] = name
                version = QtWidgets.QTableWidgetItem(item[1])
                version.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[1]] = version
                fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3] or 0) / (1024 * 1024))) + "M")
                fileSize.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[3]] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(item[4])
                publishDate.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[4]] = publishDate
                desc = QtWidgets.QTableWidgetItem(item[5])
                desc.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[5]] = desc
                #print(item)
                rank = QtWidgets.QTableWidgetItem(str(int(item[6] or 0) / 10) + "???")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[6]] = rank
                photo = QtGui.QPixmap()
                photo.loadFromData(
                    requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(item[9].lower())).content)
                info['img'] = photo
                dUrl = item[7]
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("??????")
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info['sou'] = sou
                # print(info)
                self.signalInfo.emit(info)
            time.sleep(1)
            MainWin.row = -1
            self._signalIsRunning.emit()
        if MainWin.selectBox == "360":
            # ??????????????????????????????
            MainWin.infoBox = func.QiHu(MainWin.entryText).getInfo()
            self.signalTotal.emit(str(MainWin.infoBox[1]))
            for value in MainWin.infoBox[0].values():
                info = {}
                # ?????????????????????????????????????????????
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['softname']] = name
                version = QtWidgets.QTableWidgetItem(value['version'])
                version.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['version']] = version
                fileSize = QtWidgets.QTableWidgetItem(value['size'])
                fileSize.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['size']] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(value['date'])
                publishDate.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['date']] = publishDate
                desc = QtWidgets.QTableWidgetItem(value['desc'])
                desc.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['desc']] = desc
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "???")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['poll']] = rank
                if 'https:' not in value['logo']:
                    logUrl = 'https:' + value['logo']
                else:
                    logUrl = value['logo']
                if not value['logo']:
                    logUrl = "http://img.product.it168.com/product/1402364.jpg"
                imgData = requests.get(logUrl).content
                photo = QtGui.QPixmap()
                photo.loadFromData(imgData)
                photo.scaled(32, 32, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                info['img'] = photo
                dUrl = value['soft_download']
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("360")
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info['sou'] = sou
                self.signalInfo.emit(info)
            time.sleep(1)
            MainWin.row = -1
            self._signalIsRunning.emit()

        if MainWin.selectBox == "??????":
            # ??????????????????????????????
            mainlist = {}
            infoBox = func.Tencent(MainWin.entryText).getInfo()
            i = 0
            for key, item in infoBox[0].items():
                if MainWin.entryText in item[0]:
                    mainlist[i] = item
                    i += 1
            Box = {}
            MainWin.infoBox = [mainlist, infoBox[1][0]]
            # print(MainWin.infoBox[0].items())
            # ??????????????????????????????
            # infoBox[1][0] = ????????????????????????
            #self.signalTotal.emit(MainWin.infoBox[1][0])
            # ??????????????????????????????
            # print(MainWin.infoBox[0].items())
            for key, item in infoBox[0].items():
                info = {}

                # ???????????????
                if MainWin.entryText not in item[0]:
                    print("skip")
                    continue

                Box[key] = item
                # item[2] == osbit(????????????)
                # ????????????2??????64???
                if item[2] == '2':
                    item[1] += '64???'

                # ?????????????????????????????????????????????
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[0]] = name
                version = QtWidgets.QTableWidgetItem(item[1])
                version.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[1]] = version
                fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3] or 0) / (1024 * 1024))) + "M")
                fileSize.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[3]] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(item[4])
                publishDate.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[4]] = publishDate
                desc = QtWidgets.QTableWidgetItem(item[5])
                desc.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[5]] = desc
                rank = QtWidgets.QTableWidgetItem(str(int(item[6] or 0) / 10) + "???")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[6]] = rank
                photo = QtGui.QPixmap()
                photo.loadFromData(
                    requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(item[9].lower())).content)
                info['img'] = photo
                dUrl = item[7]
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("??????")
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info['sou'] = sou
                # print(info)
                self.signalInfo.emit(info)

            # time.sleep(1)
            # MainWin.row = -1


            # ??????????????????????????????
            infobox360 = func.QiHu(MainWin.entryText).getInfo()
            for item in infobox360[0].values():
                if MainWin.entryText in item['softname']:
                    mainlist[i] = item
                    i += 1

            MainWin.infoBox = [mainlist, int(infoBox[1][0])+int(infobox360[1])]
            print(MainWin.infoBox)
            box360 = {}
            # self.signalTotal.emit(str(infobox360[1]))
            # print(infobox360[0].values())
            for key, value in infobox360[0].items():
                info = {}

                # ???????????????
                if MainWin.entryText not in value['softname']:
                    print("skip360")
                    continue

                box360[key] = value
                # ?????????????????????????????????????????????
                # print("111111")
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['softname']] = name
                version = QtWidgets.QTableWidgetItem(value['version'])
                version.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['version']] = version
                fileSize = QtWidgets.QTableWidgetItem(value['size'])
                fileSize.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['size']] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(value['date'])
                publishDate.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['date']] = publishDate
                desc = QtWidgets.QTableWidgetItem(value['desc'])
                desc.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['desc']] = desc
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "???")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['poll']] = rank
                if 'https:' not in value['logo']:
                    logUrl = 'https:' + value['logo']
                else:
                    logUrl = value['logo']
                if not value['logo']:
                    logUrl = "http://img.product.it168.com/product/1402364.jpg"

                imgData = requests.get(logUrl).content
                photo = QtGui.QPixmap()
                photo.loadFromData(imgData)
                photo.scaled(32, 32, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                info['img'] = photo
                dUrl = value['soft_download']
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("360")
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info['sou'] = sou
                self.signalInfo.emit(info)
            # print(box360)
            time.sleep(1)
            MainWin.row = -1
            self._signalIsRunning.emit()
