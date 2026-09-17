import re
from collections import Counter

class TextAnalyzer:
    def __init__(self, text: str):
        self.cleaned_words = self._preprocess(text)

    def _preprocess(self, text: str) -> list[str]:
        lowered = text.lower()
        return re.findall(r"\b[a-z]{2,}\b", lowered)

    def get_top_words(self, n: int = 3) -> list[tuple[str, int]]:
        counter = Counter(self.cleaned_words)
        return counter.most_common(n)

sample_text = """
Python is dynamic. Python is readable and powerful.
Learning python with small projects is the best practice!
"""

analyzer = TextAnalyzer(sample_text)
print("총 단어 수:", len(analyzer.cleaned_words))
print("최빈출 단어 Top 3:")
for word, count in analyzer.get_top_words(3):
    print(f" - {word}: {count}회")