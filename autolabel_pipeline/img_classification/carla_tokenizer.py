import re
import string
from collections import Counter

class CarlaTokenizer:
    def __init__(self, vocab=None, lower_case=True, special_tokens=None):
        self.lower_case = lower_case
        self.special_tokens = special_tokens if special_tokens else {
            "<UNK>": 0, # unknown token
            "<PAD>": 1, # padding token
            "<SOS>": 2, # start of sequence token
            "<EOS>": 3, # end of sequence token
        }

        self.vocab = vocab if vocab else self.special_tokens.copy()
        self.int_to_str = {i: s for s, i in self.vocab.items()}
        self.str_to_int = self.vocab
    