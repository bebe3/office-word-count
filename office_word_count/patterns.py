import regex

SPACES = regex.compile(r"\s+")
BREAKS = regex.compile(r"[\r\n]+")

ASIAN_PATTERN = "".join(
    (
        r"、。！＂＃＄％＆＇（）＊＋，ー－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～｟｠￠￡￢￣￤￥￦",
        r"０-９ａ-ｚＡ-Ｚ",
        r"\p{HAN}",
        r"\p{HIRAGANA}",
        r"\p{KATAKANA}",
        r"\p{HANGUL}",
        r"\p{CJKRADICALSSUPPLEMENT}",
        r"\p{CJKSYMBOLSANDPUNCTUATION}",
        r"\p{CJKSTROKES}",
        r"\p{ENCLOSEDCJKLETTERSANDMONTHS}",
        r"\p{CJKCOMPATIBILITY}",
        r"\p{CJKUNIFIEDIDEOGRAPHSEXTENSIONA}",
        r"\p{CJKUNIFIEDIDEOGRAPHSEXTENSIONB}",
        r"\p{CJKUNIFIEDIDEOGRAPHSEXTENSIONC}",
        r"\p{CJKUNIFIEDIDEOGRAPHSEXTENSIOND}",
        r"\p{CJKUNIFIEDIDEOGRAPHSEXTENSIONE}",
        r"\p{CJKUNIFIEDIDEOGRAPHSEXTENSIONF}",
        r"\p{CJKUNIFIEDIDEOGRAPHSEXTENSIONG}",
        r"\p{CJKUNIFIEDIDEOGRAPHS}",
        r"\p{CJKCOMPATIBILITYFORMS}",
        r"\p{CJKCOMPATIBILITYIDEOGRAPHS}",
        r"\p{CJKCOMPATIBILITYIDEOGRAPHSSUPPLEMENT}",
    )
)

ASIANS = regex.compile(rf"[{ASIAN_PATTERN}]+")
