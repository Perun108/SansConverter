"""The main module for app logic"""

import sys

from PyQt5 import QtCore, QtWidgets

from windows.about import Ui_Dialog2
from windows.converter import Ui_SansConverter
from windows.help import Ui_Dialog


class SansConverter(QtWidgets.QMainWindow):
    """This is the main class with all the logic and connections between the GUI parts and class methods"""

    settings = QtCore.QSettings("SansConverter", "Converter")

    # fmt: off
    BALARAM = (
        "ä", "é", "ü", "ÿ", "è", "å", "ñ", "ì", "ï", "ö", "ò", "ë", "ç", "ù", "à",
        "Ä", "É", "Ü", "Ÿ", "È", "Å", "Ñ", "Ì", "Ï", "Ö", "Ò", "Ë", "Ç", "Ù", "À"
    )

    IAST = ("ā", "ī", "ū", "ḷ", "ṝ", "ṛ", "ṣ", "ṅ", "ñ", "ṭ", "ḍ", "ṇ", "ś", "ḥ", "ṁ",
            "Ā", "Ī", "Ū", "Ḷ", "Ṝ", "Ṛ", "Ṣ", "Ṅ", "Ñ", "Ṭ", "Ḍ", "Ṇ", "Ś", "Ḥ", "Ṁ")

    HK = (
        "A", "I", "U", "lR", "RR", "R", "S", "G", "J", "T", "D", "N", "z", "H", "M",
        "A", "I", "U", "lR", "RR", "R", "S", "G", "J", "T", "D", "N", "z", "H", "M"
    )

    VELTHIUS = (
        "aa", "ii", "uu", ".l", ".rr", ".r", ".s", '"n', "~n", ".t", ".d", ".n", '"s', ".h", ".m",
        "AA", "II", "UU", ".L", ".RR", ".R", ".S", '"N', "~N", ".T", ".D", ".N", '"S', ".H", ".M"
    )

    RUS = (
        "Ā", "Ӣ", "Ӯ", "Л̣", "Р̣̄", "Р̣", "Н̇", "Н̃", "Т̣", "Д̣", "Н̣", "Ш́", "Ш", "Х̣", "М̇", "А", "Б", "Ч",
        "Дж", "ДЖ", "Д", "Е", "Г", "Х", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "В",
        "Й", "ā", "ӣ", "ӯ", "л̣", "р̣̄", "р̣", "ш́", "ш", "н̇", "н̃", "т̣", "д̣", "н̣", "х̣", "м̇", "а", "б",
        "ч", "дж", "д", "е", "г", "х", "и", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "в", "й"
    )

    UKR = (
        "Ā", "Ī", "Ӯ", "Л̣", "Р̣̄", "Р̣", "Н̇", "Н̃", "Т̣", "Д̣", "Н̣", "Ш́", "Ш", "Х̣", "М̇", "А", "Б", "Ч",
        "Дж", "ДЖ", "Д", "Е", "Ґ", "Х", "І", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "В",
        "Й", "ā", "ī", "ӯ", "л̣", "р̣̄", "р̣", "ш́", "ш", "н̇", "н̃", "т̣", "д̣", "н̣", "х̣", "м̇", "а", "б",
        "ч", "дж", "д", "е", "ґ", "х", "і", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "в", "й"
    )

    BALARAM_EXT = (
        "Ä", "É", "Ü", "Ÿ", "È", "Å", "Ì", "Ï", "Ö", "Ò", "Ë", "Ç", "Ñ", "Ù", "À", "A", "B", "C",
        "J", "J", "D", "E", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V",
        "Y", "ä", "é", "ü", "ÿ", "è", "å", "ç", "ñ", "ì", "ï", "ö", "ò", "ë", "ù", "à", "a", "b",
        "c", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y"
    )

    IAST_EXT = (
        "Ā", "Ī", "Ū", "Ḷ", "Ṝ", "Ṛ", "Ṅ", "Ñ", "Ṭ", "Ḍ", "Ṇ", "Ś", "Ṣ", "Ḥ", "Ṁ", "A", "B", "C",
        "J", "J", "D", "E", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V",
        "Y", "ā", "ī", "ū", "ḷ", "ṝ", "ṛ", "ś", "ṣ", "ṅ", "ñ", "ṭ", "ḍ", "ṇ", "ḥ", "ṁ", "a", "b",
        "c", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y"
    )

    HK_EXT = (
        "A", "I", "U", "lR", "RR", "R", "G", "J", "T", "D", "N", "z", "S", "H", "M", "a", "b", "c",
        "j", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v",
        "y", "A", "I", "U", "lR", "RR", "R", "z", "S", "G", "J", "T", "D", "N", "H", "M", "a", "b",
        "c", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y"
    )

    VELTHIUS_EXT = (
        "AA", "II", "UU", ".L", ".RR", ".R", '"N', "~N", ".T", ".D", ".N", '"S', ".S", ".H", ".M",
        "A", "B", "C", "J", "J", "D", "E", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U",
        "V", "Y", "aa", "ii", "uu", ".l", ".rr", ".r", '"s', ".s", '"n', "~n", ".t", ".d", ".n", ".h", ".m",
        "a", "b", "c", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y"
    )
    # fmt: on

    # 'ASPIRATED_CYRILLIC' and 'ASPIRATED_ROMAN' are list of letters corresponding
    # to the aspirated consonants in Sanskrit (Cyrillic and Roman).
    ASPIRATED_CYRILLIC = ("к", "ґ", "ч", "ж", "т̣", "д̣", "т", "д", "п", "б")
    ASPIRATED_ROMAN = ("k", "g", "c", "j", "ṭ", "ḍ", "t", "d", "p", "b")
    # 'CYRILLIC_ENCODINGS' is the names of Cyrillic encodings
    CYRILLIC_ENCODINGS = ("Cyrillic (Russian)", "Cyrillic (Ukrainian)")
    # 'ROMAN_ENCODINGS' is the names of Roman encodings
    ROMAN_ENCODINGS = {
        "Balaram": BALARAM,
        "IAST": IAST,
        "HK": HK,
        "Velthius": VELTHIUS,
    }

    # 'ALL_ENCODINGS' is the names of full versions of both Roman and Cyrillic encodings
    ALL_ENCODINGS = {
        "Balaram": BALARAM_EXT,
        "IAST": IAST_EXT,
        "HK": HK_EXT,
        "Velthius": VELTHIUS_EXT,
        "Cyrillic (Russian)": RUS,
        "Cyrillic (Ukrainian)": UKR,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_SansConverter()
        self.ui.setupUi(self)
        # Read saved settings for "Use ṃ", encodings 1 an 2, window
        # size and position:
        self.ui.comboBox.setCurrentText(self.settings.value("encoding1"))
        self.ui.comboBox_2.setCurrentText(self.settings.value("encoding2"))
        self.ui.checkBox.setChecked(self.settings.value("Use m", type=bool))
        self.resize(self.settings.value("WindowSize", QtCore.QSize(620, 550)))
        self.move(self.settings.value("Position", QtCore.QPoint(600, 230)))
        # Linking buttons, hotkeys and menus to functions
        self.ui.pushButton.clicked.connect(self.copy_converted)
        self.ui.pushButton_2.clicked.connect(self.swap_encodings)
        self.ui.pushButton_3.clicked.connect(self.clear_input)
        self.ui.pushButton_4.clicked.connect(self.paste_input)
        # Convert on the go when encoding1 is changed manually and
        # remember it (save it to external file) to use when
        # the program is started again
        self.ui.comboBox.currentIndexChanged.connect(self.pressed)
        # Convert on the go when encoding2 is changed manually and
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
        Clears the input window (and undo history!)
        """
        self.ui.textEdit.clear()
        self.ui.textEdit.repaint()

    def paste_input(self):
        """
        Paste text from clipboard into input window
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
        start_symbols_list: list,
        end_symbols_list: list,
        encoding1: str,
        encoding2: str,
    ) -> None:
        """
        This is the main method which converts between encodings.

        Args:
            string (str): input text to convert into another encoding
            stat_symbols_list (list): list with all symbols of the original encoding
                (each in its own place, place matters!)
            end_symbols_list (list): list with all corresponding symbols of the target encoding
                (each in its own respective place, place matters!)
            encoding1 (str): Name of the original encoding
            encoding2 (str): Name of the target encoding
        """

        for i, item in enumerate(start_symbols_list):
            if item in string:
                string = string.replace(item, end_symbols_list[i])
        # Set proper case for 'Дж'
        if "Дж" in string:
            string = self.convert_j_properly(string)
        # Replace russian e when converting from Ukrainian
        if encoding1 == "Cyrillic (Russian)" and encoding2 != "Cyrillic (Russian)":
            string = self.replace_russian_e_from_ukrainian(string, encoding2)
        # Replace russian e at the beginning of a word
        if encoding2 == "Cyrillic (Russian)":
            string = self.replace_russian_e_at_beginning(string)
        # Change anusvara if the checkBox is checked
        if self.ui.checkBox.isChecked():
            string = self.change_anusvara_type(string)
        if encoding1 == "HK":
            string = string.lower()
        # If any encoding is Ukrainian then follow the loops below
        if encoding1 == "Cyrillic (Ukrainian)" or encoding2 == "Cyrillic (Ukrainian)":
            string = self.convert_ukrainian(string, encoding1, encoding2)
        self.ui.textBrowser.setPlainText(string)

    def convert_ukrainian(self, string, encoding1, encoding2):
        # 'temp_symbols' is a temporary list of all the symbols in our converted text
        temp_symbols = self.convert_aspirated_cyrillic_properly(string)
        # This is only for Ukrainian into Russian (change dga into dha)
        if encoding1 == "Cyrillic (Ukrainian)" and encoding2 == "Cyrillic (Russian)":
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

    def replace_russian_e_from_ukrainian(self, string, encoding2):
        if encoding2 == "Cyrillic (Ukrainian)":
            string = string.replace("э", "е")
            string = string.replace("Э", "Е")
        else:
            string = string.replace("э", "e")
            string = string.replace("Э", "E")
        return string

    def change_ga_to_ha(self, temp_symbols: list) -> list:
        """Change гг to гх in cyrillic"""
        for i in range(len(temp_symbols) - 1):
            if temp_symbols[i].lower() in self.ASPIRATED_CYRILLIC and temp_symbols[i + 1] == "г":
                temp_symbols[i + 1] = "х"
            elif temp_symbols[i].lower() in self.ASPIRATED_CYRILLIC and temp_symbols[i + 1] == "Г":
                temp_symbols[i + 1] = "Х"
        return temp_symbols

    def convert_aspirated_cyrillic_properly(self, string: str) -> list:
        """Fix wrong conversions that happen due to overlapping symbols"""
        # 'temp_symbols' is a temporary list of all the symbols in our converted text
        # 'ASPIRATED_CYRILLIC' and 'ASPIRATED_ROMAN' are list of letters corresponding
        # to the aspirated consonants in Sanskrit (Cyrillic and Roman).
        temp_symbols = list(string)
        for i in range(len(temp_symbols) - 1):
            if temp_symbols[i].lower() in self.ASPIRATED_CYRILLIC and temp_symbols[i + 1] == "х":
                temp_symbols[i + 1] = "г"
            elif temp_symbols[i].lower() in self.ASPIRATED_CYRILLIC and temp_symbols[i + 1] == "Х":
                temp_symbols[i + 1] = "Г"
            if temp_symbols[i].lower() in self.ASPIRATED_ROMAN and temp_symbols[i + 1] == "г":
                temp_symbols[i + 1] = "h"
            elif temp_symbols[i].lower() in self.ASPIRATED_ROMAN and temp_symbols[i + 1] == "Г":
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
        encoding1 = self.ui.comboBox.currentText()
        encoding2 = self.ui.comboBox_2.currentText()
        if encoding1 == encoding2:  # To save time for identical encodings
            self.ui.textBrowser.setPlainText(text)
        elif encoding2 == "HK":  # Peculiarities of the HK scheme, it uses only lowercase letters
            if encoding1 not in self.CYRILLIC_ENCODINGS and text.islower():
                self.convert(
                    text,
                    self.ROMAN_ENCODINGS[encoding1],
                    self.HK,
                    encoding1,
                    encoding2,
                )
            else:
                self.convert(
                    text.lower(),
                    self.ALL_ENCODINGS[encoding1],
                    self.HK_EXT,
                    encoding1,
                    encoding2,
                )
        # Simplify transliteration of the similar encodings that are based on Roman script
        elif encoding1 not in self.CYRILLIC_ENCODINGS and encoding2 not in self.CYRILLIC_ENCODINGS:
            self.convert(
                text,
                self.ROMAN_ENCODINGS[encoding1],
                self.ROMAN_ENCODINGS[encoding2],
                encoding1,
                encoding2,
            )
        # For transliterating between Roman and Cyrillic transliterations
        else:
            self.convert(
                text,
                self.ALL_ENCODINGS[encoding1],
                self.ALL_ENCODINGS[encoding2],
                encoding1,
                encoding2,
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
        self.settings.setValue("encoding1", self.ui.comboBox.currentText())
        self.settings.setValue("encoding2", self.ui.comboBox_2.currentText())
        self.settings.setValue("Use m", self.ui.checkBox.isChecked())
        self.settings.setValue("WindowSize", self.size())
        self.settings.setValue("Position", self.pos())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = SansConverter()
    sys.exit(app.exec_())
