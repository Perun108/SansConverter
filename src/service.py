from encoding_mappings import (
    ASPIRATED_CYRILLIC_LETTERS,
    ASPIRATED_ROMAN_LETTERS,
    Encodings,
)


def convert(
    string: str,
    start_symbols_list: tuple,
    end_symbols_list: tuple,
    input_encoding: str,
    output_encoding: str,
    use_anusvara: bool,
) -> str:
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
        use_anusvara (bool): To use the dot above or under m
    """

    for i, item in enumerate(start_symbols_list):
        if item in string:
            string = string.replace(item, end_symbols_list[i])

    # Set proper case for 'Дж'
    if "Дж" in string:
        string = _convert_j_properly(string)

    # Replace russian e when converting from Ukrainian
    if input_encoding == Encodings.RUS.value and output_encoding != Encodings.RUS.value:
        string = _replace_russian_e_from_ukrainian(string, output_encoding)

    # Replace russian e at the beginning of a word
    if output_encoding == Encodings.RUS.value:
        string = _replace_russian_e_at_beginning(string)

    # Change anusvara if the checkBox is checked
    if use_anusvara:
        string = _change_anusvara_type(string)

    if input_encoding == Encodings.HK.value:
        string = string.lower()

    # If any encoding is Ukrainian then follow the loops below
    if input_encoding == Encodings.UKR.value or output_encoding == Encodings.UKR.value:
        string = _convert_ukrainian(string, input_encoding, output_encoding)

    return string


def _convert_ukrainian(string, input_encoding, output_encoding):
    # 'temp_symbols' is a temporary list of all the symbols in our converted text
    temp_symbols = _convert_aspirated_cyrillic_properly(string)
    # This is only for Ukrainian into Russian (change dga into dha)
    if input_encoding == Encodings.UKR.value and output_encoding == Encodings.RUS.value:
        temp_symbols = _change_ga_to_ha(temp_symbols)
        # 'x' is the joined list 's' (original converted text
        # but now with all necessary transormations)
    converted_text = "".join(temp_symbols)
    return converted_text


def _change_anusvara_type(string):
    if "ṁ" in string:
        string = string.replace("ṁ", "ṃ")
    elif "Ṁ" in string:
        string = string.replace("Ṁ", "Ṃ")
    elif "м̇" in string:
        string = string.replace("м̇", "м̣")
    elif "М̇" in string:
        string = string.replace("М̇", "М̣")
    return string


def _replace_russian_e_from_ukrainian(string, output_encoding):
    if output_encoding == Encodings.UKR.value:
        string = string.replace("э", "е")
        string = string.replace("Э", "Е")
    else:
        string = string.replace("э", "e")
        string = string.replace("Э", "E")
    return string


def _change_ga_to_ha(temp_symbols: list) -> list:
    """Change гг to гх in cyrillic"""
    for i in range(len(temp_symbols) - 1):
        if temp_symbols[i].lower() in ASPIRATED_CYRILLIC_LETTERS and temp_symbols[i + 1] == "г":
            temp_symbols[i + 1] = "х"
        elif temp_symbols[i].lower() in ASPIRATED_CYRILLIC_LETTERS and temp_symbols[i + 1] == "Г":
            temp_symbols[i + 1] = "Х"
    return temp_symbols


def _convert_aspirated_cyrillic_properly(string: str) -> list:
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


def _replace_russian_e_at_beginning(string: str) -> str:
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


def _convert_j_properly(string: str) -> str:
    """Converts j to  cyrillic дж"""
    try:
        position = 0
        # Check if the next character after "Дж" is uppercase
        while string != "Дж" and position != -1:
            if string[position:].startswith("Дж") and string[position + 2].isupper():
                string = string[:position] + "ДЖ" + string[position + 2 :]
            # Move past the current "Дж" to find the next occurrence
            position = string.find("Дж", position + 1)
    except IndexError:
        string = string[:-1] + "Ж"
    return string
