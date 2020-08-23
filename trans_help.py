# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupGUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(617, 440)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "/home/brijabasi/Dropbox/Python_Converter/FINAL/icons8-om-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAutoFillBackground(True)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading |
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse |
                                           QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton.clicked.connect(Dialog.accept)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Help"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "<b>- IAST</b> is a transliteration system that is standard among scholars."
                                      "<br/>""<b>- Balaram</b> is a legacy ASCII transliteration system developed by ISKCON BBT.""<br/>"
                                      "<b>- Harvard-Kyoto</b> is another ASCII scheme to transliterate Sanskrit on any English keyboard without any additional software (but without capital letters).""<br/>"
                                      "<b>- Velthuis</b> is another ASCII scheme which allows capital letters.""<br/>"
                                      "- Cyrillic (Russian and Ukrainian) are based on the IAST system.""<br/>""<br/>"
                                      "<b>Velthuis scheme:</b>""<br/>"
                                      "- a double vowel for all long vowels (“aa”, “ii”, “uu”, “.rr”, “AA”, “.RR”, etc.)""<br/>"
                                      "- a dot before any consonant that has an underdot in IAST (“.m” for “ṃ”, “.r” for “ṛ”, “.t” for “ṭ”, etc.)""<br/>"
                                      "- a double quotation mark before any consonant that has any additional diacritical mark about it in IAST (except “ñ”) (“n for ṅ, \"s for ś, etc.)""<br/>"
                                      "- a tilde before “n” for ñ.""<br/>"
                                      "<br/>"
                                      "<b>Harvard-Kyoto scheme:</b>""<br/>"
                                      "A = ā, I = ī, U = ū, R = ṛ, RR = ṝ, lR = ḷ, M = ṃ, H = ḥ, G = ṅ, J = ñ, T = ṭ, D = ḍ, N = ṇ, z = ś, S = ṣ""<br/>"
                                      "<br/>"
                                      "For more information on different transliteration schemes visit the following links:""<br/>"
                                      "IAST: <a href=\"https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration\">https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration</a>""<br/>"
                                      "Harvard-Kyoto: <a href=\"https://en.wikipedia.org/wiki/Harvard-Kyoto\">https://en.wikipedia.org/wiki/Harvard-Kyoto</a>""<br/>"
                                      "Velthuis: <a href=\"https://en.wikipedia.org/wiki/Velthuis\">https://en.wikipedia.org/wiki/Velthuis</a>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupGUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
