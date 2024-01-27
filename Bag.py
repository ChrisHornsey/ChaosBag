import random

class ChaosBag:
    def __init__(self, tokens):
        self.contents = tokens

    def drawToken(self):
        return random.choice(self.contents)
