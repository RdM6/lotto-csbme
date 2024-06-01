class statistik:
    def __init__(self, spiele, gewinnklasse1, gewinnklasse2, gewinnklasse3, gewinnklasse4, gewinnklasse5, gewinnklasse6, gewinnklasse7, gewinnklasse8, gewinnklasse9):
        self.spiele = spiele
        self.gewinnklasse1 = gewinnklasse1
        self.gewinnklasse2 = gewinnklasse2
        self.gewinnklasse3 = gewinnklasse3
        self.gewinnklasse4 = gewinnklasse4
        self.gewinnklasse5 = gewinnklasse5
        self.gewinnklasse6 = gewinnklasse6
        self.gewinnklasse7 = gewinnklasse7
        self.gewinnklasse8 = gewinnklasse8
        self.gewinnklasse9 = gewinnklasse9

    def auswertung(self, gewinnklasse):
        self.spiele += 1
        match gewinnklasse:
            case 1:
                self.gewinnklasse1 += 1
            case 2:
                self.gewinnklasse2 += 1
            case 3:
                self.gewinnklasse3 += 1
            case 4:
                self.gewinnklasse4 += 1
            case 5:
                self.gewinnklasse5 += 1
            case 6:
                self.gewinnklasse6 += 1
            case 7:
                self.gewinnklasse7 += 1
            case 8:
                self.gewinnklasse8 += 1
            case 9:
                self.gewinnklasse9 += 1