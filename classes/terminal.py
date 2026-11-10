from classes import brama
import okienko


class terminal():
    def __init__(self, pojemnosc_magazynu, liczba_okienek=60, liczba_bram=30):
        self.okienka = [okienko() for _ in range(liczba_okienek)]
        
    def przydzielenie_okienka_dla_statka(self,statek):
        for okienko in self.okienka:
            if okienko.sprawdz():
                okienko.zajac(statek)
    def rozladuj_statki(self):
        if self.sprawdz_wolne_miejsca():
            for okienko in self.okienka:
                if self.sprawdz_wolne_miejsca():
                    okienko.rozladuj_statek()
    def sprawdz_wolne_miejsca(self):
        return self.wolne_miejsca_w_magazynie>0
    def rozladuj_magazyn(self):
        pass