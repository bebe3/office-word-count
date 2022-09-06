# Office Word Count


## Installation
```
pip install office-word-count
```

## Example
```
from office_word_count import Counter

text = "This is a sample text."
counter = Counter(text)
counter.count()
```

```
Statistics(words=5, characters_no_space=18, characters_with_space=22, non_asian_words=5, asian_characters=0)
```
