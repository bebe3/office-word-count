from dataclasses import dataclass


@dataclass(frozen=True)
class Statistics:
    words: int
    characters_no_space: int
    characters_with_space: int
    non_asian_words: int
    asian_characters: int
