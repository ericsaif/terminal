

from classes.brama import brama
from classes.dzwig import dzwig


class okienko():
    def __init__(self,liczba_bram,pojemnosc_magazynu):
        self.dzwigi = [dzwig(3) for _ in range(3)]
        self.bramy = [brama() for _ in range(liczba_bram)]
        self.maks_pojemnosc_magazynu = pojemnosc_magazynu
        self.liczba_kontenerow_w_magazynie = 0
        self.statek=None
        self.typ="A"

    def zwolnic(self):
        self.statek=None

    # zajać
    def zajac(self,statek):
        self.statek = statek

    def jest_wolne(self):
        return self.statek is None

    def wolne_bramy(self):
        return [b for b in self.bramy if b.wolna()]
    
    def laczna_szybkosc_dzwigow(self):
        sum=0
        for dzwig in self.dzwigi:
            sum+=dzwig.jaka_szybkosc()
        return sum
    
    def zabierz_kontenery_z_magazynu(self):
        szybkosc = 0
        for brama in self.bramy:
            szybkosc+=brama.szybkosc()
        if self.liczba_kontenerow_w_magazynie <= szybkosc:
            return self.liczba_kontenerow_w_magazynie
        
        self.liczba_kontenerow_w_magazynie-=szybkosc
        return szybkosc

    def rozladuj_statek(self):
        statek = self.statek

        if statek is None:
            return True
        
        szybkosc = self.laczna_szybkosc_dzwigow()
        maks_pojemnosc=self.liczba_wolnych_miejsc()
        
        liczba_kontenerow, pusty = statek.rozladuj_kontener(min(szybkosc, maks_pojemnosc))
        self.zamagazynuj_kontenery(liczba_kontenerow)

        if pusty:
            self.zwolnic()
            return True
        return False

    def liczba_wolnych_miejsc(self):
        return self.maks_pojemnosc_magazynu - self.liczba_kontenerow_w_magazynie
    
    def zamagazynuj_kontenery(self, liczba):
        self.liczba_kontenerow_w_magazynie+=liczba
