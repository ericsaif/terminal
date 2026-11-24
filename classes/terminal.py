import random

from classes.brama import brama
from classes.ciezarowka import element_kolejki
from classes.statek import statek
from classes.okienko import okienko

class terminal():
    def __init__(self, pojemnosc_magazynu, liczba_okienek=60, liczba_bram=2):
        self.okienka = [okienko(liczba_bram, int(pojemnosc_magazynu/liczba_okienek)) for _ in range(liczba_okienek)]
        self.kolejka_s = []
        self.kolejka_c=[]

        self.brama_pociagu = brama()
        self.okno_statku_T = [okienko(liczba_bram, int(pojemnosc_magazynu/liczba_okienek)) for _ in range(liczba_okienek)]

        self.obsluzone_statki=0
        self.wyslane_kontenery=0

        self.przyjete_statki=0

    def przyjmij_statek_do_kolejki(self,statek):
        self.przyjete_statki+=1
        self.kolejka_s.append(statek)

    def przyjmij_ciezarowke_do_kolejki(self,ciezarowka):
        self.kolejka_c.append(ciezarowka)

    def przydzielenie_okienek_i_bram(self):
        for okienko in self.okienka:
            if not self.kolejka_s:
                break
            if okienko.jest_wolne():
                statek = self.kolejka_s.pop(0)

                # to do wskaznika jakosci
                czas_oczekiwania = statek.zwroc_czas_oczekiwania()
                okienko.zajac(statek)
            
            for brama in okienko.wolne_bramy():
                if not self.kolejka_c:
                    break
                ciezarowka = self.kolejka_c.pop(0)
                brama.zajac(ciezarowka)
                czas_oczekiwania_c = ciezarowka.zwroc_czas_oczekiwania()
                
    def przydzielenie_bramy(self, ciezarowka):
        self.kolejka_c.append(ciezarowka)

    def zwieksz_czas_oczekiwania(self):
        list(map(lambda x : x.zwieksz_czas_oczekiwania(),self.kolejka_c))
        list(map(lambda x : x.zwieksz_czas_oczekiwania(),self.kolejka_s))

    def rand_gaus(self, mu, s):
        return int(random.gauss(mu,s))

    # moga pojawiac sie statki typu T - puste statki, które zabierają kontenery z magazynu
    def pojawienie_sie_statkow(self):
        return self.rand_gaus(5,1.67)
    
    def pojawienie_sie_ciezarowek(self):
        return self.rand_gaus(10,3.33)

    def pojawienie_sie_pociagow(self):
        return self.rand_gaus(10,3.33)


    # moze tu dodac liste statkow i liste ciezarowek, domyslnie puste
    def krok(self):
        self.zwieksz_czas_oczekiwania()

        statki = self.pojawienie_sie_statkow()
        ciezarowki = self.pojawienie_sie_ciezarowek()

        for _ in range(statki):
            self.przyjmij_statek_do_kolejki(statek())

        for _ in range(ciezarowki):
            self.przyjmij_ciezarowke_do_kolejki(element_kolejki())
        
        # przydzielenie_bramy dla ciezarowki
        self.przydzielenie_okienek_i_bram()

        for okienko in self.okienka:
            wolne=False
            kontenery = okienko.zabierz_kontenery_z_magazynu()
            if not okienko.jest_wolne():
                wolne=okienko.rozladuj_statek()
                if wolne:
                    self.obsluzone_statki+=1
            self.wyslane_kontenery+=kontenery

    def statystyka(self):
        return self.obsluzone_statki, self.wyslane_kontenery, self.przyjete_statki