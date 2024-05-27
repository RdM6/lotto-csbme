import random

class lottoSchein:
    def __init__(self, zahlen, superzahl : int):
        self.zahlen = [zahlen[0], zahlen[1], zahlen[2], zahlen[3], zahlen[4], zahlen[5]]
        self.superzahl = superzahl

    def create_random(self):
        lottozahlen = []
        lottozahlen.extend(range(1, 50))
        self.zahlen = random.sample(lottozahlen, 6)
        self.superzahl = random.randint(0, 9)