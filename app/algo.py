__all__ = ["SpellingBeeAlgorithm"]

from collections import defaultdict
from itertools import combinations
from typing import Mapping, Tuple, List

import pandas as pd


class SpellingBeeAlgorithm:
    def __init__(self):
        word_df = pd.read_csv("https://raw.githubusercontent.com/garyongguanjie/entrie/main/unigram_freq.csv")
        word_list = word_df.word.dropna().tolist()
        word_counts = word_df.set_index("word")["count"].to_dict()

        letters_to_words = defaultdict(list)
        for i in word_list:
            letters_to_words[tuple(sorted(set(i.lower())))].append(i)
        letters_to_words = dict(letters_to_words)

        self._letters_to_words: Mapping[Tuple[str, ...]] = letters_to_words
        self._word_counts: Mapping[str, int] = word_counts

    @staticmethod
    def _get_combos(letters: str, center_letter: str) -> List[Tuple[str, ...]]:
        list_of_letters = sorted(set(list(letters.lower()) + [center_letter.lower()]))
        j: Tuple[str, ...]
        combinations_of_letters = [j for i in range(1, len(list_of_letters) + 1) for j in
                                   combinations(list_of_letters, i)]
        combos_with_center = [i for i in combinations_of_letters if center_letter.lower() in i]
        return combos_with_center

    def solve_for_words(self, letters: str, center_letter: str) -> List[str]:
        matching_words = [i for c in self._get_combos(letters, center_letter) for i in
                          (self._letters_to_words[c] if c in self._letters_to_words else [])]
        matching_words_4 = [i for i in matching_words if len(i) > 3]

        # Sort by frequency of word usage
        return sorted(matching_words_4,
                      key=lambda i: self._word_counts[i] if i in self._word_counts else 0,
                      reverse=True)
