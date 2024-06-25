"""The main module for the app logic"""

import sys

from PyQt5 import QtCore, QtWidgets

from encoding_mappings import (
    ALL_EXT_ENCODINGS,
    ASPIRATED_CYRILLIC_LETTERS,
    ASPIRATED_ROMAN_LETTERS,
    CYRILLIC_ENCODINGS,
    HK,
    HK_EXT,
    ROMAN_BASIC_ENCODINGS,
)
from windows.about import Ui_Dialog2
from windows.converter import Ui_SansConverter
from windows.help import Ui_Dialog


class SansConverter:
    """This is the main class with all the logic and connections between the GUI parts and class methods"""

    settings = QtCore.QSettings("SansConverter", "Converter")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_SansConverter()
        self.ui.setupUi(self)
        # Read saved settings for "Use ṃ", original and target encodings, window
        # size and position:
        self.ui.comboBox.setCurrentText(self.settings.value("input_encoding"))
        self.ui.comboBox_2.setCurrentText(self.settings.value("output_encoding"))
        self.ui.checkBox.setChecked(self.settings.value("Use m", type=bool))
        self.resize(self.settings.value("WindowSize", QtCore.QSize(620, 550)))
        self.move(self.settings.value("Position", QtCore.QPoint(600, 230)))
        # Linking buttons, hotkeys and menus to functions
        self.ui.pushButton.clicked.connect(self.copy_converted)
        self.ui.pushButton_2.clicked.connect(self.swap_encodings)
        self.ui.pushButton_3.clicked.connect(self.clear_input)
        self.ui.pushButton_4.clicked.connect(self.paste_input)
        # Convert on the go when input_encoding is changed manually and
        # remember it (save it to external file) to use when
        # the program is started again
        self.ui.comboBox.currentIndexChanged.connect(self.pressed)
        # Convert on the go when output_encoding is changed manually and
        # remember it (save it to external file) to use when
        # the programs is started again
        self.ui.comboBox_2.currentTextChanged.connect(self.pressed)
        # Converts on the go while typing text into textEdit widget
        self.ui.textEdit.textChanged.connect(self.pressed)
        # Converts again whenever "Use "ṃ"" is checked or unchecked
        self.ui.checkBox.stateChanged.connect(self.pressed)
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

    def convert(
        self,
        string: str,
        start_symbols_list: list[str],
        end_symbols_list: list[str],
        input_encoding: str,
        output_encoding: str,
    ) -> None:
        """
        This is the main method which converts between encodings.

        Args:
            string (str): input text to convert into another encoding
            start_symbols_list (list): list with all symbols of the original encoding
                (each in its own place, index matters!)
            end_symbols_list (list): list with all corresponding symbols of the target encoding
                (each in its own respective place, index matters!)
            input_encoding (str): Name of the original encoding
            output_encoding (str): Name of the target encoding
        """

        for i, item in enumerate(start_symbols_list):
            if item in string:
                string = string.replace(item, end_symbols_list[i])
        # Set proper case for 'Дж'
        if "Дж" in string:
            string = self.convert_j_properly(string)
        # Replace russian e when converting from Ukrainian
        if input_encoding == "Cyrillic (Russian)" and output_encoding != "Cyrillic (Russian)":
            string = self.replace_russian_e_from_ukrainian(string, output_encoding)
        # Replace russian e at the beginning of a word
        if output_encoding == "Cyrillic (Russian)":
            string = self.replace_russian_e_at_beginning(string)
        # Change anusvara if the checkBox is checked
        if self.ui.checkBox.isChecked():
            string = self.change_anusvara_type(string)
        if input_encoding == "HK":
            string = string.lower()
        # If any encoding is Ukrainian then follow the loops below
        if input_encoding == "Cyrillic (Ukrainian)" or output_encoding == "Cyrillic (Ukrainian)":
            string = self.convert_ukrainian(string, input_encoding, output_encoding)
        self.ui.textBrowser.setPlainText(string)

    def convert_ukrainian(self, string, input_encoding, output_encoding):
        # 'temp_symbols' is a temporary list of all the symbols in our converted text
        temp_symbols = self.convert_aspirated_cyrillic_properly(string)
        # This is only for Ukrainian into Russian (change dga into dha)
        if input_encoding == "Cyrillic (Ukrainian)" and output_encoding == "Cyrillic (Russian)":
            temp_symbols = self.change_ga_to_ha(temp_symbols)
            # 'x' is the joined list 's' (original converted text
            # but now with all necessary transormations)
        converted_text = "".join(temp_symbols)
        return converted_text

    def change_anusvara_type(self, string):
        if "ṁ" in string:
            string = string.replace("ṁ", "ṃ")
        elif "Ṁ" in string:
            string = string.replace("Ṁ", "Ṃ")
        elif "м̇" in string:
            string = string.replace("м̇", "м̣")
        elif "М̇" in string:
            string = string.replace("М̇", "М̣")
        return string

    def replace_russian_e_from_ukrainian(self, string, output_encoding):
        if output_encoding == "Cyrillic (Ukrainian)":
            string = string.replace("э", "е")
            string = string.replace("Э", "Е")
        else:
            string = string.replace("э", "e")
            string = string.replace("Э", "E")
        return string

    def change_ga_to_ha(self, temp_symbols: list) -> list:
        """Change гг to гх in cyrillic"""
        for i in range(len(temp_symbols) - 1):
            if temp_symbols[i].lower() in ASPIRATED_CYRILLIC_LETTERS and temp_symbols[i + 1] == "г":
                temp_symbols[i + 1] = "х"
            elif temp_symbols[i].lower() in ASPIRATED_CYRILLIC_LETTERS and temp_symbols[i + 1] == "Г":
                temp_symbols[i + 1] = "Х"
        return temp_symbols

    def convert_aspirated_cyrillic_properly(self, string: str) -> list:
        """Fix wrong conversions that happen due to overlapping symbols"""
        # 'temp_symbols' is a temporary list of all the symbols in our converted text
        # 'ASPIRATED_CYRILLIC_LETTERS' and 'ASPIRATED_ROMAN_LETTERS' are list of letters corresponding
        # to the aspirated consonants in Sanskrit (Cyrillic and Roman).
        temp_symbols = list(string)
        for i in range(len(temp_symbols) - 1):
            if temp_symbols[i].lower() in ASPIRATED_CYRILLIC_LETTERS and temp_symbols[i + 1] == "х":
                temp_symbols[i + 1] = "г"
            elif temp_symbols[i].lower() in ASPIRATED_CYRILLIC_LETTERS and temp_symbols[i + 1] == "Х":
                temp_symbols[i + 1] = "Г"
            if temp_symbols[i].lower() in ASPIRATED_ROMAN_LETTERS and temp_symbols[i + 1] == "г":
                temp_symbols[i + 1] = "h"
            elif temp_symbols[i].lower() in ASPIRATED_ROMAN_LETTERS and temp_symbols[i + 1] == "Г":
                temp_symbols[i + 1] = "H"
        return temp_symbols

    def replace_russian_e_at_beginning(self, string: str) -> str:
        """Replaces е with э at the beginning of a word"""
        if string.startswith("е"):
            string = string.replace("е", "э", 1)
        if string.startswith("Е"):
            string = string.replace("Е", "Э", 1)
        if "\nе" in string:
            string = string.replace("\nе", "\nэ")
        if "\nЕ" in string:
            string = string.replace("\nЕ", "\nЭ")
        if " е" in string:
            string = string.replace(" е", " э")
        if " Е" in string:
            string = string.replace(" Е", " Э")
        return string

    def convert_j_properly(self, string: str) -> str:
        """Converts j to  cyrillic дж"""
        try:
            position = 0
            while string != "Дж" and position != -1:
                if string[position:].startswith("Дж") and string[position + 2].isupper():
                    string = string[:position] + "ДЖ" + string[position + 2 :]
                position = string.find("Дж", position + 1)
        except IndexError:
            string = string[:-1] + "Ж"
        return string

    def pressed(self) -> None:
        """
        Selects and sends arguments to the 'convert' method
        The first 4 lists are short lists with only those Roman letters that have diacritical marks
        They are used for converting between two encodings that are based on Roman script
        Other lists (RUS, UKR, GAURA_TIMES and the rest with '_EXT' are long lists with *all* symbols
        of the Roman/Cyrillic alphabet in both uppercase and lowercase)
        """
        text = self.ui.textEdit.toPlainText()
        input_encoding = self.ui.comboBox.currentText()
        output_encoding = self.ui.comboBox_2.currentText()
        if input_encoding == output_encoding:  # To save time for identical encodings
            self.ui.textBrowser.setPlainText(text)
        elif output_encoding == "HK":  # Peculiarities of the HK scheme, it uses only lowercase letters
            if input_encoding not in CYRILLIC_ENCODINGS and text.islower():
                self.convert(
                    text,
                    ROMAN_BASIC_ENCODINGS[input_encoding],
                    HK,
                    input_encoding,
                    output_encoding,
                )
            else:
                self.convert(
                    text.lower(),
                    ALL_EXT_ENCODINGS[input_encoding],
                    HK_EXT,
                    input_encoding,
                    output_encoding,
                )
        # Simplify transliteration of the similar encodings that are based on Roman script
        elif input_encoding not in CYRILLIC_ENCODINGS and output_encoding not in CYRILLIC_ENCODINGS:
            self.convert(
                text,
                ROMAN_BASIC_ENCODINGS[input_encoding],
                ROMAN_BASIC_ENCODINGS[output_encoding],
                input_encoding,
                output_encoding,
            )
        # For transliterating between Roman and Cyrillic transliterations
        else:
            self.convert(
                text,
                ALL_EXT_ENCODINGS[input_encoding],
                ALL_EXT_ENCODINGS[output_encoding],
                input_encoding,
                output_encoding,
            )

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
        self.settings.setValue("input_encoding", self.ui.comboBox.currentText())
        self.settings.setValue("output_encoding", self.ui.comboBox_2.currentText())
        self.settings.setValue("Use m", self.ui.checkBox.isChecked())
        self.settings.setValue("WindowSize", self.size())
        self.settings.setValue("Position", self.pos())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = SansConverter()
    sys.exit(app.exec_())
