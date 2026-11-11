from classes import brama, dzwig


class okienko():
    def __init__(self,liczba_bram,pojemnosc_magazynu):
        self.wolne=True
        self.dzwigi = [dzwig(3) for _ in range(3)]
        self.bramy = [brama() for _ in range(liczba_bram)]
        self.maks_pojemnosc_magazynu = pojemnosc_magazynu
        self.liczba_kontenerow_w_magazynie = pojemnosc_magazynu
        self.statek=None
    def zwolnic(self):
        self.wolne = True
        self.statek=None
    def zajac(self,statek):
        self.wolne = False
        self.statek = statek
    def sprawdz(self):
        return self.wolne
    def laczna_szybkosc_dzwigow(self):
        sum=0
        for dzwig in self.dzwigi:
            sum+=dzwig.jaka_szybkosc()
        return sum
    def zabierz_kontenery_z_magazynu(self):
        if self.liczba_kontenerow_w_magazynie <= 0:
            return
        szybkosc = 0
        for brama in self.bramy:
            szybkosc+=brama.szybkosc()
        self.liczba_kontenerow_w_magazynie-=szybkosc
    def rozladuj_statek(self):
        statek = self.statek
        szybkosc = self.laczna_szybkosc_dzwigow()
        maks_pojemnosc=self.liczba_wolnych_miejsc()
        liczba_kontenerow = statek.rozladuj_kontener(min(szybkosc, maks_pojemnosc))
        self.zamagazynuj_kontenery(liczba_kontenerow)
    def liczba_wolnych_miejsc(self):
        return self.maks_pojemnosc_magazynu - self.liczba_kontenerow_w_magazynie
    def zamagazynuj_kontenery(self, liczba):
            self.liczba_kontenerow_w_magazynie+=liczba
