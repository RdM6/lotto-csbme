import random
import statistik

class spiel:

    def __init__(self, zahlen, superzahl, lottoscheine, gewinnklasse):
        self.zahlen = [zahlen[0], zahlen[1], zahlen[2], zahlen[3], zahlen[4], zahlen[5]]
        self.superzahl = superzahl
        self.lottoscheine = []
        self.gewinnklasse = gewinnklasse

    def create_winning_numbers(self):
        alle_lottozahlen = []
        alle_lottozahlen.extend(range(1, 50))
        self.zahlen = random.sample(alle_lottozahlen, 6)
        self.superzahl = random.randint(0, 9)

    def addLottoSchein(self, lottoSchein):
        self.lottoScheine.append((lottoSchein.zahlen, lottoSchein.superzahl))

    def check_for_win(self):
        for lottoSchein in self.lottoscheine:
            übereinstimmungen = len(set(self.zahlen).intersection(set(lottoSchein.zahlen)))
            if lottoSchein.superzahl == self.superzahl:
                match übereinstimmungen:
                    case 6:
                        gewinnklasse = 1
                    case 5: 
                        gewinnklasse = 3
                    case 4:
                        gewinnklasse = 5
                    case 3:
                        gewinnklasse = 7
                    case 2:
                        gewinnklasse = 9
                    case _:
                        gewinnklasse = "verloren"
            else:
                match übereinstimmungen:
                    case 6:
                        gewinnklasse = 2
                    case 5:
                        gewinnklasse = 4
                    case 4:
                        gewinnklasse = 6
                    case 3:
                        gewinnklasse = 8
                    case _:
                        gewinnklasse = "verloren"
            statistik.statistik.auswertung(gewinnklasse)