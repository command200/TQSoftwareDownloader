# -*- coding: utf-8 -*-
import json
import os
import re

from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtGui import QFont, QAction
from PyQt6.QtWidgets import QMessageBox, QFileDialog, QApplication, QDialog, QSizePolicy

import Main
from core import func

import sys
import requests
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED, as_completed


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1196, 640)
        MainWindow.setMinimumSize(800, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)

        top_layout = QtWidgets.QHBoxLayout()
        top_layout.setSpacing(10)

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setObjectName("label")
        top_layout.addWidget(self.label)

        top_layout.addStretch(1)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("填写查找内容")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFixedWidth(180)
        top_layout.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        top_layout.addWidget(self.pushButton)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        top_layout.addWidget(self.label_2)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        top_layout.addWidget(self.comboBox)

        main_layout.addLayout(top_layout)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        for i in range(8):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        main_layout.addWidget(self.tableWidget)

        middle_layout = QtWidgets.QHBoxLayout()
        middle_layout.setSpacing(10)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setObjectName("label_4")
        middle_layout.addWidget(self.label_4)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        middle_layout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        middle_layout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        middle_layout.addWidget(self.pushButton_4)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        middle_layout.addWidget(self.label_3)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        middle_layout.addWidget(self.lineEdit_2)

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        middle_layout.addWidget(self.toolButton)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        middle_layout.addWidget(self.pushButton_5)

        middle_layout.addStretch(1)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        middle_layout.addWidget(self.label_5)

        main_layout.addLayout(middle_layout)

        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        for i in range(8):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setHorizontalHeaderItem(i, item)

        main_layout.addWidget(self.tableWidget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "软件下载器"))
        self.pushButton.setText(_translate("MainWindow", "搜索"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "填写查找内容"))
        self.label.setText(_translate("MainWindow", "软件下载器"))
        self.comboBox.setCurrentText(_translate("MainWindow", "腾讯"))
        self.comboBox.setItemText(0, _translate("MainWindow", "腾讯"))
        self.comboBox.setItemText(1, _translate("MainWindow", "360"))
        # self.comboBox.setItemText(2, _translate("MainWindow", "聚合"))
        self.label_2.setText(_translate("MainWindow", "软件库："))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "下载路径："))

        headers = ["名称", "版本", "大小", "发布日期", "描述", "评分", "操作", "来源"]
        for i, header in enumerate(headers):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", header))

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        headers_2 = ["名称", "版本", "大小", "发布日期", "描述", "评分", "操作", "链接"]
        for i, header in enumerate(headers_2):
            item = self.tableWidget_2.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", header))

        self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.label_4.setText(_translate("MainWindow", "已添加列表"))
        self.pushButton_2.setText(_translate("MainWindow", "清空列表"))
        self.pushButton_3.setText(_translate("MainWindow", "一键下载"))
        self.pushButton_4.setText(_translate("MainWindow", "推荐软件"))
        self.pushButton_5.setText(_translate("MainWindow", "打开下载目录"))
        self.label_5.setText(_translate("MainWindow", "共添加了0个软件"))

        self.localfile_action = QAction(MainWindow)
        self.localfile_action.setCheckable(False)
        self.localfile_action.setObjectName('aboutAction')
        self.localfile_action.triggered.connect(MainWin.menuButton)
        self.localfile_action.setText('关于')
        self.menubar.addAction(self.localfile_action)


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
    downNum = 0

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.searchAppInfo)
        self.lineEdit.returnPressed.connect(self.searchAppInfo)

        application_path = os.path.dirname(os.path.dirname(__file__))
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        self.lineEdit_2.setText(str(application_path))
        self.toolButton.clicked.connect(self.get_directory)

        self.pushButton_2.clicked.connect(self.cleantableWidget_2)
        self.pushButton_3.clicked.connect(self.clickButton_3)
        self.pushButton_4.clicked.connect(self.clickButton_4)
        self.pushButton_5.clicked.connect(self.clickButton_5)

        self.downloadThread = None

    def closeEvent(self, event):
        DownloadThread.is_exit = 1
        event.accept()

    def searchAppInfo(self):
        MainWin.selectBox = self.comboBox.currentText()

        MainWin.entryText = self.lineEdit.text()

        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        if MainWin.entryText == '':
            return
        else:
            self.tableWidget.clearContents()
            self.searchThread = SearchThread()
            self.searchThread.signalInfo.connect(self.flushTableWidget)
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

        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)

        self.downloadButton = QtWidgets.QPushButton()
        self.downloadButton.setText("添加")
        font = QFont()
        font.setPointSize(20)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("background-color: #5A9BB3")

        try:
            self.headWidget = QtWidgets.QWidget()
            self.imgLabel = QtWidgets.QLabel()
            self.imgLabel.setFixedSize(48, 48)
            self.imgLabel.setScaledContents(True)
            self.imgLabel.setPixmap(v[6])
            self.textLabel = QtWidgets.QLabel()
            self.textLabel.setText(k[0])
            self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
            self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hLayout.addWidget(self.textLabel)
            self.tableWidget.setCellWidget(row_count, 0, self.headWidget)
            self.tableWidget.setRowHeight(row_count, 60)

            self.tableWidget.setItem(row_count, 1, v[1])
            self.tableWidget.setItem(row_count, 2, v[2])
            self.tableWidget.setItem(row_count, 3, v[3])
            self.tableWidget.setItem(row_count, 4, v[4])
            self.tableWidget.setItem(row_count, 5, v[5])
            self.tableWidget.setCellWidget(row_count, 6, self.downloadButton)
            self.downloadButton.clicked.connect(self.addDownloadList)
            self.tableWidget.setItem(row_count, 7, v[8])

        except:
            self.tableWidget.hideRow(MainWin.row)

    def addDownloadList(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Icon.Critical, '错误', '请等待全部下载完成后操作')
            msg_box.exec()
            return
        rowLine = self.tableWidget.currentRow()

        row_count = self.tableWidget_2.rowCount()
        for i in range(0, row_count):
            if self.tableWidget.item(rowLine, 4).text() == self.tableWidget_2.item(i, 4).text():
                msg_box = QMessageBox(QMessageBox.Icon.Information, '提示', '已添加')
                msg_box.exec()
                return

        self.tableWidget_2.insertRow(row_count)

        MainWin.data = {}
        if self.tableWidget.item(rowLine, 7).text() == '腾讯':
            photo = QtGui.QPixmap()
            try:
                photo.loadFromData(
                    requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(
                        MainWin.infoBox[0][rowLine][9].lower())).content)
            except:
                pass
            MainWin.data['img'] = photo
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
            photo.scaled(32, 32, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
            MainWin.data['img'] = photo
            MainWin.data['url'] = MainWin.infoBox[0][rowLine]['soft_download']
            MainWin.data['name'] = MainWin.infoBox[0][rowLine]['softname']

        self.headWidget = QtWidgets.QWidget()
        self.imgLabel = QtWidgets.QLabel()
        self.imgLabel.setFixedSize(48, 48)
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setPixmap(MainWin.data['img'])
        self.textLabel = QtWidgets.QLabel()
        self.textLabel.setText(MainWin.data['name'])
        self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
        self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hLayout.addWidget(self.textLabel)
        self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
        self.tableWidget_2.setRowHeight(row_count, 70)

        for i in range(1, 6):
            name = QtWidgets.QTableWidgetItem(self.tableWidget.item(rowLine, i).text())
            name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
            self.tableWidget_2.setItem(row_count, i, name)
        self.deleteButton = QtWidgets.QPushButton()
        self.deleteButton.setText("删除")
        font = QFont()
        font.setPointSize(20)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("background-color: #e74f4f")
        self.tableWidget_2.setCellWidget(row_count, 6, self.deleteButton)
        self.deleteButton.clicked.connect(self.deleteClicked)

        name = QtWidgets.QTableWidgetItem(MainWin.data['url'])
        name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
        self.tableWidget_2.setItem(row_count, 7, name)

        MainWin.table2num += 1
        self.label_5.setText("共添加了" + str(MainWin.table2num) + "个软件")

    def deleteClicked(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Icon.Critical, '错误', '请等待全部下载完成后操作')
            msg_box.exec()
            return
        button = self.sender()
        if button:
            row = self.tableWidget_2.indexAt(button.pos()).row()
            self.tableWidget_2.removeRow(row)
        MainWin.table2num -= 1
        self.label_5.setText("共添加了" + str(MainWin.table2num) + "个软件")

    def cleantableWidget_2(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Icon.Critical, '错误', '请等待全部下载完成后操作')
            msg_box.exec()
            return
        MainWin.table2num = 0
        self.label_5.setText("共添加了0个软件")
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.clearContents()

    def get_directory(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              self.lineEdit_2.text()) or self.lineEdit_2.text()
        self.lineEdit_2.setText(str(get_directory_path))

    def addRecommendList(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Icon.Critical, '错误', '请等待全部下载完成后操作')
            msg_box.exec()
            return
        self.cleantableWidget_2()
        DeRecommendList = [["QQ", 1, "腾讯"],
                           ["微信", 1, "腾讯"],
                           ["钉钉64位", 1, "360"],
                           ["企业微信", 1, "腾讯"],
                           ["火绒", "https://www.huorong.cn/product/downloadHr60.php?pro=hr60", "火绒"],
                           ]

        try:
            application_path = os.path.dirname(os.path.dirname(__file__))
            if getattr(sys, 'frozen', False):
                application_path = os.path.dirname(sys.executable)
            with open(os.path.join(application_path, "推荐列表.ini"), "r", encoding='UTF-8') as f:
                res = f.read()
                pattern = re.compile(
                    r"在下面添加--------------------(.*?)--------------在上面添加",
                    re.I | re.S)
                RecommendList = pattern.findall(res.replace(' ', '').replace('\n', '').replace('\r', ''))
                pattern = re.compile(
                    r"\[\"(.*?)\",(.*?),\"(.*?)\"\]",
                    re.I | re.S)
                RecommendList = pattern.findall(RecommendList[0])
            f.close()
        except:
            RecommendList = DeRecommendList
            msg_box = QMessageBox(QMessageBox.Icon.Critical, '错误', '无法读取列表将变更为默认')
            msg_box.exec()

        total = len(RecommendList)
        for i, lis in enumerate(RecommendList):
            self.updateProgress(f"正在读取推荐列表... ({i+1}/{total})")
            if lis[2] == "腾讯":
                self.updateProgress(f"正在获取 {lis[0]} 信息...")
                infoBox = func.Tencent(lis[0]).getInfo()
                item = list(infoBox[0].values())[int(lis[1]) - 1]
                info = {}

                if item[2] == '2':
                    item[1] += '64位'

                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[0]] = name
                version = QtWidgets.QTableWidgetItem(item[1])
                version.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[1]] = version
                fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3] or 0) / (1024 * 1024))) + "M")
                fileSize.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[3]] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(item[4])
                publishDate.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[4]] = publishDate
                desc = QtWidgets.QTableWidgetItem(item[5])
                desc.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[5]] = desc
                rank = QtWidgets.QTableWidgetItem(str(int(item[6] or 0) / 10) + "分")
                rank.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[6]] = rank
                photo = QtGui.QPixmap()
                self.updateProgress(f"正在下载 {lis[0]} 图标...")
                photo.loadFromData(
                    requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(item[9].lower())).content)
                info['img'] = photo
                dUrl = item[7]
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("腾讯")
                sou.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info['sou'] = sou

                row_count = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_count)

                self.headWidget = QtWidgets.QWidget()
                self.imgLabel = QtWidgets.QLabel()
                self.imgLabel.setFixedSize(48, 48)
                self.imgLabel.setScaledContents(True)
                self.imgLabel.setPixmap(info['img'])
                self.textLabel = QtWidgets.QLabel()
                self.textLabel.setText(item[0])
                self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
                self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
                self.hLayout.addWidget(self.textLabel)
                self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
                self.tableWidget_2.setRowHeight(row_count, 70)

                info_values = list(info.values())
                for i in range(1, 6):
                    self.tableWidget_2.setItem(row_count, i, info_values[i])
                self.deleteButton = QtWidgets.QPushButton()
                self.deleteButton.setText("删除")
                font = QFont()
                font.setPointSize(20)
                self.deleteButton.setFont(font)
                self.deleteButton.setStyleSheet("background-color: #e74f4f")
                self.tableWidget_2.setCellWidget(row_count, 6, self.deleteButton)
                self.deleteButton.clicked.connect(self.deleteClicked)

                url_item = QtWidgets.QTableWidgetItem(info['url'])
                url_item.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                self.tableWidget_2.setItem(row_count, 7, url_item)

                MainWin.table2num += 1

            elif lis[2] == "360":
                self.updateProgress(f"正在获取 {lis[0]} 信息...")
                infoBox = func.QiHu(lis[0]).getInfo()
                value = list(infoBox[0].values())[int(lis[1]) - 1]
                info = {}

                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['softname']] = name
                version = QtWidgets.QTableWidgetItem(value['version'])
                version.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['version']] = version
                fileSize = QtWidgets.QTableWidgetItem(value['size'])
                fileSize.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['size']] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(value['date'])
                publishDate.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['date']] = publishDate
                desc = QtWidgets.QTableWidgetItem(value['desc'])
                desc.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['desc']] = desc
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "分")
                rank.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['poll']] = rank
                if 'https:' not in value['logo']:
                    logUrl = 'https:' + value['logo']
                else:
                    logUrl = value['logo']
                if not value['logo']:
                    logUrl = "http://img.product.it168.com/product/1402364.jpg"
                self.updateProgress(f"正在下载 {lis[0]} 图标...")
                imgData = requests.get(logUrl).content
                photo = QtGui.QPixmap()
                photo.loadFromData(imgData)
                photo.scaled(32, 32, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
                info['img'] = photo
                dUrl = value['soft_download']
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("360")
                sou.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info['sou'] = sou

                row_count = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_count)

                self.headWidget = QtWidgets.QWidget()
                self.imgLabel = QtWidgets.QLabel()
                self.imgLabel.setFixedSize(48, 48)
                self.imgLabel.setScaledContents(True)
                self.imgLabel.setPixmap(info['img'])
                self.textLabel = QtWidgets.QLabel()
                self.textLabel.setText(value['softname'])
                self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
                self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
                self.hLayout.addWidget(self.textLabel)
                self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
                self.tableWidget_2.setRowHeight(row_count, 70)

                info_values = list(info.values())
                for i in range(1, 6):
                    self.tableWidget_2.setItem(row_count, i, info_values[i])
                self.deleteButton = QtWidgets.QPushButton()
                self.deleteButton.setText("删除")
                font = QFont()
                font.setPointSize(20)
                self.deleteButton.setFont(font)
                self.deleteButton.setStyleSheet("background-color: #e74f4f")
                self.tableWidget_2.setCellWidget(row_count, 6, self.deleteButton)
                self.deleteButton.clicked.connect(self.deleteClicked)

                url_item = QtWidgets.QTableWidgetItem(info['url'])
                url_item.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                self.tableWidget_2.setItem(row_count, 7, url_item)

                MainWin.table2num += 1
            else:
                self.updateProgress(f"正在获取 {lis[0]} 信息...")
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                if "http" in lis[1]:
                    dUrl = lis[1].replace("\"", "")
                else:
                    dUrl = "无效链接"
                if lis[2] == "火绒":
                    headers = {
                        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/129.0.0.0 Safari/537.36"}
                    res1 = requests.get(dUrl, headers=headers)
                    dUrl = res1.url
                sou = QtWidgets.QTableWidgetItem(lis[2])
                sou.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)

                row_count = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_count)

                self.headWidget = QtWidgets.QWidget()
                self.imgLabel = QtWidgets.QLabel()
                self.imgLabel.setFixedSize(48, 48)
                self.imgLabel.setScaledContents(True)
                self.textLabel = QtWidgets.QLabel()
                self.textLabel.setText(lis[0])
                self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
                self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
                self.hLayout.addWidget(self.textLabel)
                self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
                self.tableWidget_2.setRowHeight(row_count, 70)

                for i in range(1, 6):
                    name = QtWidgets.QTableWidgetItem("")
                    name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                    self.tableWidget_2.setItem(row_count, i, name)
                self.deleteButton = QtWidgets.QPushButton()
                self.deleteButton.setText("删除")
                font = QFont()
                font.setPointSize(20)
                self.deleteButton.setFont(font)
                self.deleteButton.setStyleSheet("background-color: #e74f4f")
                self.tableWidget_2.setCellWidget(row_count, 6, self.deleteButton)
                self.deleteButton.clicked.connect(self.deleteClicked)

                name = QtWidgets.QTableWidgetItem(dUrl)
                name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                self.tableWidget_2.setItem(row_count, 7, name)

                MainWin.table2num += 1

        self.label_5.setText("共添加了" + str(MainWin.table2num) + "个软件")

    def click(self):
        return

    def menuButton(self):
        from core import about
        dialog = QDialog()
        dialog_help = about.Ui_Dialog()
        dialog_help.setupUi(dialog)
        dialog.exec()

    def clickButton_5(self):
        os.startfile(self.lineEdit_2.text())

    def clickButton_4(self):
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setText("读取中")
        QApplication.processEvents()
        self.addRecommendList()
        self.pushButton_4.setText("推荐软件")
        self.pushButton_4.setEnabled(True)

    def updateProgress(self, msg):
        self.label_5.setText(msg)
        QApplication.processEvents()

    def clickButton_3(self):
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setText("下载中")
        QApplication.processEvents()

        MainWin.line_2 = self.lineEdit_2.text()
        if not self.tableWidget_2.rowCount():
            self.pushButton_3.setText("一键下载")
            self.pushButton_3.setEnabled(True)
            return

        i = 1
        while i == 1:
            if self.tableWidget_2.rowCount() and self.tableWidget_2.item(0, 4).text() == "下载完成":
                self.tableWidget_2.removeRow(0)
            else:
                i = 2

        row_count = self.tableWidget_2.rowCount()
        MainWin.table2num = row_count
        self.label_5.setText("共添加了" + str(MainWin.table2num) + "个软件")
        if not row_count:
            self.pushButton_3.setText("一键下载")
            self.pushButton_3.setEnabled(True)
            return

        for row in range(0, row_count):
            MainWin.table2list.append(self.tableWidget_2.item(row, 7).text())
            font = QFont()
            font.setPointSize(15)
            self.tableWidget_2.item(row, 4).setFont(font)
            self.tableWidget_2.item(row, 4).setText("等待下载")

        self.downloadThread = DownloadThread()
        self.downloadThread.signal.connect(self.flushValue)
        self.downloadThread.start()

    def flushValue(self, value):
        if value[0] == -1:
            self.label_5.setText(
                "共添加" + str(MainWin.table2num) + "个软件" + "已完成" + str(MainWin.table2num) + "个")
            row_count = self.tableWidget_2.rowCount()
            self.tableWidget_2.item(row_count - 1, 4).setText("下载完成")
            self.downloadThread.exit(0)
            MainWin.is_done = 0
            MainWin.downNum = 0
            self.pushButton_3.setText("一键下载")
            self.pushButton_3.setEnabled(True)
            QMessageBox.information(self, "通知", "全部下载完毕", QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Yes)
            return

        if value[1] == -1:
            self.tableWidget_2.item(value[0], 4).setText("下载完成")
            MainWin.downNum += 1
        else:
            self.tableWidget_2.item(value[0], 4).setText(str(value[1]) + '%')
        self.label_5.setText("共添加" + str(MainWin.table2num) + "个软件" + "已完成" + str(MainWin.downNum) + "个")


class DownloadThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)
    Drow = -1
    Durl = ""
    is_exit = 0

    def run(self):
        data = MainWin.table2list
        MainWin.downEnd = 1
        DownloadThread.num = len(data)
        list = []
        for row, url in enumerate(data):
            list.append([row, url])
        pool = ThreadPoolExecutor(max_workers=10)
        all_task = [pool.submit(self.doDownload, i) for i in list]
        wait(all_task, timeout=None, return_when=ALL_COMPLETED)
        print("----complete-----")
        pool.shutdown()

        self.signal.emit([-1, 1])
        MainWin.table2list = []
        MainWin.downEnd = 0

    def doDownload(self, val):
        url = val[1]
        row = val[0]
        try:
            res = requests.get(url, stream=True)

            fileSize = res.headers['Content-Length']
            chunk_size = 102400
            chunk_temp = 0
            name = url.split('/')[-1]
            with open(MainWin.line_2 + "\\" + name, 'wb') as f:
                for chunk in res.iter_content(chunk_size=chunk_size):
                    if DownloadThread.is_exit == 1:
                        return
                    if chunk:
                        temp = "%.2f" % (chunk_temp / float(fileSize) * 100)
                        f.write(chunk)
                    chunk_temp += chunk_size
                    self.signal.emit([row, temp])
            self.signal.emit([row, -1])
            f.close()
        except Exception as e:
            print(e)
        finally:
            return


class SearchThread(QtCore.QThread):
    signalTotal = QtCore.pyqtSignal(str)
    signalInfo = QtCore.pyqtSignal(dict)
    _signalIsRunning = QtCore.pyqtSignal()

    def run(self):
        MainWin.infoBox = {}
        if MainWin.selectBox == "腾讯":
            MainWin.infoBox = func.Tencent(MainWin.entryText).getInfo()
            self.signalTotal.emit(MainWin.infoBox[1][0])

            for key, item in MainWin.infoBox[0].items():
                info = {}

                if item[2] == '2':
                    item[1] += '64位'

                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[0]] = name
                version = QtWidgets.QTableWidgetItem(item[1])
                version.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[1]] = version
                fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3] or 0) / (1024 * 1024))) + "M")
                fileSize.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[3]] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(item[4])
                publishDate.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[4]] = publishDate
                desc = QtWidgets.QTableWidgetItem(item[5])
                desc.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[5]] = desc
                rank = QtWidgets.QTableWidgetItem(str(int(item[6] or 0) / 10) + "分")
                rank.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[6]] = rank
                photo = QtGui.QPixmap()
                try:
                    photo.loadFromData(
                        requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(item[9].lower())).content)
                except:
                    pass
                info['img'] = photo
                dUrl = item[7]
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("腾讯")
                sou.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info['sou'] = sou
                self.signalInfo.emit(info)
            time.sleep(1)
            MainWin.row = -1
            self._signalIsRunning.emit()
        if MainWin.selectBox == "360":
            MainWin.infoBox = func.QiHu(MainWin.entryText).getInfo()
            self.signalTotal.emit(str(MainWin.infoBox[1]))
            for value in MainWin.infoBox[0].values():
                info = {}

                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['softname']] = name
                version = QtWidgets.QTableWidgetItem(value['version'])
                version.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['version']] = version
                fileSize = QtWidgets.QTableWidgetItem(value['size'])
                fileSize.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['size']] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(value['date'])
                publishDate.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['date']] = publishDate
                desc = QtWidgets.QTableWidgetItem(value['desc'])
                desc.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['desc']] = desc
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "分")
                rank.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
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
                photo.scaled(32, 32, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
                info['img'] = photo
                dUrl = value['soft_download']
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("360")
                sou.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info['sou'] = sou
                self.signalInfo.emit(info)
            time.sleep(1)
            MainWin.row = -1
            self._signalIsRunning.emit()

        if MainWin.selectBox == "聚合":
            mainlist = {}
            infoBox = func.Tencent(MainWin.entryText).getInfo()
            i = 0
            for key, item in infoBox[0].items():
                if MainWin.entryText in item[0]:
                    mainlist[i] = item
                    i += 1
            Box = {}
            MainWin.infoBox = [mainlist, infoBox[1][0]]

            for key, item in infoBox[0].items():
                info = {}

                if MainWin.entryText not in item[0]:
                    continue

                Box[key] = item

                if item[2] == '2':
                    item[1] += '64位'

                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[0]] = name
                version = QtWidgets.QTableWidgetItem(item[1])
                version.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[1]] = version
                fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3] or 0) / (1024 * 1024))) + "M")
                fileSize.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[3]] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(item[4])
                publishDate.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[4]] = publishDate
                desc = QtWidgets.QTableWidgetItem(item[5])
                desc.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[5]] = desc
                rank = QtWidgets.QTableWidgetItem(str(int(item[6] or 0) / 10) + "分")
                rank.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[item[6]] = rank
                photo = QtGui.QPixmap()
                photo.loadFromData(
                    requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(item[9].lower())).content)
                info['img'] = photo
                dUrl = item[7]
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("腾讯")
                sou.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info['sou'] = sou
                self.signalInfo.emit(info)

            infobox360 = func.QiHu(MainWin.entryText).getInfo()
            for item in infobox360[0].values():
                if MainWin.entryText in item['softname']:
                    mainlist[i] = item
                    i += 1

            MainWin.infoBox = [mainlist, int(infoBox[1][0]) + int(infobox360[1])]
            box360 = {}

            for key, value in infobox360[0].items():
                info = {}

                if MainWin.entryText not in value['softname']:
                    continue

                box360[key] = value

                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['softname']] = name
                version = QtWidgets.QTableWidgetItem(value['version'])
                version.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['version']] = version
                fileSize = QtWidgets.QTableWidgetItem(value['size'])
                fileSize.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['size']] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(value['date'])
                publishDate.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['date']] = publishDate
                desc = QtWidgets.QTableWidgetItem(value['desc'])
                desc.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info[value['desc']] = desc
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "分")
                rank.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
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
                photo.scaled(32, 32, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
                info['img'] = photo
                dUrl = value['soft_download']
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("360")
                sou.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
                info['sou'] = sou
                self.signalInfo.emit(info)
