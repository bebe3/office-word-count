from typing import Final

import regex

from .patterns import ASIANS, BREAKS, SPACES


class Text:
    def __init__(self, value: str):
        if value is None:
            raise ValueError("Text value must not be None.")

        self.value: Final[str] = value

    def __repr__(self) -> str:
        return f"Text(value='{self.value}')"

    def __add__(self, other):
        return Text(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value

    @property
    def char_count(self) -> int:
        return len(self.value)

    @property
    def word_count(self) -> int:
        return len([word for word in self._split_by_space() if word])

    def break2space(self):
        return Text(BREAKS.sub(" ", self.value))

    def no_break(self):
        return Text(BREAKS.sub("", self.value))

    def no_space(self):
        return Text(SPACES.sub("", self.value))

    def no_asian(self):
        return Text(ASIANS.sub("", self.value))

    def only_asian(self):
        return Text("".join(ASIANS.findall(self.value)))

    def _split_by_space(self):
        return regex.split(r"\s", self.value)
