from collections import OrderedDict

from pkg_resources import fixup_namespace_packages
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QTextCursor, QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat 
from PIL import Image
import numpy as np
from gui_import.codeeditor import CodeEditor
import json
import os
import subprocess
import copy
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filePathText = QtWidgets.QLineEdit(self.centralwidget)
        self.filePathText.setReadOnly(True)
        self.filePathText.setObjectName("filePathText")
        self.horizontalLayout.addWidget(self.filePathText)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setObjectName("browse")
        self.horizontalLayout.addWidget(self.browse)
        self.runFile = QtWidgets.QPushButton(self.centralwidget)
        self.runFile.setObjectName("runFile")
        self.horizontalLayout.addWidget(self.runFile)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.issue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.issue.setFont(font)
        self.issue.setObjectName("issue")
        self.horizontalLayout_2.addWidget(self.issue)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.atomic = QtWidgets.QCheckBox(self.centralwidget)
        self.atomic.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.atomic.setObjectName("atomic")
        self.horizontalLayout_2.addWidget(self.atomic)
        self.readOnly = QtWidgets.QCheckBox(self.centralwidget)
        self.readOnly.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.readOnly.setObjectName("readOnly")
        self.horizontalLayout_2.addWidget(self.readOnly)
        self.interruptDisabled = QtWidgets.QCheckBox(self.centralwidget)
        self.interruptDisabled.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.interruptDisabled.setObjectName("interruptDisabled")
        self.horizontalLayout_2.addWidget(self.interruptDisabled)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.byteCode = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.byteCode.setFont(font)
        self.byteCode.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.byteCode.setObjectName("byteCode")
        self.horizontalLayout_3.addWidget(self.byteCode)
        self.sourceCode = CodeEditor(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.sourceCode.setFont(font)
        self.sourceCode.setPlainText("")
        self.sourceCode.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.sourceCode.setObjectName("sourceCode")
        self.horizontalLayout_3.addWidget(self.sourceCode)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.microstepExplain = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.microstepExplain.setFont(font)
        self.microstepExplain.setReadOnly(True)
        self.microstepExplain.setObjectName("microstepExplain")
        self.verticalLayout_2.addWidget(self.microstepExplain)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.microstepsLabel = QtWidgets.QLabel(self.centralwidget)
        self.microstepsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.microstepsLabel.setText("")
        self.microstepsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.microstepsLabel.setObjectName("microstepsLabel")
        self.verticalLayout_3.addWidget(self.microstepsLabel)
        self.sharedVariables = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.sharedVariables.setFont(font)
        self.sharedVariables.setObjectName("sharedVariables")
        self.verticalLayout_3.addWidget(self.sharedVariables)
        self.localVariables = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.localVariables.setFont(font)
        self.localVariables.setObjectName("localVariables")
        self.verticalLayout_3.addWidget(self.localVariables)
        self.stackTop = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.stackTop.setFont(font)
        self.stackTop.setObjectName("stackTop")
        self.verticalLayout_3.addWidget(self.stackTop)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.singleStep = QtWidgets.QCheckBox(self.centralwidget)
        self.singleStep.setObjectName("singleStep")
        self.horizontalLayout_4.addWidget(self.singleStep)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.up = QtWidgets.QPushButton(self.centralwidget)
        self.up.setMinimumSize(QtCore.QSize(65, 0))
        self.up.setObjectName("up")
        self.horizontalLayout_6.addWidget(self.up)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setObjectName("prev")
        self.horizontalLayout_5.addWidget(self.prev)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setObjectName("next")
        self.horizontalLayout_5.addWidget(self.next)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.down = QtWidgets.QPushButton(self.centralwidget)
        self.down.setObjectName("down")
        self.horizontalLayout_7.addWidget(self.down)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_9.setStretch(0, 5)
        self.horizontalLayout_9.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.threadOffsetLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.threadOffsetLabel.setFont(font)
        self.threadOffsetLabel.setText("")
        self.threadOffsetLabel.setObjectName("threadOffsetLabel")
        self.horizontalLayout_8.addWidget(self.threadOffsetLabel)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(605, 0))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(605, 16777215))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_8.addWidget(self.horizontalSlider)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.threadBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.threadBrowser.setMinimumSize(QtCore.QSize(670, 0))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.threadBrowser.setFont(font)
        self.threadBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.threadBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.threadBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.threadBrowser.setObjectName("threadBrowser")
        self.verticalLayout.addWidget(self.threadBrowser)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(4, 1)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuConfiguration = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConstants = QtWidgets.QAction(MainWindow)
        self.actionConstants.setObjectName("actionConstants")
        self.actionModules = QtWidgets.QAction(MainWindow)
        self.actionModules.setObjectName("actionModules")
        self.menuConfiguration.addAction(self.actionConstants)
        self.menuConfiguration.addAction(self.actionModules)
        self.menubar.addAction(self.menuConfiguration.menuAction())

        self.browse.clicked.connect(lambda: self.browseFiles(False, ""))
        self.next.clicked.connect(self.nextMicrostep)
        self.prev.clicked.connect(self.prevMicroStep)
        self.up.clicked.connect(self.upMicroStep)
        self.down.clicked.connect(self.downMicroStep)
        self.runFile.clicked.connect(self.runSource)

        self.actionConstants.triggered.connect(self.constantWindow)
        self.actionModules.triggered.connect(self.moduleWindow)

        # load keywords dictionary from gui_import/keywords.json
        self.keywords = json.load(open("gui_import/keywords.json"))
        # load identifier of all modules from gui_import/modules.json
        self.moduleIdentifiers = json.load(open("gui_import/modules.json"))

        self.horizontalSlider.valueChanged.connect(self.sliderMoveUpdate)
        # self.open.clicked.connect(self.openFileByTypedPath)
        # self.save.clicked.connect(self.save_file)

        self.sourceCodeCursor = self.sourceCode.textCursor()
        self.byteCodeCursor = self.byteCode.textCursor()
        self.hco = {}
        self.hvm = {}
        self.microSteps = []
        self.microStepPointer = -1
        self.sourceFile = "" # filepath of the sourcefile
        # 12 different thread active colors
        self.threadActiveColors = [[255, 0, 0], [0, 255, 0], [0, 255, 255], [255, 128, 0], [0, 128, 255], [255, 0, 127], [0, 0, 255], [255, 0, 255], [127, 0, 255], [255, 255, 0]]
        self.threadInactiveColor = [192, 192, 192] # set thread inactive color to be gray
        self.threadNumber = -1
        self.threadColor = []
        # self.stackTraceList is a list of string with length <number of threads>. Each entry is the stack trace for each thread
        self.stackTraceList = []
        # self.stackTraceTextList contains stack trace to display at each microstep
        self.stackTraceTextList = []
        # self.checkBoxList contains checkbox to display at each microstep
        self.checkBoxList = []
        # self.stackTopDisplay is a list of stack top at each microstep
        # self.stackTopDisplay[i] is a list of variables that are on stack top at microstep i
        self.stackTopDisplay = []
        # self.threadMode is a list of thread modes at each microstep
        self.threadMode = []
        # self.stmtIndicator is a list of True/False value, where True indicates next microstep is in the same line, False not
        self.stmtIndicator = []
        # self.defaultFpath is the command line argument
        self.defaultFilePath = ""

        self.constantDic = OrderedDict()
        self.moduleDic = OrderedDict()

        # source file path to compile
        self.runName = ""


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Harmony"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.runFile.setText(_translate("MainWindow", "Run"))
        self.issue.setText(_translate("MainWindow", "Issue: "))
        self.atomic.setText(_translate("MainWindow", "Atomic"))
        self.readOnly.setText(_translate("MainWindow", "Read-only"))
        self.interruptDisabled.setText(_translate("MainWindow", "Interrupt-disabled"))
        self.sharedVariables.headerItem().setText(0, _translate("MainWindow", "Shared Variables"))
        self.localVariables.headerItem().setText(0, _translate("MainWindow", "Local Variables"))
        self.stackTop.headerItem().setText(0, _translate("MainWindow", "Stack Top"))
        self.singleStep.setText(_translate("MainWindow", "Single Step"))
        self.up.setText(_translate("MainWindow", "Up"))
        self.up.setShortcut(_translate("MainWindow", "Up"))
        self.prev.setText(_translate("MainWindow", "< Prev"))
        self.prev.setShortcut(_translate("MainWindow", "Left"))
        self.next.setText(_translate("MainWindow", "Next >"))
        self.next.setShortcut(_translate("MainWindow", "Right"))
        self.down.setText(_translate("MainWindow", "Down"))
        self.down.setShortcut(_translate("MainWindow", "Down"))
        self.threadOffsetLabel.setText(_translate("MainWindow", "    "))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.actionConstants.setText(_translate("MainWindow", "Constants"))
        self.actionModules.setText(_translate("MainWindow", "Modules"))


    def openFile(self, editor, file, microStepPointer):
        text = open(file).read()
        # reset sourceCodeCursor's position before and after
        # self.insertFormatSourceCode to maintain invariant
        assert editor == self.sourceCode
        self.sourceCodeCursor.movePosition(QTextCursor.Start, QtGui.QTextCursor.MoveAnchor)
        assert self.sourceCodeCursor.position() == 0
        assert self.sourceCodeCursor.anchor() == 0
        editor.clear()

        self.insertFormatSourceCode(text, microStepPointer)

        self.sourceCodeCursor.clearSelection()
        self.sourceCodeCursor.movePosition(QTextCursor.Start, QtGui.QTextCursor.MoveAnchor)
        
    def insertFormatSourceCode(self, text, microStepPointer):
        """
        Insert text into self.sourceCode with syntactic highlighting.
        text is the sourceCode string. 
        """
        fmt = QtGui.QTextCharFormat()
        left = 0

        # set identifier dictionary for 3 different cases: (1) source file, 
        # (2) library file, (3) self-defined import
        pc = int(self.microSteps[microStepPointer]["pc"])
        fileName = self.hco['locations'][str(pc)]['file']
        sourceFileName = self.hco["locations"]["0"]["file"]
        fileNameLst = fileName.split('/')
        # case 1: source file
        if fileName == sourceFileName: 
            identifierDic = self.hvm['modules']['__main__']['identifiers']
        # case 2: import modules
        else: 
            # fix bug, find by file path, not module name
            for moduleName in self.hvm['modules']:
                if self.hvm['modules'][moduleName]['file'] == fileName:
                    identifierDic = self.hvm['modules'][moduleName]['identifiers']
                    break
            

        # insertText = "" # for checking purpose

        # parse text into words
        while left < len(text):
            # no word matched
            if not text[left].isalpha():
                # insert text[left]
                # insertText += text[left]
                self.sourceCodeCursor.insertText(text[left])
                left += 1
                continue
            # try to match a word
            right = left
            while right < len(text) and text[right].isalpha():
                right += 1
            # insert word = text[left:right]
            # insertText += text[left:right]
            word = text[left:right]

            # differenct cases for formatting word
            # word is in keywords
            if word in self.keywords:
                # bold
                fmt.setFontWeight(QtGui.QFont.Bold)
                self.sourceCodeCursor.mergeCharFormat(fmt)
                self.sourceCodeCursor.insertText(text[left:right])
                fmt.setFontWeight(QtGui.QFont.Normal)
                self.sourceCodeCursor.mergeCharFormat(fmt)
            # special case: word == "result" -> italicize
            elif word == "result":
                # italics
                fmt.setFontItalic(True)
                self.sourceCodeCursor.mergeCharFormat(fmt)
                self.sourceCodeCursor.insertText(text[left:right])
                fmt.setFontItalic(False)
                self.sourceCodeCursor.mergeCharFormat(fmt)
            # word is in identifiers
            elif word in identifierDic:
                if identifierDic[word] == "module":
                    # roman
                    fmt.setFontStyleHint(QtGui.QFont.Times)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                    self.sourceCodeCursor.insertText(text[left:right])
                    fmt.setFontStyleHint(QtGui.QFont.AnyStyle)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                elif identifierDic[word] == "local-const":
                    # italics
                    fmt.setFontItalic(True)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                    self.sourceCodeCursor.insertText(text[left:right])
                    fmt.setFontItalic(False)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                elif identifierDic[word] == "local-var":
                    # italics
                    fmt.setFontItalic(True)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                    self.sourceCodeCursor.insertText(text[left:right])
                    fmt.setFontItalic(False)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                elif identifierDic[word] == "global":
                    # roman
                    fmt.setFontItalic(True)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                    self.sourceCodeCursor.insertText(text[left:right])
                    fmt.setFontItalic(False)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                elif identifierDic[word] == "constant":
                    # roman
                    fmt.setFontStyleHint(QtGui.QFont.Times)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                    self.sourceCodeCursor.insertText(text[left:right])
                    fmt.setFontStyleHint(QtGui.QFont.AnyStyle)
                    self.sourceCodeCursor.mergeCharFormat(fmt)
                else:
                    self.sourceCodeCursor.insertText(text[left:right])
            else:
                self.sourceCodeCursor.insertText(text[left:right])
            # special case "result" in italics

            # print(text[left:right]) -- highight candidate
            left = right
        # assert insertText == text

    def const_flag(self):
        lst = []
        for k in self.constantDic:
            lst.append("-c")
            lst.append(f"{k}={self.constantDic[k]}")
        return lst
    
    def module_flag(self):
        lst = []
        for k in self.moduleDic:
            lst.append("-m")
            lst.append(f"{k}={self.moduleDic[k]}")
        return lst

    def browseFiles(self, defaultBool, defaultFilePath):
        # if defaultBool is True, defaultFilePath is the file path of commandline argument
        if defaultBool:
            # no commandline argument
            if len(defaultFilePath) == 0:
                return
            # there is a commandline argument
            else:
                fname = defaultFilePath
        # otherwise, just do browse file
        else:
            fname = QFileDialog.getOpenFileName(None, "Title", "..", "Harmony file (*.hny *.hco)")[0]
        if(fname == ""):
            return
        

        # initialize microstep pointer to 0
        self.microStepPointer = 0
        self.horizontalSlider.setValue(0)
        self.filePathText.setText(fname)
        # try open source code file
        # try:
        # self.openFile(self.sourceCode, fname)
            # self.fileNameLabel.setText(fname)
        # except:
        #     print("!")
        #     self.filePathText.setText("")
        #     self.errorMsgBox("This file cannot be opened. Please open another file.")
        #     return
        if fname[-3:] == "hny":
            sourceText = open(fname).read()
            self.clearFormat(self.sourceCodeCursor)
            self.sourceCode.clear()
            self.sourceCode.setPlainText(sourceText)
            self.runName = fname
            # clear all states
            self.byteCode.setPlainText("")
            self.threadBrowser.setText("")
            self.microstepExplain.setPlainText("")
            self.sharedVariables.clear()
            self.localVariables.clear()
            self.stackTop.clear()
            self.issue.setText("Issue: ")
            return
        else:
            # .hco file
            self.runName = ""
            self.compileAndDisplay(fname)

    def compileAndDisplay(self, fname):
        if fname[-3:] == "hny": 
            # try compile hny file
            runcmd = subprocess.run(["./harmony", "--noweb"] + self.const_flag() + self.module_flag() + [fname], capture_output=True)
            returncode = runcmd.returncode
            stdout =  runcmd.stdout.decode()
            stderr =  runcmd.stderr.decode()
            # .hny file fail to compile
            if returncode != 0:
                self.errorMsgBox("Run Failed\n" + stdout + stderr)
                return
        else:
            assert fname[-3:] == "hco"
            fname = fname[:-3] + "hny"
        
        # try open hco file
        try:
            hcoName = fname[:-3] + "hco"
            hcoFile = open(hcoName)
            hcoData = json.load(hcoFile)
        except:
            self.filePathText.setText("")
            self.errorMsgBox("Cannot open hco file. ")
            return
        # try open hvm file
        try: 
            hvmName = fname[:-3] + "hvm"
            hvmFile = open(hvmName)
            hvmData = json.load(hvmFile)
        except:
            self.filePathText.setText("")
            self.errorMsgBox("Cannot open hvm file. ")
            return
        
        # set self.hco and self.hvm
        self.hco = hcoData
        self.hvm = hvmData
        # print(self.hvm['identifiers'])
        # if there are no issues
        if "macrosteps" not in self.hco:
            assert self.hco['issue'] == 'No issues'
            self.filePathText.setText("")
            # clear all states
            self.byteCode.setPlainText("")
            self.threadBrowser.setText("")
            self.microstepExplain.setPlainText("")
            self.sharedVariables.clear()
            self.localVariables.clear()
            self.stackTop.clear()
            self.issue.setText("Issue: No issues")

            msg = QMessageBox()
            msg.setText("There are no issues in the program.")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            # self.filePathText.setText("")
            # self.sourceCode.setPlainText("")
            # self.issue.setText("Issue: ")
            return
        # construct self.microSteps to be a list of microsteps
        self.constructMicrosteps()
        # construct self.threadMode
        self.constructThreadMode()
        # construct self.stackTraceText to be stack trace to display at each microstep
        self.constructStackTraceTextList()
        # construct self.stackTopDisplay
        self.constructStackTopDisplay()
        # construct stmt indicator
        self.constructSTMT()

        # initialize bytecode display, <adding pc value before each line>
        text = ""
        pcMAX = len(self.hco["code"]) - 1
        offsetDigit = len(str(pcMAX))
        for i in range(len(self.microSteps)):
            pc = int(self.microSteps[i]["pc"])
            spaceOffset = ""
            for j in range(offsetDigit - len(str(pc))):
                spaceOffset = spaceOffset + " "
            microstepLine = spaceOffset + str(pc) + " " + self.hco["code"][int(self.microSteps[i]["pc"])]
            text += (microstepLine + "\n")
        self.byteCode.setPlainText(text)
        # initialize microstep pointer to 0
        self.microStepPointer = 0
        # initialize slider parameters
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(len(self.microSteps))
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        # initalize cursor
        # self.sourceCodeCursor = self.sourceCode.textCursor()
        self.byteCodeCursor = self.byteCode.textCursor()
        # update the highlight part
        self.sourceFile = fname
        self.highlightUpdate(self.microStepPointer)
        # initialize thread images
        self.createThreadImg()
        # display thread browser
        self.threadBrowserUpdate(self.microStepPointer)
        # update shared variable
        self.sharedVariableUpdate(self.microStepPointer)
        # update local variable
        self.localVariableUpdate(self.microStepPointer)
        # update stack top
        self.stackTopUpdate(self.microStepPointer)
        # display issue
        self.displayIssue()
        # update checkbox
        self.updateCheckBox(self.microStepPointer)
        # print(self.hco["code"][49])
    
    def runSource(self):
        if len(self.runName) > 3 and self.runName[-3:] == "hny":
            self.compileAndDisplay(self.runName)
    

    def constructMicrosteps(self):
        self.microSteps = []
        # initialize self.threadNumber to be number of threads
        self.threadNumber = len(self.hco['macrosteps'][-1]['contexts']) # fix bug - change 0 to -1
        # initialize self.threadColor index of colors
        self.threadColor = np.random.permutation(self.threadNumber).tolist()
        # initialize self.microSteps
        for macroStep in self.hco['macrosteps']:
            for microStep in macroStep['microsteps']:
                cpMicroStep = dict(microStep)
                cpMicroStep['tid'] = macroStep['tid']
                cpMicroStep['name'] = macroStep['name']
                cpMicroStep['invfails'] = macroStep['invfails']
                cpMicroStep['contexts'] = macroStep['contexts']
                cpMicroStep['context'] = macroStep['context']
                self.microSteps.append(cpMicroStep)
        # initialize self.stackTraceList
        self.stackTraceList = []
        self.stackTraceTextList = []
        for i in range(self.threadNumber):
            self.stackTraceList.append("")
        # initialize 
        for i in range(len(self.microSteps)):
            self.stackTraceTextList.append("")
        # initialize self.checkBoxList
        for i in range(len(self.microSteps)):
            self.checkBoxList.append([])
            for j in range(self.threadNumber):
                self.checkBoxList[i].append({"atomic": False, "readonly": False, "interrupt-disabled": False})
        # construct self.checkBoxList
        self.constructCheckBox()

    def constructSTMT(self):
        # construct self.stmtIndicator
        # self.stmtIndicator is a list of True/False value
        # True means current microstep and next microstep are in the same statement, False otherwise
        self.stmtIndicator = []
        for i in range(len(self.microSteps) - 1):
            pc = int(self.microSteps[i]["pc"])
            nextMicroStepPc = int(self.microSteps[i + 1]["pc"])
            # compare file name
            if self.hco['locations'][str(pc)]['file'] != self.hco['locations'][str(nextMicroStepPc)]['file']:
                self.stmtIndicator.append(False)
            # compare thread id
            elif int(self.microSteps[i]['tid']) != int(self.microSteps[i + 1]['tid']):
                self.stmtIndicator.append(False)
            # compare line 
            elif self.hco['locations'][str(pc)]['stmt'][0] != self.hco['locations'][str(nextMicroStepPc)]['stmt'][0]:
                self.stmtIndicator.append(False)
            # all three checks passes
            else:
                self.stmtIndicator.append(True)
        # add an extra False for the last microstep
        self.stmtIndicator.append(False)
        # add an extra False for the extra microstep for final state
        self.stmtIndicator.append(False)
        assert len(self.stmtIndicator) == len(self.microSteps) + 1

    def highlightUpdate(self, microStepPointer):
        # update microsteps label
        self.microstepsLabel.setText(f"Microsteps: {microStepPointer}/{len(self.microSteps)}")
        # update horizontal slider
        self.horizontalSlider.setValue(microStepPointer)
        if microStepPointer == len(self.microSteps):
            microStepPointer -= 1
        # update highlight part
        pc = int(self.microSteps[microStepPointer]["pc"])
        # update microstepExplain label
        explanation = self.microSteps[microStepPointer]['explain']
        threadId = int(self.microSteps[microStepPointer]['tid'])
        assert int(self.microSteps[microStepPointer]['contexts'][threadId]['tid']) == threadId
        threadName = self.microSteps[microStepPointer]['contexts'][threadId]['name']
        fileName = self.hco['locations'][str(pc)]['file']
        explanationText = f"T{threadId} {threadName}: {explanation}\n{fileName}"
        self.microstepExplain.setPlainText(explanationText)
        # highlight source code
        sourceFileName = self.hco["locations"]["0"]["file"]
        # start row; start col; end row; end col of current microstep
        sourceCodeR1 = int(self.hco["locations"][str(pc)]["line"])
        sourceCodeR2 = int(self.hco["locations"][str(pc)]["endline"])
        sourceCodeC1 = int(self.hco["locations"][str(pc)]["column"])
        sourceCodeC2 = int(self.hco["locations"][str(pc)]["endcolumn"]) + 1
        # start row; start col; end row; end col of stmt
        stmtR1 = int(self.hco['locations'][str(pc)]['stmt'][0])
        stmtC1 = int(self.hco['locations'][str(pc)]['stmt'][1])
        stmtR2 = int(self.hco['locations'][str(pc)]['stmt'][2])
        stmtC2 = int(self.hco['locations'][str(pc)]['stmt'][3])
        # # update thread browser scroll bar
        # self.threadBrowser.verticalScrollBar().setValue(threadId)
        if self.hco["locations"][str(pc)]["file"] == sourceFileName:
            # if code is in sourcefile
            self.openFile(self.sourceCode, self.sourceFile, microStepPointer)

            self.clearFormat(self.sourceCodeCursor)
            
            stmtStartPos = self.getPosition(self.sourceCode, stmtR1, stmtC1)
            stmtEndPos = self.getPosition(self.sourceCode, stmtR2, stmtC2)   
            self.sourceCodeCursor.setPosition(stmtStartPos - 1)
            self.sourceCodeCursor.setPosition(stmtEndPos - 1, QtGui.QTextCursor.KeepAnchor)
            fmt = QtGui.QTextCharFormat()
            fmt.setBackground(QtCore.Qt.yellow)
            self.sourceCodeCursor.mergeCharFormat(fmt)

            startPos = self.getPosition(self.sourceCode, sourceCodeR1, sourceCodeC1)
            endPos = self.getPosition(self.sourceCode, sourceCodeR2, sourceCodeC2)
            self.sourceCodeCursor.setPosition(startPos - 1)
            self.sourceCodeCursor.setPosition(endPos - 1, QtGui.QTextCursor.KeepAnchor)
            fmt = QtGui.QTextCharFormat()
            fmt.setBackground(QtCore.Qt.green)
            self.sourceCodeCursor.mergeCharFormat(fmt)
            self.sourceCode.verticalScrollBar().setValue(sourceCodeR1 - 8)

            # self.highlightByCoordinate(self.sourceCode, self.sourceCodeCursor, sourceCodeR1, sourceCodeR2, sourceCodeC1, sourceCodeC2)
        else:
            # if code is in library file
            self.openFile(self.sourceCode, self.hco["locations"][str(pc)]["file"], microStepPointer)

            self.clearFormat(self.sourceCodeCursor)
            
            stmtStartPos = self.getPosition(self.sourceCode, stmtR1, stmtC1)
            stmtEndPos = self.getPosition(self.sourceCode, stmtR2, stmtC2)   
            self.sourceCodeCursor.setPosition(stmtStartPos - 1)
            self.sourceCodeCursor.setPosition(stmtEndPos - 1, QtGui.QTextCursor.KeepAnchor)
            fmt = QtGui.QTextCharFormat()
            fmt.setBackground(QtCore.Qt.yellow)
            self.sourceCodeCursor.mergeCharFormat(fmt)

            startPos = self.getPosition(self.sourceCode, sourceCodeR1, sourceCodeC1)
            endPos = self.getPosition(self.sourceCode, sourceCodeR2, sourceCodeC2)
            self.sourceCodeCursor.setPosition(startPos - 1)
            self.sourceCodeCursor.setPosition(endPos - 1, QtGui.QTextCursor.KeepAnchor)
            fmt = QtGui.QTextCharFormat()
            fmt.setBackground(QtCore.Qt.green)
            self.sourceCodeCursor.mergeCharFormat(fmt)
            self.sourceCode.verticalScrollBar().setValue(sourceCodeR1 - 8)

        # hightlight machine code
        pcMAX = len(self.hco["code"]) - 1
        offsetDigit = len(str(pcMAX))
        byteCodeR1 = self.microStepPointer + 1
        byteCodeR2 = self.microStepPointer + 1
        byteCodeC1 = 1 + (offsetDigit) + 1
        byteCodeC2 = 1 + len(self.hco["code"][pc]) + (offsetDigit) + 1 # account for pc value at start
        self.highlightByCoordinate(self.byteCode, self.byteCodeCursor, byteCodeR1, byteCodeR2, byteCodeC1, byteCodeC2)
        # if current microstep is an unconditional jump, then update an arrow (do a red highlight)
        microstep = self.hco['code'][pc]
        npc = int(self.microSteps[microStepPointer]["npc"])
        nrow = int(self.hco["locations"][str(npc)]["line"])
        ncol = int(self.hco["locations"][str(npc)]["column"])

        curFile = self.hco["locations"][str(pc)]["file"]
        nextFile = self.hco["locations"][str(npc)]["file"]
        # print(microstep)
        if len(microstep) >= 5 and microstep[:5] == "Jump " and curFile == nextFile:
            self.highlightJumpCoordinate(nrow, ncol)

    def nextMicrostep(self):
        if self.byteCode.toPlainText() == "":
            return
        if self.microStepPointer == len(self.microSteps):
            return
        # next microstep if self.singleStep is selected
        if self.singleStep.isChecked():
            self.microStepPointer = self.microStepPointer + 1
        # next statement if self.singleStep is NOT selected
        # step over (does not go into any function)
        else:
            i = self.microStepPointer
            tid = int(self.microSteps[i]['tid'])
            curStackLength = len(self.stackTraceTextList[i - 1 if i > 0 else i][tid].split(" -> "))
            while self.stmtIndicator[i] == True:
                i += 1
            i += 1
            self.microStepPointer = i
            nextsmtStackLength = len(self.stackTraceTextList[i - 1 if i > 0 else i][tid].split(" -> "))
            if nextsmtStackLength > curStackLength:
                self.downMicroStep()
        self.updateState()

        # if self.microStepPointer < len(self.microSteps):
        #     pc = int(self.microSteps[self.microStepPointer]["pc"])
        #     print(self.microStepPointer, self.hco['locations'][str(pc)]['stmt'], self.stmtIndicator[self.microStepPointer])
        # else:
        #     print(self.microStepPointer)


    def prevMicroStep(self):
        if self.byteCode.toPlainText() == "":
            return
        if self.microStepPointer == 0:
            return

        # next microstep if self.singleStep is selected
        if self.singleStep.isChecked():
            self.microStepPointer = self.microStepPointer - 1
        # next statement if self.singleStep NOT selected
        # step over (does not go into any function)
        else:
            # handle special case and fix bug
            if self.microStepPointer == len(self.microSteps):
                self.microStepPointer -= 1
                self.updateState()
                return
            i = self.microStepPointer
            tid = int(self.microSteps[i]['tid'])
            curStackLength = len(self.stackTraceTextList[i - 1 if i > 0 else i][tid].split(" -> "))
            while i > 0 and self.stmtIndicator[i - 1] == True:
                i -= 1
            if i > 0:
                i -= 1
            while i > 0 and self.stmtIndicator[i - 1] == True:
                i -= 1
            self.microStepPointer = i
            prevsmtStackLength = len(self.stackTraceTextList[i - 1 if i > 0 else i][tid].split(" -> "))
            if prevsmtStackLength > curStackLength:
                    self.upMicroStep()
        self.updateState()

        # if self.microStepPointer < len(self.microSteps):
        #     pc = int(self.microSteps[self.microStepPointer]["pc"])
        #     print(self.microStepPointer, self.hco['locations'][str(pc)]['stmt'], self.stmtIndicator[self.microStepPointer])
        # else:
        #     print(self.microStepPointer)

    def upMicroStep(self):
        if self.byteCode.toPlainText() == "":
            return
        if self.microStepPointer == 0:
            return
        if self.microStepPointer == len(self.microSteps):
            # if in final extra microstep
            self.microStepPointer -= 1
        else:
            # not in final extra microstep
            i = self.microStepPointer
            tid = int(self.microSteps[i]['tid'])
            curStackLength = len(self.stackTraceTextList[i - 1 if i > 0 else i][tid].split(" -> "))
            while i >= 0 and len(self.stackTraceTextList[i - 1 if i > 0 else i][tid].split(" -> ")) >= curStackLength and int(self.microSteps[i]['tid']) == tid:
                i -= 1
            if i < 0:
                i = 0
            self.microStepPointer = i
        self.updateState()


    def downMicroStep(self):
        if self.byteCode.toPlainText() == "":
            return
        if self.microStepPointer == len(self.microSteps):
            return
        i = self.microStepPointer
        tid = int(self.microSteps[i]['tid'])
        curStackLength = len(self.stackTraceTextList[i - 1 if i > 0 else i][tid].split(" -> "))
        while i < len(self.microSteps) and len(self.stackTraceTextList[i - 1 if i > 0 else i][tid].split(" -> ")) >= curStackLength and int(self.microSteps[i]['tid']) == tid:
            i += 1
        if i == len(self.microSteps):
            i = len(self.microSteps) - 1
        self.microStepPointer = i
        self.updateState()

    def sliderMoveUpdate(self):
        if self.byteCode.toPlainText() == "":
            return
        self.microStepPointer = self.horizontalSlider.value()
        self.updateState()
    
    def updateState(self):
        self.highlightUpdate(self.microStepPointer)
        self.sharedVariableUpdate(self.microStepPointer)
        self.localVariableUpdate(self.microStepPointer)
        self.stackTopUpdate(self.microStepPointer)
        self.updateCheckBox(self.microStepPointer)
        self.threadBrowserUpdate(self.microStepPointer)
            
    def errorMsgBox(self, text):
        msg = QMessageBox()
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
    
    def save_file(self):
        filepath = self.fileNameLabel.text()
        text = self.plainTextEdit.toPlainText()
        try:
            with open(filepath, 'w') as file:
                file.write(text)
        except:
            self.errorMsgBox("Save failed. The file path is invalid. ")

    def highlightByCoordinate(self, editor, cursor, r1, r2, c1, c2):
        # # Handle invalid inputs
        # try:
        #     r1 = int(self.startRowText.text())
        #     r2 = int(self.endRowText.text())
        #     c1 = int(self.startColText.text())
        #     c2 = int(self.endColText.text())
        # # return error message if input are not integers
        # except:
        #     self.errorMsgBox("Input not valid")
        #     return

        # return error message if input are not positive
        if r1 <= 0 or r2 <= 0 or c1 <= 0 or c2 <= 0:
            self.errorMsgBox("1")
            return
        # return error message if start position is greater than end position
        if r1 > r2:
            self.errorMsgBox("2")
            return
        if r1 == r2 and c1 > c2:
            self.errorMsgBox("3")
            return
        # return error message if row number is out of bound
        try:
            startPos = self.getPosition(editor, r1, c1)
            endPos = self.getPosition(editor, r2, c2)
        except:
            # self.errorMsgBox("4")
            return
        self.clearFormat(cursor)
        cursor.setPosition(startPos - 1)
        cursor.setPosition(endPos - 1, QtGui.QTextCursor.KeepAnchor)
        fmt = QtGui.QTextCharFormat()
        # change bytecode color from yellow to green
        fmt.setBackground(QtCore.Qt.yellow if editor == self.sourceCode else QtCore.Qt.green)
        cursor.mergeCharFormat(fmt)
        editor.verticalScrollBar().setValue(r1 - 8)

    def highlightJumpCoordinate(self, row, col):
        editor = self.sourceCode
        cursor = self.sourceCodeCursor
        try:
            position = self.getPosition(editor, row, col)
        except:
            self.errorMsgBox("jump error")
            return 
        cursor.setPosition(position - 1)
        cursor.setPosition(position, QtGui.QTextCursor.KeepAnchor)
        fmt = QtGui.QTextCharFormat()
        fmt.setBackground(QtCore.Qt.red)
        cursor.mergeCharFormat(fmt)

    def getPosition(self, editor, row, column):
        text = editor.toPlainText()
        lines = text.splitlines(True)
        # handle the edge case - determine whether file ends with a newline
        if lines[-1][-1] == "\n":
            lines.append("")
        pos = 0
        # disallow row number to be out of bound
        if row > len(lines):
            row = len(lines)
            # raise Exception("Row number out of bound")
        for i in range(row - 1):
            pos += len(lines[i])
        # allow column number to be out of bound
        if column > len(lines[row - 1]):
            column = len(lines[row - 1]) + 1
        pos += column
        return pos

    def clearFormat(self, cursor):
        fmt = QtGui.QTextCharFormat()
        fmt.setBackground(QtCore.Qt.transparent)
        cursor.mergeCharFormat(fmt)

    def createThreadImg(self):
        h, w = 8, 600
        imgList = []
        for i in range(self.threadNumber):
            imgData = 245 * np.ones((h, w, 3), dtype=np.uint8) # initialize all images to be inactive color (grey)
            imgList.append(imgData)
        microstepThread = [] # microstepThread is a list that maps microsteps to their thread number
        for microstep in self.microSteps:
            microstepThread.append(int(microstep['tid']))
        microstepsNumber = len(self.microSteps)
        for i in range(microstepsNumber):
            # for each microstep, start is the starting coloring pixel and end is the ending coloring pixel
            start = int(w * (i / microstepsNumber))
            end = int(w * ((i + 1) / microstepsNumber))
            curThread = microstepThread[i] # the tid of current thread
            for j in range(h):
                for k in range(start, end):
                    assert len(self.threadColor) == self.threadNumber
                    imgList[curThread][j, k] = self.threadActiveColors[self.threadColor[curThread]]
        # save all the image in imgList
        for i in range(len(imgList)):
            img = Image.fromarray(imgList[i], 'RGB')
            filePath = self.hco["locations"]["0"]["file"][:-4]
            fileName = filePath.rsplit('/', 1)[-1]
            imageName = f"{fileName}_t{i}.png"
            imageDirName = f"{self.sourceFile[:-4]}_threadImg"
            # print(filePath)
            # print(fileName)
            # print(imageName)
            # print(imageDirName)
            try:
                img.save(f"{imageDirName}/{imageName}")
            except:
                os.mkdir(f"{imageDirName}")
                img.save(f"{imageDirName}/{imageName}")

    def threadBrowserUpdate(self, microStepPointer):
        if microStepPointer > 0:
            microStepPointer -= 1
        self.threadBrowser.setText("")
        cursorPosition = 4
        filePath = self.hco["locations"]["0"]["file"][:-4]
        fileName = filePath.rsplit('/', 1)[-1]
        imageDirName = f"{self.sourceFile[:-4]}_threadImg"
        # print(fileName)
        # print(imageDirName)
        for i in range(self.threadNumber):
            imageName = f"{fileName}_t{i}.png"
            # i can be 1-digit, 2-digit, or 3-digit
            if i < 10:
                self.threadBrowser.append(f"T{i}  ")
            elif i < 100:
                self.threadBrowser.append(f"T{i} ")
            elif i < 1000:
                self.threadBrowser.append(f"T{i}")
            else:
                raise Exception("thread number out of bound")
            document = self.threadBrowser.document()
            cursor = QTextCursor(document)
            cursor.setPosition(cursorPosition)
            cursor.insertImage(f"{imageDirName}/{imageName}")
            cursorPosition += 1
            cursor.setPosition(cursorPosition)
            cursor.insertText(f" {self.stackTraceTextList[microStepPointer][i]}")
            cursorPosition += (len(self.stackTraceTextList[microStepPointer][i]) + 6)

        
        # self.threadBrowser.append("T0  ")
        # document = self.threadBrowser.document()
        # cursor = QTextCursor(document)
        # cursor.setPosition(4)
        # cursor.insertImage(f"{self.sourceFile[:-4]}_threadBrowserImg/my.png")

        # TODO: handle cases where threadId has more than 1 digit

    def sharedVariableUpdate(self, microStepPointer):
        # clear all displayed content
        self.sharedVariables.clear() 
        if microStepPointer == 0:
            return
        microStepPointer -= 1
        # find current shared variable state
        mostRecentSharedVariablePointer = microStepPointer
        while 'shared' not in self.microSteps[mostRecentSharedVariablePointer]:
            mostRecentSharedVariablePointer -= 1
        microstep = self.microSteps[mostRecentSharedVariablePointer]
        sharedVariableList = microstep['shared']
        primitiveTypes = {'int', 'bool', 'atom', 'pc'}
        # iterate through harmony values in sharedVariableList
        counter = 0 
        for variableName, variable in sharedVariableList.items():
            item_0 = QtWidgets.QTreeWidgetItem(self.sharedVariables)
            if variable['type'] in primitiveTypes: 
                self.sharedVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
            elif variable['type'] == 'address':
                if self.isNaive(variable):
                    self.sharedVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                else:
                    self.recursiveAdd(item_0, self.sharedVariables.topLevelItem(counter), variable, variableName)
            elif variable['type'] == 'list':
                if self.isNaive(variable):
                    self.sharedVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                else:
                    self.recursiveAdd(item_0, self.sharedVariables.topLevelItem(counter), variable, variableName)
            elif variable['type'] == 'set':
                if self.isNaive(variable):
                    self.sharedVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                else:
                    self.recursiveAdd(item_0, self.sharedVariables.topLevelItem(counter), variable, variableName)
            elif variable['type'] == 'dict':
                self.recursiveAdd(item_0, self.sharedVariables.topLevelItem(counter), variable, variableName)
            elif variable['type'] == 'context':
                self.recursiveAdd(item_0, self.sharedVariables.topLevelItem(counter), variable, variableName)
            else:
                raise Exception("Unexpected Harmony type")
            counter += 1
    
    def localVariableUpdate(self, microStepPointer):
        # clear all displayed content
        self.localVariables.clear() 
        if microStepPointer == 0:
            return
        microStepPointer -= 1
        # find current local variable state
        mostRecentLocalVariablePointer = microStepPointer
        while 'local' not in self.microSteps[mostRecentLocalVariablePointer]:
            mostRecentLocalVariablePointer -= 1
        microstep = self.microSteps[mostRecentLocalVariablePointer]
        localVariableList = microstep['local']
        # assert microstep['tid'] == self.microSteps[microStepPointer]['tid']
        primitiveTypes = {'int', 'bool', 'atom', 'pc'}
        # iterate through harmony values in localVariableList
        counter = 0 
        for variableName, variable in localVariableList.items():
            item_0 = QtWidgets.QTreeWidgetItem(self.localVariables)
            if variable['type'] in primitiveTypes: 
                self.localVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
            elif variable['type'] == 'address':
                if self.isNaive(variable):
                    self.localVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                else:
                    self.recursiveAdd(item_0, self.localVariables.topLevelItem(counter), variable, variableName)
            elif variable['type'] == 'list':
                if self.isNaive(variable):
                    self.localVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                else:
                    self.recursiveAdd(item_0, self.localVariables.topLevelItem(counter), variable, variableName)
            elif variable['type'] == 'set':
                if self.isNaive(variable):
                    self.localVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                else:
                    self.recursiveAdd(item_0, self.localVariables.topLevelItem(counter), variable, variableName)
            elif variable['type'] == 'dict':
                self.recursiveAdd(item_0, self.localVariables.topLevelItem(counter), variable, variableName)
            elif variable['type'] == 'context':
                self.recursiveAdd(item_0, self.localVariables.topLevelItem(counter), variable, variableName)
            else:
                raise Exception("Unexpected Harmony type")
            counter += 1

    def stackTopUpdate(self, microStepPointer):
        # clear all displayed content
        self.stackTop.clear() 
        if microStepPointer == 0:
            item_0 = QtWidgets.QTreeWidgetItem(self.stackTop)
            self.stackTop.topLevelItem(0).setText(0, "()")
            return
        microStepPointer -= 1
        stackTopVariableList = self.stackTopDisplay[microStepPointer]
        primitiveTypes = {'int', 'bool', 'atom', 'pc'}
        # iterate through harmony values in stackTopVariableList
        counter = 0 
            
        for variable in stackTopVariableList:
            item_0 = QtWidgets.QTreeWidgetItem(self.stackTop)
            if variable['type'] in primitiveTypes: 
                self.stackTop.topLevelItem(counter).setText(0, f"{self.variableToText(variable['type'], variable)}")
            elif variable['type'] == 'address':
                if self.isNaive(variable):
                    self.stackTop.topLevelItem(counter).setText(0, f"{self.variableToText(variable['type'], variable)}")
                else:
                    self.recursiveAdd(item_0, self.stackTop.topLevelItem(counter), variable, "")
            elif variable['type'] == 'list':
                if self.isNaive(variable):
                    self.stackTop.topLevelItem(counter).setText(0, f"{self.variableToText(variable['type'], variable)}")
                else:
                    self.recursiveAdd(item_0, self.stackTop.topLevelItem(counter), variable, "")
            elif variable['type'] == 'set':
                if self.isNaive(variable):
                    self.stackTop.topLevelItem(counter).setText(0, f"{self.variableToText(variable['type'], variable)}")
                else:
                    self.recursiveAdd(item_0, self.stackTop.topLevelItem(counter), variable, "")
            elif variable['type'] == 'dict':
                if len(variable['value']) == 0:
                    # special case: empty dictionary - show {:}
                    self.stackTop.topLevelItem(counter).setText(0, f"{{:}}")
                else:
                    self.recursiveAdd(item_0, self.stackTop.topLevelItem(counter), variable, "")
            elif variable['type'] == 'context':
                self.recursiveAdd(item_0, self.stackTop.topLevelItem(counter), variable, "")
            else:
                raise Exception("Unexpected Harmony type")
            counter += 1

    def recursiveAdd(self, item, node, variable, variableName):
        """
        recursively display harmony values to treelist view
        """
        primitiveTypes = {'int', 'bool', 'atom', 'pc'}
        if variable['type'] in primitiveTypes:
            # base case 1
            node.setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
        elif variable['type'] == 'context':
            # base case
            node.setText(0, f"{variableName} <context>")
            # TODO: Improve on displaying context value (what information is included?)
            ctxKeys = ['pc', 'sp']
            for i in range(len(ctxKeys)):
                new_items = []
                new_items.append(QtWidgets.QTreeWidgetItem(item))
            for i in range(len(ctxKeys)):
                node.child(i).setText(0, f"{ctxKeys[i]}: {self.variableToText(variable['value'][ctxKeys[i]]['type'], variable['value'][ctxKeys[i]])}")
        elif variable['type'] == 'address':
            if self.isNaive(variable):
                # base case
                node.setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                return
            node.setText(0, f"{variableName} <address>")
            for i in range(len(variable['value'])):
                new_items = []
                new_items.append(QtWidgets.QTreeWidgetItem(item))
            for i in range(len(variable['value'])):
                self.recursiveAdd(node.child(i), node.child(i), variable['value'][i], f"[{i}]")
        elif variable['type'] == 'list':
            if self.isNaive(variable):
                # base case
                node.setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                return
            node.setText(0, f"{variableName} <list>")
            for i in range(len(variable['value'])):
                new_items = []
                new_items.append(QtWidgets.QTreeWidgetItem(item))
            for i in range(len(variable['value'])):
                self.recursiveAdd(node.child(i), node.child(i), variable['value'][i], f"[{i}]")
        elif variable['type'] == 'set':
            if self.isNaive(variable):
                # base case
                node.setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                return
            node.setText(0, f"{variableName} <set>")
            for i in range(len(variable['value'])):
                new_items = []
                new_items.append(QtWidgets.QTreeWidgetItem(item))
            for i in range(len(variable['value'])):
                self.recursiveAdd(node.child(i), node.child(i), variable['value'][i], f"[{i}]")
        elif variable['type'] == 'dict':
            # dictionary is naive (all keys are primitive types)
            if self.isNaive(variable):
                # special case empty dictionary
                if len(variable['value']) == 0:
                    assert variable['value'] == []
                    node.setText(0, f"{variableName} = {{}}")
                    return
                node.setText(0, f"{variableName} <dict>")
                for i in range(len(variable['value'])):
                    new_items = []
                    new_items.append(QtWidgets.QTreeWidgetItem(item))
                for i in range(len(variable['value'])):
                    keyValue = variable['value'][i]['key']
                    assert keyValue['type'] in primitiveTypes
                    key = self.variableToText(keyValue['type'], keyValue)
                    self.recursiveAdd(node.child(i), node.child(i), variable['value'][i]['value'], f"[{key}]")
            # special the case where dictionary is not naive
            else:
                node.setText(0, f"{variableName} <dict>")
                for i in range(len(variable['value'])):
                    new_items = []
                    new_items.append(QtWidgets.QTreeWidgetItem(item))
                    new_items.append(QtWidgets.QTreeWidgetItem(item))
                for i in range(len(variable['value'])):
                    self.recursiveAdd(node.child(2*i), node.child(2*i), variable['value'][i]['key'], f"key[{i}]")
                    self.recursiveAdd(node.child(2*i + 1), node.child(2*i + 1), variable['value'][i]['value'], f"value[{i}]")

    def variableToText(self, type, value):
        """
        Transform non-recursive variables to text (primitive values and naive non-primitive values)
        """
        if type == 'int':
            # e.g, { "type": "int", "value": "1" } -> "1"
            return value['value']
        elif type == 'bool':
            # e.g, { "type": "bool", "value": "True" } -> "True"
            return value['value']
        elif type == 'atom':
            # e.g, { "type": "atom", "value": "hello" } -> "\"hello\""
            return f"\"{value['value']}\""
        elif type == 'pc':
            pc = int(value['value'])
            byteCode = self.hco['code'][pc]
            # If pc points to a method or is lambda, then bytecode is "Frame ..."
            # shows everything after "Frame "
            if byteCode[:6] == 'Frame ':
                return byteCode[6:]
            else:
                # i points to the nearest bytecode that starts with "Frame "
                # show "pc({pcNumber} = {methodName} + {offset})"
                i = self.microStepPointer - 1 # !!!!!!!
                while self.hco['code'][int(self.microSteps[i]["pc"])][:6] != 'Frame ':
                    i -= 1
                assert i >= 0
                offset = pc - int(self.microSteps[i]["pc"])
                methodName = self.hco['code'][int(self.microSteps[i]["pc"])][6:]
                return f"pc({pc} = {methodName} + {offset})"
        elif type == 'address':
            assert self.isNaive(value)
            if len(value['value']) == 0:
                return "None"
            addrStr = "?"
            addrStr += value['value'][0]['value']
            for i in range(1, len(value['value'])):
                addrStr += f"[{value['value'][i]['value']}]"
            return addrStr
        elif type == 'list':
            assert self.isNaive(value)
            # a harmony value of type list whose entries are primitive
            listText = ""
            naiveList = value['value']
            if len(naiveList) == 0:
                return "[ ]"
            for i in range(len(naiveList) - 1):
                element = naiveList[i]
                listText += f"{self.variableToText(element['type'], element)}, "
            lastElement = naiveList[len(naiveList) - 1]
            listText += f"{self.variableToText(lastElement['type'], lastElement)}"
            listText = f"[ {listText} ]"
            return listText
        elif type == 'set':
            assert self.isNaive(value)
            # a harmony value of type set whose entries are primitive
            setText = ""
            naiveSet = value['value']
            if len(naiveSet) == 0:
                return "{ }"
            for i in range(len(naiveSet) - 1):
                element = naiveSet[i]
                setText += f"{self.variableToText(element['type'], element)}, "
            lastElement = naiveSet[len(naiveSet) - 1]
            setText += f"{self.variableToText(lastElement['type'], lastElement)}"
            setText = "{ " + setText + " }"
            return setText

    def isNaive(self, value):
        """
        determine whether a non-primitive value (list/set or dictionary or address) is naive 
        A list/set is naive iff all entries are primitive values
        A dictionary is naive iff all keys are primitive values
        An address is naive iff all values in the list are primitive values
        """
        assert value['type'] in {'list', 'set', 'dict', 'address'}
        primitiveTypes = {'int', 'bool', 'atom', 'pc'}
        # handle the case of a list/set
        if value['type'] in {'list', 'set'}:
            for element in value['value']:
                if element['type'] not in primitiveTypes:
                    # Do not return False if this is a naive address
                    if element['type'] == 'address' and self.isNaive(element):
                        continue
                    return False
            return True
        # handle the case of a dictonary
        elif value['type'] == 'dict':
            for keyValuePair in value['value']:
                if keyValuePair['key']['type'] not in primitiveTypes:
                    # Do not return False if this is a naive address
                    if keyValuePair['key']['type'] == 'address' and self.isNaive(keyValuePair['key']):
                        continue
                    return False
            return True
        # handle the case of a dictionary
        elif value['type'] == 'address':
            for element in value['value']:
                if element['type'] not in primitiveTypes:
                    return False
            return True
        
    def constructStackTraceTextList(self):
        assert len(self.stackTraceList) == self.threadNumber
        assert len(self.stackTraceTextList) == len(self.microSteps)
        # base case for i = 0 to fix the initial stack trace
        assert 'contexts' in self.hco['macrosteps'][0]
        for thread in self.hco['macrosteps'][0]['contexts']:
            tid = int(thread['tid'])
            assert 'trace' in thread
            trace = thread['trace']
            traceLine = ""
            assert len(trace) > 0
            for j in range(len(trace) - 1):
                traceLine = traceLine + trace[j]['method'] + ' -> '
            traceLine += trace[len(trace) - 1]['method']
            self.stackTraceList[tid] = traceLine
        self.stackTraceTextList[0] = []
        for stackTraceLine in self.stackTraceList:
            self.stackTraceTextList[0].append(stackTraceLine)
        # other microsteps for i > 0
        for i in range(1, len(self.microSteps)):
            if 'trace' in self.microSteps[i]:
                # there is a change in stack trace
                trace = self.microSteps[i]['trace']
                traceLine = ""
                if(len(trace) > 0):
                    for j in range(len(trace) - 1):
                        traceLine = traceLine + trace[j]['method'] + ' -> '
                    traceLine = traceLine + trace[len(trace) - 1]['method']
                tid = int(self.microSteps[i]['tid'])
                self.stackTraceList[tid] = traceLine
                # update the ith entry in self.stackTraceTextList
                self.stackTraceTextList[i] = []
                for stackTraceLine in self.stackTraceList:
                    self.stackTraceTextList[i].append(stackTraceLine)
            else:
                # there is no change in stack trace
                self.stackTraceTextList[i] = copy.deepcopy(self.stackTraceTextList[i - 1])
            # print failure in stack trace (commented out since already covered by next)
            # if 'failure' in self.microSteps[i]:
            #     tid = int(self.microSteps[i]['tid'])
            #     self.stackTraceTextList[i][tid] += f" -> {self.microSteps[i]['failure']}!"
            
        # add "about to" information to the end of stack trace line
        i = 0
        for macrostep in self.hco['macrosteps']:
            i += len(macrostep['microsteps']) - 1
            assert 'contexts' in macrostep
            for context in macrostep['contexts']:
                if 'next' in context and int(context['tid']) == int(self.microSteps[i]['tid']):
                    tid = int(self.microSteps[i]['tid'])
                    self.stackTraceTextList[i][tid] += f" ({self.about(context)})"
                    tmp = i + 1
                    while tmp < len(self.microSteps) and int(self.microSteps[tmp]['tid']) != tid:
                        self.stackTraceTextList[tmp][tid] += f" ({self.about(context)})"
                        tmp += 1
            i += 1

        for i in range(len(self.stackTraceTextList)):
            for j in range(len(self.stackTraceTextList[i])):
                self.stackTraceTextList[i][j] = f"[{self.threadMode[i][j]}] " + self.stackTraceTextList[i][j] 

    def constructStackTopDisplay(self):
        """
        construct self.stackTopDisplay
        """
        stacks = []
        self.stackTopDisplay = []
        for i in range(self.threadNumber):
            stacks.append([])
        # default stack for each thread
        for t in range(self.threadNumber):
            i = 0
            while int(self.microSteps[i]['tid']) != t:
                i += 1
            stacks[t] = self.microSteps[i]['context']['stack']
        framePointer = -1
        for i in range(len(self.microSteps)):
            tid = int(self.microSteps[i]['tid'])
            # update frame pointer
            if 'fp' in self.microSteps[i]:
                framePointer = int(self.microSteps[i]['fp'])
            # pop items first
            if 'pop' in self.microSteps[i]:
                assert len(stacks[tid]) >= int(self.microSteps[i]['pop'])
                for j in range(int(self.microSteps[i]['pop'])):
                    del stacks[tid][-1]
            if 'push' in self.microSteps[i]:
                for variable in self.microSteps[i]['push']:
                    stacks[tid].append(variable)
            # update self.stackTopDisplay
            self.stackTopDisplay.append([])
            for k in range(framePointer, len(stacks[tid])):
                self.stackTopDisplay[i].append(stacks[tid][k])

    def constructThreadMode(self):
        # initialize self.threadMode
        for i in range(len(self.microSteps)):
            self.threadMode.append([])
            for j in range(self.threadNumber):
                self.threadMode[i].append("runnable")
        # construct thread mode for each microstep
        i = 0
        for macrostep in self.hco['macrosteps']:
            if i > 0:
                self.threadMode[i] = copy.deepcopy(self.threadMode[i - 1])
            if 'contexts' in macrostep:
                for context in macrostep['contexts']:
                    if 'mode' in context:
                        self.threadMode[i][int(context['tid'])] = 'runnable' if context['mode'] == 'choosing' else context['mode'] # change choosing to runnable
            if ('context' in macrostep) and ('mode' in macrostep['context']):
                self.threadMode[i][int(macrostep['context']['tid'])] = 'runnable' if macrostep['context']['mode'] == 'choosing' else macrostep['context']['mode']
            for j in range(len(macrostep['microsteps'])):
                if j > 0:
                    self.threadMode[i] = copy.deepcopy(self.threadMode[i - 1])
                if 'mode' in macrostep['microsteps'][j]:
                    self.threadMode[i][int(self.microSteps[i]['tid'])] = 'runnable' if macrostep['microsteps'][j]['mode'] == 'choosing' else macrostep['microsteps'][j]['mode']
                if j < len(macrostep['microsteps']) - 1:
                    i += 1
            if 'contexts' in macrostep:
                for context in macrostep['contexts']:
                    if 'mode' in context:
                        self.threadMode[i][int(context['tid'])] = 'runnable' if context['mode'] == 'choosing' else context['mode']
            i += 1
        # for k in range(len(self.threadMode)):
        #     print(self.threadMode[k])
        

    def displayIssue(self):
        issueText = self.hco["issue"]
        self.issue.setText(f"Issue: {issueText}")

    def constructCheckBox(self):
        for i in range(len(self.microSteps)):
            assert 'context' in self.microSteps[i]
            assert 'tid' in self.microSteps[i]
            tid = int(self.microSteps[i]['tid'])
            # construct atomic status for each microstep and each thread
            if 'atomic' in self.microSteps[i]:
                self.checkBoxList[i][tid]['atomic'] = int(self.microSteps[i]['atomic']) > 0
            elif 'atomic' in self.microSteps[i]['context']:
                self.checkBoxList[i][tid]['atomic'] = int(self.microSteps[i]['context']['atomic']) > 0
            else:
                if i > 0:
                    self.checkBoxList[i][tid]['atomic'] = self.checkBoxList[i - 1][tid]['atomic']
            # construct readonly status for each microstep and each thread
            if 'readonly' in self.microSteps[i]:
                self.checkBoxList[i][tid]['readonly'] = int(self.microSteps[i]['readonly']) > 0
            elif 'readonly' in self.microSteps[i]['context']:
                self.checkBoxList[i][tid]['readonly'] = int(self.microSteps[i]['context']['readonly']) > 0
            else:
                if i > 0:
                    self.checkBoxList[i][tid]['readonly'] = self.checkBoxList[i - 1][tid]['readonly']
            # construct interrupt-disabled status for each microstep and each thread
            # TODO: small differences from .hco file, e.g. Frame handler()
            if 'interruptlevel' in self.microSteps[i]:
                self.checkBoxList[i][tid]['interrupt-disabled'] = int(self.microSteps[i]['interruptlevel']) > 0
            elif 'interruptlevel' in self.microSteps[i]['context']:
                self.checkBoxList[i][tid]['interrupt-disabled'] = int(self.microSteps[i]['context']['interruptlevel']) > 0
            else:
                if i > 0:
                    self.checkBoxList[i][tid]['interrupt-disabled'] = self.checkBoxList[i - 1][tid]['interrupt-disabled']

    def updateCheckBox(self, microStepPointer):
        if microStepPointer == 0:
            self.atomic.setChecked(False)
            self.readOnly.setChecked(False)
            self.interruptDisabled.setChecked(False)
            return
        microStepPointer -= 1
        i = microStepPointer
        tid = int(self.microSteps[i]['tid'])
        # update atomic checkbox
        self.atomic.setChecked(self.checkBoxList[i][tid]['atomic'])
        # update readonly checkbox
        self.readOnly.setChecked(self.checkBoxList[i][tid]['readonly'])
        # update interrupt-disabled checkbox
        self.interruptDisabled.setChecked(self.checkBoxList[i][tid]['interrupt-disabled'])

    def verbose_kv(self, js):
        return (self.verbose_string(js["key"]), self.verbose_string(js["value"]))

    def verbose_idx(self, js):
        return "[" + self.verbose_string(js) + "]"

    def verbose_string(self, js):
        type = js["type"]
        v = js["value"]
        if type == "bool":
            return v
        if type == "int":
            return str(v) if isinstance(v, int) else v
        if type == "atom":
            return json.dumps(v, ensure_ascii=False)
        if type == "set":
            if v == []:
                return "{}"
            lst = [ self.verbose_string(val) for val in v ]
            return "{ " + ", ".join(lst) + " }"
        if type == "list":
            if v == []:
                return "[]"
            lst = [ self.verbose_string(val) for val in v ]
            return "[ " + ", ".join(lst) + " ]"
        if type == "dict":
            if v == []:
                return "{:}"
            lst = [ self.verbose_kv(kv) for kv in v ]
            keys = [ k for k,v in lst ]
            if keys == [str(i) for i in range(len(v))]:
                return "[ " + ", ".join([v for k,v in lst]) + " ]" 
            else:
                return "{ " + ", ".join([k + ": " + v for k,v in lst]) + " }" 
        if type == "pc":
            return "PC(%s)"%v
        if type == "address":
            if v == []:
                return "None"
            return "?" + v[0]["value"] + "".join([ self.verbose_idx(kv) for kv in v[1:] ])
        if type == "context":
            return "CONTEXT(" + str(v["pc"]) + ")"

    def about(self, ctx):
        nxt = ctx["next"]
        if nxt["type"] == "Frame":
            return f"about to run method {nxt['name']} with argument {self.verbose_string(nxt['value'])}"
        elif nxt["type"] == "Load":
            return f"about to load variable {nxt['var']}"
        elif nxt["type"] == "Store":
            return f"about to store: {nxt['var']}<-{self.verbose_string(nxt['value'])}"
        elif nxt["type"] == "Print":
            return f"about to print {self.verbose_string(nxt['value'])}"
        elif nxt["type"] == "AtomicInc":
            return "about to execute atomic section"
        elif nxt["type"] == "Assert":
            return "assertion failed"
        else:
            return f"about to {nxt['type']}"

    def constantWindow(self):
        constant = QDialog()
        constant.ui = Ui_Dialog()
        constant.ui.setupUi(constant, self.constantDic, "Enter constants")
        constant.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        constant.exec_()
    
    def moduleWindow(self):
        constant = QDialog()
        constant.ui = Ui_Dialog()
        constant.ui.setupUi(constant, self.moduleDic, "Enter modules")
        constant.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        constant.exec_()


class Ui_Dialog(object):
    def setupUi(self, Dialog, dic, diagType):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 371, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(19)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)
        self.add = QtWidgets.QToolButton(Dialog)
        self.add.setGeometry(QtCore.QRect(10, 260, 26, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.remove = QtWidgets.QToolButton(Dialog)
        self.remove.setGeometry(QtCore.QRect(40, 260, 26, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.remove.setFont(font)
        self.remove.setObjectName("remove")
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(220, 260, 71, 32))
        self.cancel.setObjectName("cancel")
        self.apply = QtWidgets.QPushButton(Dialog)
        self.apply.setGeometry(QtCore.QRect(310, 260, 71, 32))
        self.apply.setObjectName("apply")
        self.run = QtWidgets.QPushButton(Dialog)
        self.run.setGeometry(QtCore.QRect(90, 260, 71, 32))
        self.run.setObjectName("run")

        self.d = Dialog
        self.dic = dic

        self.add.clicked.connect(self._addRow)
        self.remove.clicked.connect(self._removeRow)
        self.cancel.clicked.connect(self._cancel)
        self.apply.clicked.connect(self._apply)
        self.run.clicked.connect(self._run)

        self.retranslateUi(Dialog, diagType)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self._display()

    def retranslateUi(self, Dialog, diagType):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Value"))
        self.add.setText(_translate("Dialog", "+"))
        self.remove.setText(_translate("Dialog", "-"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.apply.setText(_translate("Dialog", "Apply"))
        self.run.setText(_translate("Dialog", "Run"))

    def _display(self):
        i = 0
        for k in self.dic:
          self._addRow()
          self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(k))
          self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.dic[k]))
          i += 1

    def _addRow(self):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)

    def _removeRow(self):
        if self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(self.tableWidget.rowCount() - 1)
    
    def _cancel(self):
        self.d.close()
    
    def _apply(self):
        self.dic.clear()
        for i in range(self.tableWidget.rowCount()):
          k = self.tableWidget.item(i, 0).text()
          v = self.tableWidget.item(i, 1).text()
          self.dic[k] = v

    def _run(self):
        self._apply()
        ui.runSource()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # open file passed in as commandline argument
    n = len(sys.argv)
    if not 1 <= n <= 2:
        raise Exception("Cannot have more than 1 parameter")
    if n == 2:
        fpath = os.path.join(os.getcwd(), sys.argv[1])
        ui.browseFiles(True, fpath)
        
    sys.exit(app.exec_())
