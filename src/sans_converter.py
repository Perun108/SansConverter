"""The main module for the app logic"""

import sys

from PyQt5 import QtCore, QtWidgets

from encoding_mappings import (
    ALL_EXT_ENCODINGS,
    CYRILLIC_ENCODINGS,
    HK,
    HK_EXT,
    ROMAN_BASIC_ENCODINGS,
    Encodings,
)
from service import convert
from windows.about import Ui_Dialog2
from windows.converter import Ui_SansConverter
from windows.help import Ui_Dialog


class SansConverter(QtWidgets.QMainWindow):
    """This is the main class with all the logic and connections between the GUI parts and class methods"""

    settings = QtCore.QSettings("SansConverter", "Converter")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_SansConverter()
        self.ui.setupUi(self)
        # Read saved settings for "Use ṃ", original and target encodings, window
        # size and position:
        self.ui.comboBox.setCurrentText(self.settings.value("input_encoding_name"))
        self.ui.comboBox_2.setCurrentText(self.settings.value("output_encoding_name"))
        self.ui.checkBox.setChecked(self.settings.value("Use m", type=bool))
        self.resize(self.settings.value("WindowSize", QtCore.QSize(620, 550)))
        self.move(self.settings.value("Position", QtCore.QPoint(600, 230)))
        # Linking buttons, hotkeys and menus to functions
        self.ui.pushButton.clicked.connect(self.copy_converted)
        self.ui.pushButton_2.clicked.connect(self.swap_encodings)
        self.ui.pushButton_3.clicked.connect(self.clear_input)
        self.ui.pushButton_4.clicked.connect(self.paste_input)
        # Convert on the go when input_encoding_name is changed manually and
        # remember it (save it to external file) to use when
        # the program is started again
        self.ui.comboBox.currentIndexChanged.connect(self.convert)
        # Convert on the go when output_encoding_name is changed manually and
        # remember it (save it to external file) to use when
        # the programs is started again
        self.ui.comboBox_2.currentTextChanged.connect(self.convert)
        # Converts on the go while typing text into textEdit widget
        self.ui.textEdit.textChanged.connect(self.convert)
        # Converts again whenever "Use "ṃ"" is checked or unchecked
        self.ui.checkBox.stateChanged.connect(self.convert)
        self.ui.actionClear.triggered.connect(self.clear_input)
        self.ui.actionCopy.triggered.connect(self.copy_converted)
        self.ui.actionPaste.triggered.connect(self.paste_input)
        self.ui.actionRedo.triggered.connect(self.ui.textEdit.redo)
        self.ui.actionUndo.triggered.connect(self.ui.textEdit.undo)
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionSwap.triggered.connect(self.swap_encodings)
        self.ui.actionTransliteration_help.triggered.connect(self.open_help)
        self.ui.actionAbout_SansConverter.triggered.connect(self.open_about)
        self.show()

    def clear_input(self):
        """
        Clears the input window (and undoes history!)
        """
        self.ui.textEdit.clear()
        self.ui.textEdit.repaint()

    def paste_input(self):
        """
        Paste text from clipboard into the input window
        """
        self.ui.textEdit.paste()
        self.ui.textEdit.repaint()

    def open_help(self):
        """
        Opens another dialog window with help in it
        """
        self.window = QtWidgets.QDialog()
        self.ui1 = Ui_Dialog()
        self.ui1.setupGUi(self.window)
        self.window.show()

    def open_about(self):
        """
        Opens another dialog window with 'About' information
        """
        self.window = QtWidgets.QDialog()
        self.ui2 = Ui_Dialog2()
        self.ui2.setupUi(self.window)
        self.window.show()

    def convert(self) -> None:
        """
        Selects and sends arguments to the 'convert' method
        The first 4 lists are short lists with only those Roman letters that have diacritical marks
        They are used for converting between two encodings that are based on Roman script
        Other lists (RUS, UKR, GAURA_TIMES and the rest with '_EXT' are long lists with *all* symbols
        of the Roman/Cyrillic alphabet in both uppercase and lowercase)
        """
        text = self.ui.textEdit.toPlainText()
        input_encoding_name = self.ui.comboBox.currentText()
        output_encoding_name = self.ui.comboBox_2.currentText()

        # To save time for identical encodings we don't convert them
        if input_encoding_name != output_encoding_name:
            # Peculiarities of the HK scheme, it uses only lowercase letters
            if output_encoding_name == Encodings.HK.value:
                if input_encoding_name not in CYRILLIC_ENCODINGS and text.islower():
                    input_chars = ROMAN_BASIC_ENCODINGS[input_encoding_name]
                    output_chars = HK
                else:
                    input_chars = ALL_EXT_ENCODINGS[input_encoding_name]
                    output_chars = HK_EXT

            # Simplify transliteration of the similar encodings that are based on Roman script
            elif input_encoding_name not in CYRILLIC_ENCODINGS and output_encoding_name not in CYRILLIC_ENCODINGS:
                input_chars = ROMAN_BASIC_ENCODINGS[input_encoding_name]
                output_chars = ROMAN_BASIC_ENCODINGS[output_encoding_name]

            # For transliterating between Roman and Cyrillic transliterations
            else:
                input_chars = ALL_EXT_ENCODINGS[input_encoding_name]
                output_chars = ALL_EXT_ENCODINGS[output_encoding_name]

            text = convert(
                text,
                input_chars,
                output_chars,
                input_encoding_name,
                output_encoding_name,
                use_anusvara=self.ui.checkBox.isChecked(),
            )
        self.ui.textBrowser.setPlainText(text)

    def copy_converted(self) -> None:
        """
        Copies converted text from the output window when the 'Copy' button is pressed
        """
        self.ui.textBrowser.selectAll()
        self.ui.textBrowser.copy()

    def swap_encodings(self) -> None:
        """
        Pastes converted text from the output window, swaps encodings
        and converts the text back into original encoding
        """
        output = self.ui.textBrowser.toPlainText()
        enc1 = self.ui.comboBox.currentText()
        enc2 = self.ui.comboBox_2.currentText()
        self.ui.comboBox.setCurrentText(enc2)
        self.ui.comboBox_2.setCurrentText(enc1)
        self.ui.textEdit.setPlainText(output)
        self.ui.textEdit.repaint()

    def closeEvent(self, event) -> None:
        """
        Remembers settings and quits the program
        """
        self.settings.setValue("input_encoding_name", self.ui.comboBox.currentText())
        self.settings.setValue("output_encoding_name", self.ui.comboBox_2.currentText())
        self.settings.setValue("Use m", self.ui.checkBox.isChecked())
        self.settings.setValue("WindowSize", self.size())
        self.settings.setValue("Position", self.pos())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = SansConverter()
    sys.exit(app.exec_())
