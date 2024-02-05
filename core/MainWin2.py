# -*- coding: utf-8 -*-
import json
import os
import re

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QApplication, QAction, QDialog

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
        self.label_5.setGeometry(QtCore.QRect(740, 325, 200, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        # self.menu.setObjectName("menu")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "软件下载器"))
        self.pushButton.setText(_translate("MainWindow", "搜索"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "填写查找内容"))
        self.label.setText(_translate("MainWindow", "软件下载器"))
        self.comboBox.setCurrentText(_translate("MainWindow", "腾讯"))
        self.comboBox.setItemText(0, _translate("MainWindow", "腾讯"))
        self.comboBox.setItemText(1, _translate("MainWindow", "360"))
        self.comboBox.setItemText(2, _translate("MainWindow", "聚合"))
        self.label_2.setText(_translate("MainWindow", "软件库："))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "下载路径："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "版本"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "大小"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "发布日期"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "描述"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "评分"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "操作"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "来源"))
        # 每列宽度
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 350)
        self.tableWidget.setColumnWidth(5, 50)
        self.tableWidget.setColumnWidth(6, 60)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "版本"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "大小"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "发布日期"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "描述"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "评分"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "操作"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "链接"))
        # 每列宽度
        self.tableWidget_2.setColumnWidth(0, 275)
        self.tableWidget_2.setColumnWidth(1, 120)
        self.tableWidget_2.setColumnWidth(2, 80)
        self.tableWidget_2.setColumnWidth(3, 100)
        self.tableWidget_2.setColumnWidth(4, 350)
        self.tableWidget_2.setColumnWidth(5, 50)
        self.tableWidget_2.setColumnWidth(6, 60)
        self.tableWidget_2.setColumnWidth(7, 150)
        self.label_4.setText(_translate("MainWindow", "已添加列表"))
        self.pushButton_2.setText(_translate("MainWindow", "清空列表"))
        self.pushButton_3.setText(_translate("MainWindow", "一键下载"))
        self.pushButton_4.setText(_translate("MainWindow", "推荐软件"))
        self.pushButton_5.setText(_translate("MainWindow", "打开下载目录"))
        self.label_5.setText(_translate("MainWindow", "共添加了0个软件"))
        # self.menu.setTitle(_translate("MainWindow", "关于"))
        self.localfile_action = QAction(MainWindow)
        self.localfile_action.setCheckable(False)
        self.localfile_action.setObjectName('aboutAction')
        self.localfile_action.triggered.connect(MainWin.menuButton)
        self.localfile_action.setText('关于')
        self.menubar.addAction(self.localfile_action)
        # self.menu_2.setTitle(_translate("MainWindow", "退出"))


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
        # 默认当前文件夹和选择文件
        application_path = os.path.dirname(__file__)
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        self.lineEdit_2.setText(str(application_path))
        self.toolButton.clicked.connect(self.get_directory)
        # 清空列表
        self.pushButton_2.clicked.connect(self.cleantableWidget_2)
        # 一键下载
        self.pushButton_3.clicked.connect(self.clickButton_3)
        # 推荐软件
        self.pushButton_4.clicked.connect(self.clickButton_4)
        # 打开下载目录
        self.pushButton_5.clicked.connect(self.clickButton_5)
        # 下载对象
        self.downloadThread = None

    def closeEvent(self, event):
        DownloadThread.is_exit = 1
        event.accept()

    # 查询软件相关信息功能返回字典
    def searchAppInfo(self):
        # 获取选择控件文字
        MainWin.selectBox = self.comboBox.currentText()

        # 获取输入搜索关键字
        MainWin.entryText = self.lineEdit.text()
        # 清理所有行
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
        row_count = self.tableWidget.rowCount()  # 返回当前行数(尾部)
        self.tableWidget.insertRow(row_count)  # 尾部插入一行

        # row_count -= 1
        # print(row_count)
        # return
        self.downloadButton = QtWidgets.QPushButton()
        # 设置下载按钮图片
        # self.downloadButton.setIcon(QtGui.QIcon("./src/images/download.png"))
        self.downloadButton.setText("添加")
        font = QFont()
        font.setPointSize(20)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("background-color: #5A9BB3")

        try:
            # 创建窗口对象
            self.headWidget = QtWidgets.QWidget()
            # 创建图像标签对象
            self.imgLabel = QtWidgets.QLabel()
            # 将解析的logo片放入图像标签
            self.imgLabel.setScaledContents(True)
            self.imgLabel.setPixmap(v[6])
            # print(v)
            # 创建文字标签
            self.textLabel = QtWidgets.QLabel()
            # 设置应用名称到文字标签
            self.textLabel.setText(k[0])
            # 创建水平布局，讲窗口对象放进此布局
            self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
            # 将图像标签放入窗口对象所在布局并设置居中
            self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
            # 将文字标签放入窗口对象所在布局
            self.hLayout.addWidget(self.textLabel)
            # 将窗口对象添加到每行第一个单元格
            self.tableWidget.setCellWidget(row_count, 0, self.headWidget)
            # 设置单元格高度
            self.tableWidget.setRowHeight(row_count, 60)
            # print(v[1])
            self.tableWidget.setItem(row_count, 1, v[1])
            self.tableWidget.setItem(row_count, 2, v[2])
            self.tableWidget.setItem(row_count, 3, v[3])
            self.tableWidget.setItem(row_count, 4, v[4])
            self.tableWidget.setItem(row_count, 5, v[5])
            self.tableWidget.setCellWidget(row_count, 6, self.downloadButton)
            # 给下载按钮建立信号槽
            self.downloadButton.clicked.connect(self.addDownloadList)
            self.tableWidget.setItem(row_count, 7, v[8])

        except:
            self.tableWidget.hideRow(MainWin.row)

    def addDownloadList(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请等待全部下载完成后操作')
            msg_box.exec_()
            return
        rowLine = self.tableWidget.currentRow()
        print(rowLine)
        # print(self.tableWidget.item(rowLine, 3).text())

        row_count = self.tableWidget_2.rowCount()  # 返回当前行数(尾部)
        # 判断是否已添加
        for i in range(0, row_count):
            if self.tableWidget.item(rowLine, 4).text() == self.tableWidget_2.item(i, 4).text():
                msg_box = QMessageBox(QMessageBox.Information, '提示', '已添加')
                msg_box.exec_()
                return

        self.tableWidget_2.insertRow(row_count)  # 尾部插入一行
        # print(row_count)

        # print(MainWin.infoBox[0])
        # return
        MainWin.data = {}
        # print(MainWin.infoBox)
        if self.tableWidget.item(rowLine, 7).text() == '腾讯':
            photo = QtGui.QPixmap()
            try:
                photo.loadFromData(
                    requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(
                        MainWin.infoBox[0][rowLine][9].lower())).content)
            except:
                pass
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

        # 创建窗口对象
        self.headWidget = QtWidgets.QWidget()
        # 创建图像标签对象
        self.imgLabel = QtWidgets.QLabel()
        # 将解析的logo片放入图像标签
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setPixmap(MainWin.data['img'])
        # 创建文字标签
        self.textLabel = QtWidgets.QLabel()
        # 设置应用名称到文字标签
        self.textLabel.setText(MainWin.data['name'])
        # 创建水平布局，讲窗口对象放进此布局
        self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
        # 将图像标签放入窗口对象所在布局并设置居中
        self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
        # 将文字标签放入窗口对象所在布局
        self.hLayout.addWidget(self.textLabel)
        # 将窗口对象添加到每行第一个单元格
        self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
        # 设置单元格高度
        self.tableWidget_2.setRowHeight(row_count, 70)

        for i in range(1, 6):
            name = QtWidgets.QTableWidgetItem(self.tableWidget.item(rowLine, i).text())
            name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
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
        name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
        self.tableWidget_2.setItem(row_count, 7, name)
        # 数量
        MainWin.table2num += 1
        self.label_5.setText("共添加了" + str(MainWin.table2num) + "个软件")

    def deleteClicked(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请等待全部下载完成后操作')
            msg_box.exec_()
            return
        button = self.sender()
        if button:
            row = self.tableWidget_2.indexAt(button.pos()).row()
            self.tableWidget_2.removeRow(row)
        MainWin.table2num -= 1
        self.label_5.setText("共添加了" + str(MainWin.table2num) + "个软件")

    def cleantableWidget_2(self):
        if MainWin.downEnd == 1:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请等待全部下载完成后操作')
            msg_box.exec_()
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
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请等待全部下载完成后操作')
            msg_box.exec_()
            return
        self.cleantableWidget_2()
        # 搜索词 ，第几行，什么软件库
        DeRecommendList = [["QQ", 1, "腾讯"],
                           ["微信", 1, "腾讯"],
                           ["钉钉64位", 1, "360"],
                           ["企业微信", 1, "腾讯"],
                           ["火绒", "https://huorong.cn/5.0.version.json", "火绒"],
                           ]

        try:
            application_path = os.path.dirname(__file__)
            if getattr(sys, 'frozen', False):
                application_path = os.path.dirname(sys.executable)
            with open(str(application_path) + "\\推荐列表.ini", "r", encoding='UTF-8') as f:
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
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '无法读取列表将变更为默认')
            msg_box.exec_()

        # print(RecommendList)
        for lis in RecommendList:
            if lis[2] == "腾讯":
                infoBox = func.Tencent(lis[0]).getInfo()
                # print(list(infoBox[0].values())[0])
                item = list(infoBox[0].values())[int(lis[1]) - 1]
                info = {}
                # item[2] == osbit(系统位数)
                # 如果等于2就是64位
                if item[2] == '2':
                    item[1] += '64位'

                # 设置单元格项目并且全部不可点击
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
                rank = QtWidgets.QTableWidgetItem(str(int(item[6] or 0) / 10) + "分")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[6]] = rank
                photo = QtGui.QPixmap()
                photo.loadFromData(
                    requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(item[9].lower())).content)
                info['img'] = photo
                dUrl = item[7]
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("腾讯")
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info['sou'] = sou

                # print(info)
                # 生成一行
                row_count = self.tableWidget_2.rowCount()  # 返回当前行数(尾部)
                self.tableWidget_2.insertRow(row_count)  # 尾部插入一行

                # 创建窗口对象
                self.headWidget = QtWidgets.QWidget()
                # 创建图像标签对象
                self.imgLabel = QtWidgets.QLabel()
                # 将解析的logo片放入图像标签
                self.imgLabel.setScaledContents(True)
                self.imgLabel.setPixmap(info['img'])
                # 创建文字标签
                self.textLabel = QtWidgets.QLabel()
                # 设置应用名称到文字标签
                self.textLabel.setText(item[0])
                # 创建水平布局，讲窗口对象放进此布局
                self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
                # 将图像标签放入窗口对象所在布局并设置居中
                self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
                # 将文字标签放入窗口对象所在布局
                self.hLayout.addWidget(self.textLabel)
                # 将窗口对象添加到每行第一个单元格
                self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
                # 设置单元格高度
                self.tableWidget_2.setRowHeight(row_count, 70)

                for i in range(1, 6):
                    name = QtWidgets.QTableWidgetItem(list(info.values())[i])
                    name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                    self.tableWidget_2.setItem(row_count, i, name)
                self.deleteButton = QtWidgets.QPushButton()
                self.deleteButton.setText("删除")
                font = QFont()
                font.setPointSize(20)
                self.deleteButton.setFont(font)
                self.deleteButton.setStyleSheet("background-color: #e74f4f")
                self.tableWidget_2.setCellWidget(row_count, 6, self.deleteButton)
                self.deleteButton.clicked.connect(self.deleteClicked)

                name = QtWidgets.QTableWidgetItem(info['url'])
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                self.tableWidget_2.setItem(row_count, 7, name)
                # 数量
                MainWin.table2num += 1
                # self.label_5.setText("共添加了" + str(MainWin.table2num) + "个软件")

            elif lis[2] == "360":
                infoBox = func.QiHu(lis[0]).getInfo()
                value = list(infoBox[0].values())[int(lis[1]) - 1]
                info = {}
                # 设置单元格项目并且全部不可点击
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
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "分")
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

                # 生成一行
                row_count = self.tableWidget_2.rowCount()  # 返回当前行数(尾部)
                self.tableWidget_2.insertRow(row_count)  # 尾部插入一行

                # 创建窗口对象
                self.headWidget = QtWidgets.QWidget()
                # 创建图像标签对象
                self.imgLabel = QtWidgets.QLabel()
                # 将解析的logo片放入图像标签
                self.imgLabel.setScaledContents(True)
                self.imgLabel.setPixmap(info['img'])
                # 创建文字标签
                self.textLabel = QtWidgets.QLabel()
                # 设置应用名称到文字标签
                self.textLabel.setText(value['softname'])
                # 创建水平布局，讲窗口对象放进此布局
                self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
                # 将图像标签放入窗口对象所在布局并设置居中
                self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
                # 将文字标签放入窗口对象所在布局
                self.hLayout.addWidget(self.textLabel)
                # 将窗口对象添加到每行第一个单元格
                self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
                # 设置单元格高度
                self.tableWidget_2.setRowHeight(row_count, 70)

                for i in range(1, 6):
                    name = QtWidgets.QTableWidgetItem(list(info.values())[i])
                    name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                    self.tableWidget_2.setItem(row_count, i, name)
                self.deleteButton = QtWidgets.QPushButton()
                self.deleteButton.setText("删除")
                font = QFont()
                font.setPointSize(20)
                self.deleteButton.setFont(font)
                self.deleteButton.setStyleSheet("background-color: #e74f4f")
                self.tableWidget_2.setCellWidget(row_count, 6, self.deleteButton)
                self.deleteButton.clicked.connect(self.deleteClicked)

                name = QtWidgets.QTableWidgetItem(info['url'])
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                self.tableWidget_2.setItem(row_count, 7, name)
                # 数量
                MainWin.table2num += 1
            else:

                # 设置单元格项目并且全部不可点击
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                if "http" in lis[1]:
                    dUrl = lis[1].replace("\"", "")
                else:
                    dUrl = "无效链接"
                if lis[2] == "火绒":
                    res1 = requests.get(lis[1])
                    dUrl = json.loads(res1.text)["urlAll"]
                sou = QtWidgets.QTableWidgetItem(lis[2])
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))

                # print(info)
                # 生成一行
                row_count = self.tableWidget_2.rowCount()  # 返回当前行数(尾部)
                self.tableWidget_2.insertRow(row_count)  # 尾部插入一行

                # 创建窗口对象
                self.headWidget = QtWidgets.QWidget()
                # 创建图像标签对象
                self.imgLabel = QtWidgets.QLabel()
                # 将解析的logo片放入图像标签
                self.imgLabel.setScaledContents(True)
                # self.imgLabel.setPixmap(info['img'])
                # 创建文字标签
                self.textLabel = QtWidgets.QLabel()
                # 设置应用名称到文字标签
                self.textLabel.setText(lis[0])
                # 创建水平布局，讲窗口对象放进此布局
                self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
                # 将图像标签放入窗口对象所在布局并设置居中
                self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
                # 将文字标签放入窗口对象所在布局
                self.hLayout.addWidget(self.textLabel)
                # 将窗口对象添加到每行第一个单元格
                self.tableWidget_2.setCellWidget(row_count, 0, self.headWidget)
                # 设置单元格高度
                self.tableWidget_2.setRowHeight(row_count, 70)

                for i in range(1, 6):
                    name = QtWidgets.QTableWidgetItem("")
                    name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
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
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                self.tableWidget_2.setItem(row_count, 7, name)
                # 数量
                MainWin.table2num += 1

        self.label_5.setText("共添加了" + str(MainWin.table2num) + "个软件")

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
        self.pushButton_4.setText("读取中")
        QApplication.processEvents()
        self.addRecommendList()
        self.pushButton_4.setText("推荐软件")
        self.pushButton_4.setEnabled(True)

    def clickButton_3(self):
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setText("下载中")
        QApplication.processEvents()

        MainWin.line_2 = self.lineEdit_2.text()
        if not self.tableWidget_2.rowCount():
            self.pushButton_3.setText("一键下载")
            self.pushButton_3.setEnabled(True)
            return
        # 清除已下载
        # print(self.tableWidget_2.rowCount())
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
        # QApplication.processEvents()
        self.downloadThread = DownloadThread()
        self.downloadThread.signal.connect(self.flushValue)
        self.downloadThread.start()

    def flushValue(self, value):
        # print(value)

        if value[0] == -1:
            self.label_5.setText("共添加" + str(MainWin.table2num) + "个软件" + "已完成" + str(MainWin.table2num) + "个")
            print('done')
            row_count = self.tableWidget_2.rowCount()
            print(row_count)
            self.tableWidget_2.item(row_count - 1, 4).setText("下载完成")
            self.downloadThread.exit(0)
            MainWin.is_done = 0
            MainWin.downNum = 0
            self.pushButton_3.setText("一键下载")
            self.pushButton_3.setEnabled(True)
            QMessageBox.information(self, "通知", "全部下载完毕", QMessageBox.Yes, QMessageBox.Yes)
            return

        if value[1] == -1:
            self.tableWidget_2.item(value[0], 4).setText("下载完成")
            MainWin.downNum += 1
        else:
            # print(str(value[1]))
            self.tableWidget_2.item(value[0], 4).setText(str(value[1]) + '%')
        self.label_5.setText("共添加" + str(MainWin.table2num) + "个软件" + "已完成" + str(MainWin.downNum) + "个")


class DownloadThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)
    Drow = -1
    Durl = ""
    is_exit = 0
    pool = ThreadPoolExecutor(max_workers=10)

    def run(self):
        data = MainWin.table2list
        MainWin.downEnd = 1
        DownloadThread.num = len(data)
        list = []
        for row, url in enumerate(data):
            list.append([row, url])
        all_task = [self.pool.submit(self.doDownload, i) for i in list]
        wait(all_task, timeout=None, return_when=ALL_COMPLETED)
        print("----complete-----")
        self.pool.shutdown()

        self.signal.emit([-1, 1])
        MainWin.table2list = []
        MainWin.downEnd = 0

    # def handle_exit(self):
    #     print("用户退出结束所有进程")
    #     self.pool.shutdown()
    #     self.exit(0)

    def doDownload(self, val):
        url = val[1]
        row = val[0]
        try:
            res = requests.get(url, stream=True)

            # 获取文件大小
            fileSize = res.headers['Content-Length']
            chunk_size = 102400
            chunk_temp = 0
            name = url.split('/')[-1]
            # print(MainWin.line_2 + "\\" + name)
            with open(MainWin.line_2 + "\\" + name, 'wb') as f:
                for chunk in res.iter_content(chunk_size=chunk_size):
                    if DownloadThread.is_exit == 1:
                        return
                    if chunk:
                        temp = "%.2f" % (chunk_temp / float(fileSize) * 100)
                        f.write(chunk)
                    chunk_temp += chunk_size
                    # print([row, temp])
                    # DownloadThread.flushValue(DownloadThread(),[row, temp])
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
            # 得到处理后的信息字典
            MainWin.infoBox = func.Tencent(MainWin.entryText).getInfo()

            # 创建表格控件中的行数
            # infoBox[1][0] = 查询到的软件总数
            self.signalTotal.emit(MainWin.infoBox[1][0])
            # 遍历查询到的软件信息
            # print(MainWin.infoBox[0].items())
            for key, item in MainWin.infoBox[0].items():
                info = {}
                # item[2] == osbit(系统位数)
                # 如果等于2就是64位
                if item[2] == '2':
                    item[1] += '64位'

                # 设置单元格项目并且全部不可点击
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
                # print(item)
                rank = QtWidgets.QTableWidgetItem(str(int(item[6] or 0) / 10) + "分")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
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
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info['sou'] = sou
                # print(info)
                self.signalInfo.emit(info)
            time.sleep(1)
            MainWin.row = -1
            self._signalIsRunning.emit()
        if MainWin.selectBox == "360":
            # 得到处理后的信息字典
            MainWin.infoBox = func.QiHu(MainWin.entryText).getInfo()
            self.signalTotal.emit(str(MainWin.infoBox[1]))
            for value in MainWin.infoBox[0].values():
                info = {}
                # 设置单元格项目并且全部不可点击
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
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "分")
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

        if MainWin.selectBox == "聚合":
            # 得到处理后的信息字典
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
            # 创建表格控件中的行数
            # infoBox[1][0] = 查询到的软件总数
            # self.signalTotal.emit(MainWin.infoBox[1][0])
            # 遍历查询到的软件信息
            # print(MainWin.infoBox[0].items())
            for key, item in infoBox[0].items():
                info = {}

                # 跳过不匹配
                if MainWin.entryText not in item[0]:
                    print("skip")
                    continue

                Box[key] = item
                # item[2] == osbit(系统位数)
                # 如果等于2就是64位
                if item[2] == '2':
                    item[1] += '64位'

                # 设置单元格项目并且全部不可点击
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
                rank = QtWidgets.QTableWidgetItem(str(int(item[6] or 0) / 10) + "分")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[6]] = rank
                photo = QtGui.QPixmap()
                photo.loadFromData(
                    requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(item[9].lower())).content)
                info['img'] = photo
                dUrl = item[7]
                info['url'] = dUrl
                sou = QtWidgets.QTableWidgetItem("腾讯")
                sou.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info['sou'] = sou
                # print(info)
                self.signalInfo.emit(info)

            # time.sleep(1)
            # MainWin.row = -1

            # 得到处理后的信息字典
            infobox360 = func.QiHu(MainWin.entryText).getInfo()
            for item in infobox360[0].values():
                if MainWin.entryText in item['softname']:
                    mainlist[i] = item
                    i += 1

            MainWin.infoBox = [mainlist, int(infoBox[1][0]) + int(infobox360[1])]
            print(MainWin.infoBox)
            box360 = {}
            # self.signalTotal.emit(str(infobox360[1]))
            # print(infobox360[0].values())
            for key, value in infobox360[0].items():
                info = {}

                # 跳过不匹配
                if MainWin.entryText not in value['softname']:
                    print("skip360")
                    continue

                box360[key] = value
                # 设置单元格项目并且全部不可点击
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
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "分")
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
