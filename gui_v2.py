# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v2.6.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QTextCursor, QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat 
from PIL import Image
import numpy as np
from gui_import.codeeditor import CodeEditor
import json
import os
import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.filePathText = QtWidgets.QLineEdit(self.centralwidget)
        self.filePathText.setReadOnly(True)
        self.filePathText.setObjectName("filePathText")
        self.horizontalLayout_5.addWidget(self.filePathText)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setObjectName("browse")
        self.horizontalLayout_5.addWidget(self.browse)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.byteCode = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.byteCode.setFont(font)
        self.byteCode.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.byteCode.setObjectName("byteCode")
        self.horizontalLayout.addWidget(self.byteCode)
        self.sourceCode = CodeEditor(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.sourceCode.setFont(font)
        self.sourceCode.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.sourceCode.setObjectName("sourceCode")
        self.horizontalLayout.addWidget(self.sourceCode)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.microstepExplain = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.microstepExplain.setMinimumSize(QtCore.QSize(0, 0))
        self.microstepExplain.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.microstepExplain.setFont(font)
        self.microstepExplain.setReadOnly(True)
        self.microstepExplain.setPlainText("")
        self.microstepExplain.setObjectName("microstepExplain")
        self.verticalLayout_2.addWidget(self.microstepExplain)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.microstepsLabel = QtWidgets.QLabel(self.centralwidget)
        self.microstepsLabel.setText("")
        self.microstepsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.microstepsLabel.setObjectName("microstepsLabel")
        self.verticalLayout.addWidget(self.microstepsLabel)
        self.sharedVariables = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.sharedVariables.setFont(font)
        self.sharedVariables.setObjectName("sharedVariables")
        self.verticalLayout.addWidget(self.sharedVariables)
        self.localVariables = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.localVariables.setFont(font)
        self.localVariables.setObjectName("localVariables")
        self.verticalLayout.addWidget(self.localVariables)
        self.stackTop = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.stackTop.setFont(font)
        self.stackTop.setObjectName("stackTop")
        self.verticalLayout.addWidget(self.stackTop)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.prevIns = QtWidgets.QPushButton(self.centralwidget)
        self.prevIns.setObjectName("prevIns")
        self.horizontalLayout_7.addWidget(self.prevIns)
        self.nextIns = QtWidgets.QPushButton(self.centralwidget)
        self.nextIns.setObjectName("nextIns")
        self.horizontalLayout_7.addWidget(self.nextIns)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.threadOffsetLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.threadOffsetLabel.setFont(font)
        self.threadOffsetLabel.setObjectName("threadOffsetLabel")
        self.horizontalLayout_6.addWidget(self.threadOffsetLabel)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(605, 0))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(605, 16777215))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_6.addWidget(self.horizontalSlider)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.stackTraceLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.stackTraceLabel.setFont(font)
        self.stackTraceLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.stackTraceLabel.setObjectName("stackTraceLabel")
        self.gridLayout_2.addWidget(self.stackTraceLabel, 0, 1, 1, 1)
        self.stackTrace = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.stackTrace.setFont(font)
        self.stackTrace.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.stackTrace.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.stackTrace.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.stackTrace.setPlainText("")
        self.stackTrace.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.stackTrace.setObjectName("stackTrace")
        self.gridLayout_2.addWidget(self.stackTrace, 1, 1, 1, 1)
        self.threadBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.threadBrowser.setMinimumSize(QtCore.QSize(650, 0))
        self.threadBrowser.setMaximumSize(QtCore.QSize(650, 16777215))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.threadBrowser.setFont(font)
        self.threadBrowser.setObjectName("threadBrowser")
        self.threadBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.gridLayout_2.addWidget(self.threadBrowser, 1, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 10)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_3.setStretch(1, 10)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.browse.clicked.connect(self.browseFiles)
        self.nextIns.clicked.connect(self.nextMicrostep)
        self.prevIns.clicked.connect(self.prevMicroStep)
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


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.sharedVariables.headerItem().setText(0, _translate("MainWindow", "Shared Variables"))
        self.localVariables.headerItem().setText(0, _translate("MainWindow", "Local Variables"))
        self.stackTop.headerItem().setText(0, _translate("MainWindow", "Stack Top"))
        self.prevIns.setText(_translate("MainWindow", "< Prev"))
        self.prevIns.setShortcut(_translate("MainWindow", "Left"))
        self.nextIns.setText(_translate("MainWindow", "Next >"))
        self.nextIns.setShortcut(_translate("MainWindow", "Right"))
        self.threadOffsetLabel.setText(_translate("MainWindow", "    "))
        self.stackTraceLabel.setText(_translate("MainWindow", "Stack Trace"))


    def openFile(self, editor, file):
        text = open(file).read()
        editor.setPlainText(text)
    
    def browseFiles(self):
        fname = QFileDialog.getOpenFileName(None, "Title", "..", "Harmony source code (*.hny)")[0]
        if(fname == ""):
            return
        self.filePathText.setText(fname)
        # try open source code file
        try:
            self.openFile(self.sourceCode, fname)
            # self.fileNameLabel.setText(fname)
        except:
            self.filePathText.setText("")
            self.errorMsgBox("This file cannot be opened. Please open another file.")
            return
        
        # try compile hvm file
        runcmd = subprocess.run(["./harmony", "--noweb", fname], capture_output=True)
        returncode = runcmd.returncode
        stdout =  runcmd.stdout.decode()
        stderr =  runcmd.stderr.decode()
        # .hny file fail to compile
        if returncode != 0:
            self.errorMsgBox("Run Failed\n" + stdout + stderr)
            return
        
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
        # construct self.microSteps to be a list of microsteps
        self.constructMicrosteps()
        # construct self.stackTraceText to be stack trace to display at each microstep
        self.constructStackTraceTextList()
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
        self.horizontalSlider.setMaximum(len(self.microSteps) - 1)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        # initalize cursor
        # self.sourceCodeCursor = self.sourceCode.textCursor()
        self.byteCodeCursor = self.byteCode.textCursor()
        # update the highlight part
        self.sourceFile = fname
        self.highlightUpdate()
        # display thread browser
        self.displayThreadBrowser()
        # update shared variable
        self.sharedVariableUpdate()
        # update local variable
        self.localVariableUpdate()
        # update stack trace
        self.stackTraceUpdate()

    def constructMicrosteps(self):
        self.microSteps = []
        # initialize self.threadNumber to be number of threads
        self.threadNumber = len(self.hco['macrosteps'][0]['contexts'])
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
                self.microSteps.append(cpMicroStep)
        # initialize self.stackTraceList
        for i in range(self.threadNumber):
            self.stackTraceList.append("")
        # initialize 
        for i in range(len(self.microSteps)):
            self.stackTraceTextList.append("")

    def highlightUpdate(self):
        # update microsteps label
        self.microstepsLabel.setText(f"Microsteps: {self.microStepPointer + 1}/{len(self.microSteps)}")
        # update horizontal slider
        self.horizontalSlider.setValue(self.microStepPointer)
        # update highlight part
        pc = int(self.microSteps[self.microStepPointer]["pc"])
        # update microstepExplain label
        explanation = self.hco['explain'][pc]
        threadId = int(self.microSteps[self.microStepPointer]['tid'])
        assert int(self.microSteps[self.microStepPointer]['contexts'][threadId]['tid']) == threadId
        threadName = self.microSteps[self.microStepPointer]['contexts'][threadId]['name']
        fileName = self.hco['locations'][str(pc)]['file']
        explanationText = f"T{threadId} {threadName}: {explanation}\n{fileName}"
        self.microstepExplain.setPlainText(explanationText)
        # highlight source code
        sourceFileName = self.hco["locations"]["0"]["file"]
        # start row; start col; end row; end col
        sourceCodeR1 = int(self.hco["locations"][str(pc)]["line"])
        sourceCodeR2 = int(self.hco["locations"][str(pc)]["endline"])
        sourceCodeC1 = int(self.hco["locations"][str(pc)]["column"])
        sourceCodeC2 = int(self.hco["locations"][str(pc)]["endcolumn"]) + 1
        # # update thread browser scroll bar
        # self.threadBrowser.verticalScrollBar().setValue(threadId)
        if self.hco["locations"][str(pc)]["file"] == sourceFileName: 
            # if code is in sourcefile
            self.openFile(self.sourceCode, self.sourceFile)
            self.highlightByCoordinate(self.sourceCode, self.sourceCodeCursor, sourceCodeR1, sourceCodeR2, sourceCodeC1, sourceCodeC2)
        else:
            # if code is in library file
            self.openFile(self.sourceCode, self.hco["locations"][str(pc)]["file"])
            self.highlightByCoordinate(self.sourceCode, self.sourceCodeCursor, sourceCodeR1, sourceCodeR2, sourceCodeC1, sourceCodeC2)
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
        npc = int(self.microSteps[self.microStepPointer]["npc"])
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
        if self.microStepPointer == len(self.microSteps) - 1:
            return
        self.microStepPointer = self.microStepPointer + 1
        self.highlightUpdate()
        self.sharedVariableUpdate()
        self.localVariableUpdate()
        self.stackTraceUpdate()

    def prevMicroStep(self):
        if self.byteCode.toPlainText() == "":
            return
        if self.microStepPointer == 0:
            return
        self.microStepPointer = self.microStepPointer - 1
        self.highlightUpdate()
        self.sharedVariableUpdate()
        self.localVariableUpdate()
        self.stackTraceUpdate()

    def sliderMoveUpdate(self):
        if self.byteCode.toPlainText() == "":
            return
        self.microStepPointer = self.horizontalSlider.value()
        self.highlightUpdate()
        self.sharedVariableUpdate()
        self.localVariableUpdate()
        self.stackTraceUpdate()
    
    def openFileByTypedPath(self):
        filepath = self.filePathText.text()
        try:
            self.openFile(filepath)
            # self.fileNameLabel.setText(filepath)
        except FileNotFoundError:
            self.errorMsgBox(f"No such file or directory: '{filepath}'")
        except:
            self.filePathText.setText("")
            self.errorMsgBox("This file cannot be opened. Please open another file.")
            
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
        fmt.setBackground(QtCore.Qt.yellow)
        cursor.setCharFormat(fmt)
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
        cursor.setCharFormat(fmt)
        # cursor.setPosition(jumpDesPos - 2)
        # cursor.setPosition(jumpDesPos - 1, QtGui.QTextCursor.KeepAnchor)
        # fmt = QtGui.QTextCharFormat()
        # fmt.setBackground(QtCore.Qt.red)
        # cursor.setCharFormat(fmt)

    def getPosition(self, editor, row, column):
        text = editor.toPlainText()
        lines = text.splitlines(True)
        # handle the edge case - determine whether file ends with a newline
        if lines[-1][-1] == "\n":
            lines.append("")
        pos = 0
        # disallow row number to be out of bound
        if row > len(lines):
            raise Exception("Row number out of bound")
        for i in range(row - 1):
            pos += len(lines[i])
        # allow column number to be out of bound
        if column > len(lines[row - 1]):
            column = len(lines[row - 1]) + 1
        pos += column
        return pos

    def clearFormat(self, cursor):
        fmt = QtGui.QTextCharFormat()
        cursor.setCharFormat(fmt)

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

    def displayThreadBrowser(self):
        self.threadBrowser.setText("")
        self.createThreadImg()
        cursorPosition = -2
        filePath = self.hco["locations"]["0"]["file"][:-4]
        fileName = filePath.rsplit('/', 1)[-1]
        imageDirName = f"{self.sourceFile[:-4]}_threadImg"
        # print(fileName)
        # print(imageDirName)
        for i in range(self.threadNumber):
            imageName = f"{fileName}_t{i}.png"
            cursorPosition += 6
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
        
        # self.threadBrowser.append("T0  ")
        # document = self.threadBrowser.document()
        # cursor = QTextCursor(document)
        # cursor.setPosition(4)
        # cursor.insertImage(f"{self.sourceFile[:-4]}_threadBrowserImg/my.png")

        # TODO: handle cases where threadId has more than 1 digit

    def sharedVariableUpdate(self):
        # clear all displayed content
        self.sharedVariables.clear() 
        # find current shared variable state
        mostRecentSharedVariablePointer = self.microStepPointer
        while 'shared' not in self.microSteps[mostRecentSharedVariablePointer]:
            mostRecentSharedVariablePointer -= 1
        microstep = self.microSteps[mostRecentSharedVariablePointer]
        sharedVariableList = microstep['shared']
        # TODO: are pc and address primitive?
        primitiveTypes = {'int', 'bool', 'atom', 'pc', 'address'}
        # iterate through harmony values in sharedVariableList
        counter = 0 
        for variableName, variable in sharedVariableList.items():
            item_0 = QtWidgets.QTreeWidgetItem(self.sharedVariables)
            if variable['type'] in primitiveTypes: 
                self.sharedVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
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
            counter += 1
    
    def localVariableUpdate(self):
        # clear all displayed content
        self.localVariables.clear() 
        # find current local variable state
        mostRecentLocalVariablePointer = self.microStepPointer
        while 'local' not in self.microSteps[mostRecentLocalVariablePointer]:
            mostRecentLocalVariablePointer -= 1
        microstep = self.microSteps[mostRecentLocalVariablePointer]
        localVariableList = microstep['local']
        assert microstep['tid'] == self.microSteps[self.microStepPointer]['tid']
        # TODO: are pc and address primitive?
        primitiveTypes = {'int', 'bool', 'atom', 'pc', 'address'}
        # iterate through harmony values in localVariableList
        counter = 0 
        for variableName, variable in localVariableList.items():
            item_0 = QtWidgets.QTreeWidgetItem(self.localVariables)
            if variable['type'] in primitiveTypes: 
                self.localVariables.topLevelItem(counter).setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
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
            counter += 1

    def recursiveAdd(self, item, node, variable, variableName):
        """
        recursively display harmony values to treelist view
        """
        primitiveTypes = {'int', 'bool', 'atom', 'pc', 'address'}
        if variable['type'] in primitiveTypes:
            # base case 1
            node.setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
        if variable['type'] == 'list':
            if self.isNaive(variable):
                # base case
                node.setText(0, f"{variableName}: {self.variableToText(variable['type'], variable)}")
                return
            node.setText(0, f"{variableName} <list>")
            for i in range(len(variable['value'])):
                new_items = []
                new_items.append(QtWidgets.QTreeWidgetItem(item))
            for i in range(len(variable['value'])):
                self.recursiveAdd(node.child(i), node.child(i), variable['value'][i], f"{variableName}[{i}]")
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
                self.recursiveAdd(node.child(i), node.child(i), variable['value'][i], f"{variableName}[{i}]")
        elif variable['type'] == 'dict':
            node.setText(0, f"{variableName} <dict>")
            for i in range(len(variable['value'])):
                new_items = []
                new_items.append(QtWidgets.QTreeWidgetItem(item))
            for i in range(len(variable['value'])):
                keyValue = variable['value'][i]['key']
                # !!! here we are assuming dictionary key is of primitive type
                # is it safe to assume so?
                assert keyValue['type'] in primitiveTypes
                key = self.variableToText(keyValue['type'], keyValue)
                self.recursiveAdd(node.child(i), node.child(i), variable['value'][i]['value'], f"{variableName}[{key}]")

    # TODO: context variable
    def variableToText(self, type, value):
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
            # TODO: if pc points to a label, only shows "pc(pc_number)"
            else:
                return f"pc({pc})"
        elif type == 'address':
            # Precondition: everything in adress is of type string and int
            # TODO: what if is not string or int? list/dictionary/set? boolean? 
            # value['value'] is a list of harmony values
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
        determine whether a list or set is naive
        """
        assert value['type'] == 'list' or value['type'] == 'set'
        primitiveTypes = {'int', 'bool', 'atom', 'pc', 'address'}
        for element in value['value']:
            if element['type'] not in primitiveTypes:
                return False
        return True


    # TODO: merge self.threadBrowser and self.stackTrace
    def constructStackTraceTextList(self):
        # assert len(self.stackTraceList) == self.threadNumber
        # assert len(self.stackTraceTextList) == len(self.microSteps)
        for i in range(len(self.microSteps)):
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
                text = ""
                for stackTraceLine in self.stackTraceList:
                    text = text + stackTraceLine + "\n"
                self.stackTraceTextList[i] = text
            else:
                # there is no change in stack trace
                self.stackTraceTextList[i] = self.stackTraceTextList[i - 1]

    def stackTraceUpdate(self):
        self.stackTrace.setPlainText(self.stackTraceTextList[self.microStepPointer])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
