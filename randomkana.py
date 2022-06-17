import json
import random

class RandomKana:
    def __init__(self):
        with open("hiragana.txt") as f:
            self.hiragana = json.load(f)

    def random(self):
        kana, eng = random.choice(list(self.hiragana.items()))
        return (kana, eng)