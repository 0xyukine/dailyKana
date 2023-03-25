from pathlib import Path

import random
import json

path = Path(__file__).parent

class RandomKana:
    #Load both kana text files into dictionaries on initialisation
    def __init__(self):
        with open(path / "../res/hiragana.txt") as f:
            self.hiragana = json.load(f)
        with open(path / "../res/katakana.txt") as f:
            self.katakana = json.load(f)

    def hira(self):
        kana, eng = random.choice(list(self.hiragana.items()))
        return (kana,eng)

    def kata(self):
        kana, eng = random.choice(list(self.katakana.items()))
        return (kana,eng)

    def kana(self):
        kana, eng = random.choice(list({**self.hiragana,**self.katakana}.items()))
        return (kana,eng)