import random
from game.symbols import SYMBOLS

class Reel:
    def spin_reels(self):
        return [random.choice(SYMBOLS) for _ in range(3)]
