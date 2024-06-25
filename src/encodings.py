from enum import Enum

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

UKR = (
    "Ā", "Ī", "Ӯ", "Л̣", "Р̣̄", "Р̣", "Н̇", "Н̃", "Т̣", "Д̣", "Н̣", "Ш́", "Ш", "Х̣", "М̇", "А", "Б", "Ч",
    "Дж", "ДЖ", "Д", "Е", "Ґ", "Х", "І", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "В",
    "Й", "ā", "ī", "ӯ", "л̣", "р̣̄", "р̣", "ш́", "ш", "н̇", "н̃", "т̣", "д̣", "н̣", "х̣", "м̇", "а", "б",
    "ч", "дж", "д", "е", "ґ", "х", "і", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "в", "й"
)

RUS = (
    "Ā", "Ӣ", "Ӯ", "Л̣", "Р̣̄", "Р̣", "Н̇", "Н̃", "Т̣", "Д̣", "Н̣", "Ш́", "Ш", "Х̣", "М̇", "А", "Б", "Ч",
    "Дж", "ДЖ", "Д", "Е", "Г", "Х", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "В",
    "Й", "ā", "ӣ", "ӯ", "л̣", "р̣̄", "р̣", "ш́", "ш", "н̇", "н̃", "т̣", "д̣", "н̣", "х̣", "м̇", "а", "б",
    "ч", "дж", "д", "е", "г", "х", "и", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "в", "й"
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

# 'ASPIRATED_CYRILLIC' and 'ASPIRATED_ROMAN' are lists of letters corresponding
# to the aspirated consonants in Sanskrit (Cyrillic and Roman).
ASPIRATED_CYRILLIC = ("к", "ґ", "ч", "ж", "т̣", "д̣", "т", "д", "п", "б")
ASPIRATED_ROMAN = ("k", "g", "c", "j", "ṭ", "ḍ", "t", "d", "p", "b")


# ENUMS
class Encodings(Enum):
    UKR = "Cyrillic (Ukrainian)"
    RUS = "Cyrillic (Russian)"


# 'CYRILLIC_ENCODINGS' is the names of Cyrillic encodings
CYRILLIC_ENCODINGS = (Encodings.UKR, Encodings.RUS)
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
