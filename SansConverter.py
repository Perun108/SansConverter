# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore
from converter_generated import Ui_SansConverter
from about import Ui_Dialog2
from trans_help import Ui_Dialog


class SansConverter(QtWidgets.QMainWindow):
    """This is the main class with all the logic and connection between GUI parts and class methods"""
    settings = QtCore.QSettings("SansConverter", "Converter")
    balaram = ["ä", "é", "ü", "ÿ", "è", "å", "ñ", "ì", "ï", "ö", "ò", "ë", "ç", "ù",
               "à", "Ä", "É", "Ü", "Ÿ", "È", "Å", "Ñ", "Ì", "Ï", "Ö", "Ò", "Ë", "Ç", "Ù", "À"]
    iast = ["ā", "ī", "ū", "ḷ", "ṝ", "ṛ", "ṣ", "ṅ", "ñ", "ṭ", "ḍ", "ṇ", "ś", "ḥ",
            "ṁ", "Ā", "Ī", "Ū", "Ḷ", "Ṝ", "Ṛ", "Ṣ", "Ṅ", "Ñ", "Ṭ", "Ḍ", "Ṇ", "Ś", "Ḥ", "Ṁ"]
    hk = ["A", "I", "U", "lR", "RR", "R", "S", "G", "J", "T", "D", "N", "z", "H", "M",
          "A", "I", "U", "lR", "RR", "R", "S", "G", "J", "T", "D", "N", "z", "H", "M"]
    velthius = ['aa', 'ii', 'uu', '.l', '.rr', '.r', '.s', '"n', '~n', '.t', '.d', '.n', '"s', '.h',
                '.m', 'AA', 'II', 'UU', '.L', '.RR', '.R', '.S', '"N', '~N', '.T', '.D', '.N', '"S', '.H', '.M']

    rus = ["Ā", "Ӣ", "Ӯ", "Л̣", "Р̣̄", "Р̣", "Н̇", "Н̃", "Т̣", "Д̣", "Н̣", "Ш́", "Ш", "Х̣", "М̇", "А", "Б", "Ч", "Дж", "ДЖ", "Д", "Е", "Г", "Х", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "В",
           "Й", "ā", "ӣ", "ӯ", "л̣", "р̣̄", "р̣", "ш́", "ш", "н̇", "н̃", "т̣", "д̣", "н̣", "х̣", "м̇", "а", "б", "ч", "дж", "д", "е", "г", "х", "и", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "в", "й"]

    ukr = ["Ā", "Ī", "Ӯ", "Л̣", "Р̣̄", "Р̣", "Н̇", "Н̃", "Т̣", "Д̣", "Н̣", "Ш́", "Ш", "Х̣", "М̇", "А", "Б", "Ч", "Дж", "ДЖ", "Д", "Е", "Ґ", "Х", "І", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "В",
           "Й", "ā", "ī", "ӯ", "л̣", "р̣̄", "р̣", "ш́", "ш", "н̇", "н̃", "т̣", "д̣", "н̣", "х̣", "м̇", "а", "б", "ч", "дж", "д", "е", "ґ", "х", "і", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "в", "й"]

    balaram_ext = ["Ä", "É", "Ü", "Ÿ", "È", "Å", "Ì", "Ï", "Ö", "Ò", "Ë", "Ç", "Ñ", "Ù", "À", "A", "B", "C", "J", "J", "D", "E", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U",
                   "V", "Y", "ä", "é", "ü", "ÿ", "è", "å", "ç", "ñ", "ì", "ï", "ö", "ò", "ë", "ù", "à", "a", "b", "c", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y"]

    iast_ext = ["Ā", "Ī", "Ū", "Ḷ", "Ṝ", "Ṛ", "Ṅ", "Ñ", "Ṭ", "Ḍ", "Ṇ", "Ś", "Ṣ", "Ḥ", "Ṁ", "A", "B", "C", "J", "J", "D", "E", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U",
                "V", "Y", "ā", "ī", "ū", "ḷ", "ṝ", "ṛ", "ś", "ṣ", "ṅ", "ñ", "ṭ", "ḍ", "ṇ", "ḥ", "ṁ", "a", "b", "c", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y"]

    hk_ext = ["A", "I", "U", "lR", "RR", "R", "G", "J", "T", "D", "N", "z", "S", "H", "M", "a", "b", "c", "j", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v",
              "y", "A", "I", "U", "lR", "RR", "R", "z", "S", "G", "J", "T", "D", "N", "H", "M", "a", "b", "c", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y"]

    velthius_ext = ['AA', 'II', 'UU', '.L', '.RR', '.R', '"N', '~N', '.T', '.D', '.N', '"S', '.S', '.H', '.M', "A", "B", "C", "J", "J", "D", "E", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U",
                    "V", "Y", 'aa', 'ii', 'uu', '.l', '.rr', '.r', '"s', '.s', '"n', '~n', '.t', '.d', '.n', '.h', '.m', "a", "b", "c", "j", "d", "e", "g", "h", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y"]
    # 'ext' is the names of Cyrillic encodings
    # 'roman_encodings' is the names of Roman encodings
    # 'all_encodings_names' is the names of full versions of both Roman and Cyrillic encodings
    cyrillic_encodings = ["Cyrillic (Russian)", "Cyrillic (Ukrainian)"]
    roman_encodings = {"Balaram": balaram, "IAST": iast,
                 "HK": hk, "Velthius": velthius}
    all_encodings = {"Balaram": balaram_ext, "IAST": iast_ext, "HK": hk_ext,
                     "Velthius": velthius_ext, "Cyrillic (Russian)": rus, "Cyrillic (Ukrainian)": ukr}
    
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

    def convert(self, string, list1, list2, encoding1, encoding2):
        """
        This is the main method which converts between encodings
        It would be great to refactor it, but no time to do it now,
        plus this is the single method that transforms and outputs
        the target text, so need to figure out how to refactor it keeping this in mind
        Args:
        text (string): input text to convert into another encoding
        list1 (list): list with all symbols of the original encoding
        (each in its own place, place matters!)
        list2 (list): list with all corresponding symbols of the target encoding
        (each in its own respective place, place matters!)
        encoding1 (string): Name of the original encoding
        encoding2 (string): Name of the target encoding
        """
        for j in range(len(list1)):
            if list1[j] in string:
                string = string.replace(list1[j], list2[j])
        
        # Set proper case for 'Дж'
        if "Дж" in string:
            string = self.convert_j_properly(string)
        # Replace russian e when converting from Ukrainian
        if encoding1 == "Cyrillic (Russian)" and encoding2 != "Cyrillic (Russian)":
            if encoding2 == "Cyrillic (Ukrainian)":
                string = string.replace("э", "е")
                string = string.replace("Э", "Е")
            else:
                string = string.replace("э", "e")
                string = string.replace("Э", "E")
        # Replace russian e at the beginning of a word
        if encoding2 == "Cyrillic (Russian)":
            string = self.replace_russian_e_at_start(string)
        # Change anusvara if the checkBox is checked
        if self.ui.checkBox.isChecked() and ("ṁ" in string or "Ṁ" in string):
            string = string.replace("ṁ", "ṃ")
            string = string.replace("Ṁ", "Ṃ")
        elif self.ui.checkBox.isChecked() and ("м̇" in string or "М̇" in string):
            string = string.replace("м̇", "м̣")
            string = string.replace("М̇", "М̣")
        if encoding1 == "HK":
            string = string.lower()
        # Check if any encoding is Ukrainian
        # if yes then follow the loops below
        if (encoding1 == "Cyrillic (Ukrainian)" or encoding2 == "Cyrillic (Ukrainian)"):
            # 's' is a temporary list of all the symbols in our converted text
            # 'asp_cy' and 'asp_en' are list of letters corresponding to the aspirated
            # consonants in Sanskrit (Cyrillic and Roman).
            s = list(string)
            asp_cy = ["к", "ґ", "ч", "ж", "т̣", "д̣", "т", "д", "п", "б"]
            asp_en = ["k", "g", "c", "j", "ṭ", "ḍ", "t", "d", "p", "b"]
            for i in range(len(s)-1):
                if s[i].lower() in asp_cy and s[i+1] == "х":
                    s[i+1] = "г"
                elif s[i].lower() in asp_cy and s[i+1] == "Х":
                    s[i+1] = "Г"
                if s[i].lower() in asp_en and s[i+1] == "г":
                    s[i+1] = "h"
                elif s[i].lower() in asp_en and s[i+1] == "Г":
                    s[i+1] = "H"
            # This is only for Ukrainian into Russian (change dga into dha)
            if (encoding1 == "Cyrillic (Ukrainian)" and encoding2 == "Cyrillic (Russian)"):
                for i in range(len(s)-1):
                    if s[i].lower() in asp_cy and s[i+1] == "г":
                        s[i+1] = "х"
                    elif s[i].lower() in asp_cy and s[i+1] == "Г":
                        s[i+1] = "Х"
            # 'x' is the joined list 's' (original converted text
            # but now with all necessary transormations)
            x = "".join(s)
            self.ui.textBrowser.setPlainText(x)
        else:
            self.ui.textBrowser.setPlainText(string)

    def replace_russian_e_at_start(self, string):
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

    def convert_j_properly(self, string):
        try:
            position = 0
            while string != "Дж" and position != -1:
                if string[position:].startswith("Дж") and string[position + 2].isupper():
                    string = string[:position] + "ДЖ" + string[position+2:]
                position = string.find("Дж", position+1)
        except IndexError:
            string = string[:-1] + "Ж"
        return string

    def pressed(self):
        """
        This is a method which selects and sends arguments to the convert method
        The first 4 lists are short lists with only those Roman letters that have diacritical marks
        They are used for converting between two encodings that are based on Roman script
        Other lists (rus, ukr, gaura_times and the rest with '_ext' are long lists with *all* symbols
        of the Roman/Cyrillic alphabet in both uppercase and lowercase)
        """
        text = self.ui.textEdit.toPlainText()
        encoding1 = self.ui.comboBox.currentText()
        encoding2 = self.ui.comboBox_2.currentText()
        if encoding1 == encoding2:  # To save time for identical encodings
            self.ui.textBrowser.setPlainText(text)
        elif encoding2 == "HK":  # Peculiarities of the HK scheme, it uses only lowercase letters
            if encoding1 not in self.cyrillic_encodings and text.islower():
                self.convert(
                    text, self.roman_encodings[encoding1], self.hk, encoding1, encoding2)
            else:
                self.convert(
                    text.lower(), self.all_encodings_names[encoding1], self.hk_ext, encoding1, encoding2)
        # Simplify transliteration of the similar encodings that are based on Roman script
        elif encoding1 not in self.cyrillic_encodings and encoding2 not in self.cyrillic_encodings:
            self.convert(text, self.roman_encodings[encoding1],
                         self.roman_encodings[encoding2], encoding1, encoding2)
        # For transliterating between Roman and Cyrillic transliterations
        else:
            self.convert(
                text, self.all_encodings_names[encoding1], self.all_encodings_names[encoding2], encoding1, encoding2)

    def copy_converted(self):
        """
        Copies converted text from the output window when the 'Copy' button is pressed
        """
        self.ui.textBrowser.selectAll()
        self.ui.textBrowser.copy()

    def swap_encodings(self):
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

    def closeEvent(self, event):
        """
        Remembers settings and quits the program
        """
        self.settings.setValue("encoding1", self.ui.comboBox.currentText())
        self.settings.setValue("encoding2", self.ui.comboBox_2.currentText())
        self.settings.setValue("Use m", self.ui.checkBox.isChecked())
        self.settings.setValue("WindowSize", self.size())
        self.settings.setValue("Position", self.pos())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = SansConverter()
    sys.exit(app.exec_())
