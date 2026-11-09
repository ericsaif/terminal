from classes import dzwig


class okienko():
    def __init__(self):
        self.wolne=True
        self.dzwigi = [dzwig(3) for _ in range(3)]
        self.statek=None
    def zwolnic(self):
        self.wolne = True
        self.statek=None
    def zajac(self,statek):
        self.wolne = False
        self.statel = statek
    def sprawdz(self):
        return self.wolne
    def laczna_szybkosc_dzwigow(self):
        sum=0
        for dzwig in self.dzwigi:
            sum+=dzwig.jaka_szybkosc()
        return sum
    def rozladuj_statek(self):
        statek = self.statek
        szybkosc = self.laczna_szybkosc_dzwigow()
        # statek.rozladuj_kontenery(liczba_kontenerow)