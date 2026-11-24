from classes.dzwig import dzwig


class brama():
    def __init__(self):
        self.dzwig=dzwig(3)
        self.ciezarowka=None

    def wolna(self):
        return self.ciezarowka is None

    def zajac(self, c):
        self.ciezarowka = c

    def zwolnic(self):
        self.ciezarowka = None
        
    def szybkosc(self):
        return self.dzwig.jaka_szybkosc()

        # if self.ciezarowka:
        #     print("s=",self.dzwig.jaka_szybkosc())
        #     return self.dzwig.jaka_szybkosc()
        # return 0