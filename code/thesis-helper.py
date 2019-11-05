#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019年11月4日16:56:33
# @Author  : 穆华岭
# @Software: 毕业论文小助手
# @github    ：https://github.com/muhualing/
import os
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)
from controller import con
from watch_clip import WatchClip
translate_res = None

class PDFView(QWebEngineView):
    def __init__(self):
        super(PDFView, self).__init__()
        pdf_js_path = "file:///" + os.path.join(os.getcwd(), "code", "web", "viewer.html")
        print(os.getcwd())
        print(pdf_js_path)
        pdf_path = ""
        pdf_path = "file:///" + os.path.join(os.getcwd(), "sample","sample.pdf")
        print(pdf_path)
        pdf_js_path = pdf_js_path.replace('\\', '/')
        pdf_path = pdf_path.replace('\\', '/')
        self.load(QUrl.fromUserInput('%s?file=%s' % (pdf_js_path, pdf_path)))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("毕业论文小助手")
        global translate_res
        self.translate_res = QtWidgets.QTextEdit()
        self.translate_res.setStyleSheet("font: 14pt Roboto")
        vbox = QVBoxLayout()
        vbox.addWidget(self.translate_res)

        gbox = QtWidgets.QGroupBox("中文翻译结果")
        gbox.setStyleSheet("font: 12pt Roboto")
        gbox.setLayout(vbox)
        
        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(PDFView())
        hBoxLayout.addWidget(gbox)
        hBoxLayout.setStretch(0, 9)
        hBoxLayout.setStretch(1, 3)

        widget = QWidget()
        widget.setLayout(hBoxLayout)
        self.setCentralWidget(widget)
        self.showMaximized()
    
    def update(self, cur_text):
        self.translate_res.clear()
        self.translate_res.setText(cur_text)

    def closeEvent(self,event):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    con.clip_changed.connect(mainWindow.update)
    watch_clip_thread = WatchClip()
    watch_clip_thread.start()
    sys.exit(app.exec_())