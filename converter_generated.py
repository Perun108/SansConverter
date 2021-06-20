# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SansConverter(object):

    def setupUi(self, SansConverter):
        SansConverter.setObjectName("SansConverter")
        SansConverter.resize(620, 550)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            SansConverter.sizePolicy().hasHeightForWidth())
        SansConverter.setSizePolicy(sizePolicy)
        SansConverter.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "/home/Dropbox/Python_Converter/FINAL/icons8-om-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SansConverter.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SansConverter)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 3, 9, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(100, 16))
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 4, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 9, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 9, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 7, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 11, 9, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 6, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(100, 16))
        self.textBrowser.setTabChangesFocus(True)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setReadOnly(True)
        self.gridLayout_2.addWidget(self.textBrowser, 11, 0, 1, 1)
        SansConverter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SansConverter)
        self.statusbar.setObjectName("statusbar")
        SansConverter.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(SansConverter)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 815, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menuHelp.setObjectName("menuHelp")
        self.menuQuit = QtWidgets.QMenu(self.menuBar)
        self.menuQuit.setObjectName("menuQuit")
        SansConverter.setMenuBar(self.menuBar)
        self.actionUndo = QtWidgets.QAction(SansConverter)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(SansConverter)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(SansConverter)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(SansConverter)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSwap = QtWidgets.QAction(SansConverter)
        self.actionSwap.setObjectName("actionSwap")
        self.actionClear = QtWidgets.QAction(SansConverter)
        self.actionClear.setObjectName("actionClear")
        self.actionQuit = QtWidgets.QAction(SansConverter)
        self.actionQuit.setObjectName("actionQuit")
        self.actionTransliteration_help = QtWidgets.QAction(SansConverter)
        self.actionTransliteration_help.setObjectName(
            "actionTransliteration_help")
        self.actionAbout_SansConverter = QtWidgets.QAction(SansConverter)
        self.actionAbout_SansConverter.setObjectName(
            "actionAbout_SansConverter")
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionClear)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSwap)
        self.menuEdit.addSeparator()
        self.menuHelp.addAction(self.actionTransliteration_help)
        self.menuHelp.addAction(self.actionAbout_SansConverter)
        self.menuQuit.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuQuit.menuAction())
        # Linking buttons, hotkeys and menus to functions
        self.actionClear.setShortcut("Ctrl+R")
        self.actionCopy.setShortcut("Ctrl+C")
        self.actionPaste.setShortcut("Ctrl+V")
        self.actionRedo.setShortcut("Ctrl+Y")
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionSwap.setShortcut("Alt+S")
        self.retranslateUi(SansConverter)
        QtCore.QMetaObject.connectSlotsByName(SansConverter)
        # Tabbing order of buttons and other widgets
        SansConverter.setTabOrder(self.textEdit, self.comboBox)
        SansConverter.setTabOrder(self.comboBox, self.pushButton_3)
        SansConverter.setTabOrder(self.pushButton_3, self.pushButton_4)
        SansConverter.setTabOrder(self.pushButton_4, self.checkBox)
        SansConverter.setTabOrder(self.checkBox, self.pushButton_2)
        SansConverter.setTabOrder(self.pushButton_2, self.comboBox_2)
        SansConverter.setTabOrder(self.comboBox_2, self.pushButton)
        SansConverter.setTabOrder(self.pushButton, self.textBrowser)

    def retranslateUi(self, SansConverter):
        _translate = QtCore.QCoreApplication.translate
        SansConverter.setWindowTitle(_translate(
            "SansConverter", "SansConverter (v1.6)"))
        SansConverter.setStatusTip(_translate(
            "SansConverter", "Welcome to SansConverter"))
        self.pushButton.setText(_translate("SansConverter", "Copy text"))
        self.pushButton.setStatusTip(_translate(
            "SansConverter", "Copy converted text (Ctrl+C)"))
        self.pushButton.setToolTip(_translate(
            "SansConverter", "Copy converted text (Ctrl+C)"))
        self.pushButton_2.setText(_translate(
            "SansConverter", "Swap transliterations and texts"))
        self.pushButton_2.setStatusTip(_translate(
            "SansConverter", "Swap transliterations and texts (Alt+S)"))
        self.pushButton_3.setText(_translate("SansConverter", "Clear"))
        self.pushButton_3.setStatusTip(_translate(
            "SansConverter", "Clear input window (Ctrl+R)"))
        self.pushButton_3.setToolTip(_translate(
            "SansConverter", "Clear input window (Ctrl+R)"))
        self.pushButton_4.setText(_translate(
            "SansConverter", "Paste from clipboard"))
        self.pushButton_4.setStatusTip(_translate(
            "SansConverter", "Paste text to convert (Ctrl+V)"))
        self.pushButton_4.setToolTip(_translate(
            "SansConverter", "Paste text to convert (Ctrl+V)"))
        self.checkBox.setText(_translate("SansConverter", "Use \"ṃ\""))
        self.checkBox.setStatusTip(_translate(
            "SansConverter", "Select anusvara (\"ṃ\" or \"ṁ\")"))
        self.checkBox.setToolTip(_translate(
            "SansConverter", "Select anusvara (\"ṃ\" or \"ṁ\")"))
        self.comboBox.setItemText(0, _translate("SansConverter", "Balaram"))
        self.comboBox.setItemText(1, _translate("SansConverter", "Velthius"))
        self.comboBox.setItemText(2, _translate("SansConverter", "HK"))
        self.comboBox.setItemText(3, _translate("SansConverter", "IAST"))
        self.comboBox.setItemText(4, _translate(
            "SansConverter", "Cyrillic (Russian)"))
        self.comboBox.setItemText(5, _translate(
            "SansConverter", "Cyrillic (Ukrainian)"))
        self.comboBox.setStatusTip(_translate(
            "SansConverter", "Select input transliteration. For more info see \"Help\"→\"Transliteration help\""))
        self.comboBox_2.setItemText(0, _translate("SansConverter", "IAST"))
        self.comboBox_2.setItemText(1, _translate(
            "SansConverter", "Cyrillic (Russian)"))
        self.comboBox_2.setItemText(2, _translate(
            "SansConverter", "Cyrillic (Ukrainian)"))
        self.comboBox_2.setItemText(3, _translate("SansConverter", "Balaram"))
        self.comboBox_2.setItemText(4, _translate("SansConverter", "HK"))
        self.comboBox_2.setItemText(5, _translate("SansConverter", "Velthius"))
        self.comboBox_2.setStatusTip(_translate(
            "SansConverter", "Select input transliteration. For more info see \"Help\"→\"Transliteration help\""))
        self.menuEdit.setTitle(_translate("SansConverter", "&Edit"))
        self.menuEdit.setStatusTip(_translate("SansConverter", "Edit"))
        self.menuHelp.setTitle(_translate("SansConverter", "&Help"))
        self.menuHelp.setStatusTip(_translate("SansConverter", "&Help"))
        self.menuQuit.setTitle(_translate("SansConverter", "&Quit"))
        self.menuQuit.setStatusTip(_translate("SansConverter", "Quit"))
        self.actionUndo.setText(_translate("SansConverter", "&Undo"))
        self.actionUndo.setStatusTip(
            _translate("SansConverter", "Undo Ctrl+Z"))
        self.actionRedo.setText(_translate("SansConverter", "&Redo"))
        self.actionRedo.setStatusTip(
            _translate("SansConverter", "Redo Ctrl+Y"))
        self.actionCopy.setText(_translate("SansConverter", "&Copy converted"))
        self.actionCopy.setStatusTip(_translate(
            "SansConverter", "Copy converted Ctrl+C"))
        self.actionPaste.setText(_translate("SansConverter", "&Paste"))
        self.actionPaste.setStatusTip(
            _translate("SansConverter", "Paste Ctrl+V"))
        self.actionSwap.setText(_translate(
            "SansConverter", "&Swap transliterations and texts"))
        self.actionSwap.setStatusTip(_translate(
            "SansConverter", "Swap transliterations and texts Alt+S"))
        self.actionClear.setText(_translate("SansConverter", "&Clear"))
        self.actionClear.setStatusTip(
            _translate("SansConverter", "Clear Ctrl+R"))
        self.actionQuit.setText(_translate("SansConverter", "&Quit"))
        self.actionQuit.setStatusTip(_translate(
            "SansConverter", "Quit SansConverter Ctrl+Q"))
        self.actionTransliteration_help.setText(
            _translate("SansConverter", "&Transliteration help"))
        self.actionTransliteration_help.setStatusTip(_translate(
            "SansConverter", "Show transliteration systems help"))
        self.actionAbout_SansConverter.setText(
            _translate("SansConverter", "&About SansConverter"))
        self.actionAbout_SansConverter.setStatusTip(
            _translate("SansConverter", "About SansConverter"))
