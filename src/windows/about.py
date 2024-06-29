""" 'About' dialog window generated by QtDesigner"""

from PyQt6 import QtCore, QtGui, QtWidgets


class UiAboutDialog(QtWidgets.QDialog):
    """Creates an 'About' dialog window"""

    def __init__(self, parent):
        super().__init__(parent)
        # parent dialog will be SansConverter
        self.parent_dialog = parent
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.Popup)

    def setupUi(self, Dialog):
        """Sets up 'About' dialog window"""

        Dialog.setObjectName("Dialog")
        Dialog.resize(377, 350)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse
            | QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard
            | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/icons8-om-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton.clicked.connect(Dialog.accept)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """Adds formatted text to the 'About' dialog window"""

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.label.setText(
            _translate(
                "Dialog",
                "<b>SansConverter</b>"
                "<br/>"
                "<br/>"
                "SansConverter is an offline tool to easily convert romanized Sanskrit text from one system of "
                "transliteration to another."
                "<br/>"
                "<br/>"
                "It can also be used to type in Sanskrit text with diacritics (using HK or Velthuis systems)."
                "<br/>"
                "<br/>"
                "Copyright © 2022 Kostiantyn Perun."
                "<br/>"
                "Version 1.7"
                "<br/>"
                '<a href="https://github.com/Perun108">https://github.com/Perun108</a>'
                "<br/>"
                "<br/>"
                'Send your feedback or suggestions to <a href= "mailto: kosperun@gmail.com">kosperun@gmail.com</a>',
            )
        )
        self.pushButton.setText(_translate("Dialog", "Close"))
