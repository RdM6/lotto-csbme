import random

class spiel:

    def __init__(self, zahlen, superzahl, lottoscheine):
        self.zahlen = [zahlen[0], zahlen[1], zahlen[2], zahlen[3], zahlen[4], zahlen[5]]
        self.superzahl = superzahl
        self.lottoscheine = []

    def create_winning_numbers(self):
        alle_lottozahlen = []
        alle_lottozahlen.extend(range(1, 50))
        self.zahlen = random.sample(alle_lottozahlen, 6)
        self.superzahl = random.randint(0, 9)

    def addLottoSchein(self, lottoSchein):
        self.lottoScheine.append((lottoSchein.zahlen, lottoSchein.superzahl))

    def check_for_win(self):
        for lottoSchein in self.lottoscheine:
            if lottoSchein.zahlen == self.zahlen and lottoSchein.superzahl == self.superzahl:
                return True
        return False