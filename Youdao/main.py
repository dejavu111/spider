# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from translate import YouDao
class Ui_Youdao(object):
    def setupUi(self, Youdao):
        Youdao.setObjectName("Youdao")
        Youdao.resize(466, 275)
        Youdao.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.translated = QtWidgets.QTextBrowser(Youdao)
        self.translated.setGeometry(QtCore.QRect(240, 40, 201, 81))
        self.translated.setObjectName("translated")
        self.tobetranslate = QtWidgets.QTextEdit(Youdao)
        self.tobetranslate.setGeometry(QtCore.QRect(20, 40, 161, 81))
        self.tobetranslate.setObjectName("tobetranslate")
        self.pushButton = QtWidgets.QPushButton(Youdao)
        self.pushButton.setGeometry(QtCore.QRect(330, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Youdao)
        self.tobetranslate.textChanged.connect(self.translated.reload)
        QtCore.QMetaObject.connectSlotsByName(Youdao)
        self.pushButton.clicked.connect(self.action)

    def retranslateUi(self, Youdao):
        _translate = QtCore.QCoreApplication.translate
        Youdao.setWindowTitle(_translate("Youdao", "翻译"))
        self.tobetranslate.setHtml(_translate("Youdao", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请输入你要翻译的内容</p></body></html>"))
        self.pushButton.setText(_translate("Youdao", "翻译"))

    def action(self):
        text = self.tobetranslate.toPlainText()
        y = YouDao(text)
        result = y.get_result()
        self.translated.setText(result)

if __name__ == '__main__':
    # while True:
    #     words = input('输入要翻译的内容：(输入0退出)')
    #     if words=='0':
    #         break
    #     y = Youdao(words)
    #     y.get_result()
    import sys
    from PyQt5.QtGui import QIcon
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Youdao()
    ui.setupUi(widget)
    widget.show()
    #ui.translated.reload(Youdao(ui.tobetranslate.toPlainText()).get_result())
    sys.exit(app.exec_())