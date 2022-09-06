import pytest
from office_word_count.text import Text


@pytest.mark.parametrize(
    ("text"),
    [
        ("\nsample\ntext\n"),
        ("\r\nsample\r\ntext\r\n"),
        ("\nsample\r\ntext\r\n\n"),
    ],
)
def test_text_no_break(text):
    _text = Text(text).no_break()
    assert ("\n" not in _text.value) is True
    assert ("\r\n" not in _text.value) is True
    assert _text.value == "sampletext"


@pytest.mark.parametrize(
    ("text"),
    [
        (" sample text "),
        ("　sample　text　"),
        ("\u3000sample\u3000text\u3000"),
        (" sample　text\u3000"),
    ],
)
def test_text_no_space(text):
    _text = Text(text).no_space()
    assert (" " not in _text.value) is True
    assert ("　" not in _text.value) is True
    assert ("\u3000" not in _text.value) is True
    assert _text.value == "sampletext"


@pytest.mark.parametrize(
    ("text"),
    [
        ("\nsample\ntext\n"),
        ("\r\nsample\r\ntext\r\n"),
        ("\nsample\r\ntext\r\n\n"),
    ],
)
def test_text_break2space(text):
    _text = Text(text).break2space()
    assert ("\n" not in _text.value) is True
    assert ("\r\n" not in _text.value) is True
    assert _text.value == " sample text "


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("あア亜Ａ", ""),
        ("abcABC", "abcABC"),
    ],
)
def test_text_no_asian(text, expected):
    _text = Text(text).no_asian()
    assert _text.value == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("sample text", 2),
        ("URL: http://www.example.com", 2),
    ],
)
def test_text_word_count(text, expected):
    _text = Text(text)
    assert _text.word_count == expected
