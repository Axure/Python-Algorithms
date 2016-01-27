import types
from types import *
from typings import type_check
from difflib import SequenceMatcher

@type_check.type_checked
def word_similarity(word_1: str, word_2: str) -> float:
    s = SequenceMatcher(None, word_1, word_2) # An official implementation.
    return s.ratio()

if __name__ == '__main__':
    print(word_similarity('1235', '4565'))
