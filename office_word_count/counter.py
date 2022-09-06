from typing import Final

from .statistics import Statistics
from .text import Text


class Counter:
    def __init__(self, text: str):
        self.text: Final[Text] = Text(text)

    def count(self) -> Statistics:
        return Statistics(
            words=self.count_words(),
            characters_no_space=self.count_characters_no_space(),
            characters_with_space=self.count_characters_with_space(),
            non_asian_words=self.count_non_asian_words(),
            asian_characters=self.count_asian_characters(),
        )

    def count_words(self) -> int:
        return self.count_non_asian_words() + self.count_asian_characters()

    def count_characters_no_space(self) -> int:
        text_no_space = self.text.no_space()
        return text_no_space.char_count

    def count_characters_with_space(self) -> int:
        text_no_break = self.text.no_break()
        return text_no_break.char_count

    def count_non_asian_words(self) -> int:
        text_no_break = self.text.break2space()
        text_no_asian = text_no_break.no_asian()
        return text_no_asian.word_count

    def count_asian_characters(self) -> int:
        text_no_space = self.text.no_space()
        text_asian = text_no_space.only_asian()
        return text_asian.char_count
