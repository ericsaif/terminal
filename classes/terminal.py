import okienko

class terminal():
    def __init__(self, pojemnosc_magazynu, liczba_okienek=60, liczba_bram=2):
        self.okienka = [okienko(liczba_bram, pojemnosc_magazynu/liczba_okienek) for _ in range(liczba_okienek)]
        self.kolejka_s = []
        self.kolejka_c=[]

    def przyjmij_statek_do_kolejki(self,statek):
        self.kolejka_s.append(statek)

    def przydzielenie_okienka_dla_statka(self):
        for okienko in self.okienka:
            if okienko.jest_wolne():
                statek = self.kolejka_s.pop()
                # to do wskaznika jakosci
                czas_oczekiwania = statek.zwroc_czas_oczekiwania()
                okienko.zajac(statek)
                
    def przydzielenie_bramy(self, ciezarowka):
        self.kolejka_c.append(ciezarowka)

    def zwieksz_czas_oczekiwania(self):
        list(lambda x : x.zwieksz_czas_oczekiwania(),map(self.kolejka_c))
        list(lambda x : x.zwieksz_czas_oczekiwania(),map(self.kolejka_s))

    # moze tu dodac liste statkow i liste ciezarowek, domyslnie puste
    def krok(self, statek=None):
        self.zwieksz_czas_oczekiwania()
        if statek:
            self.przyjmij_statek_do_kolejki(statek)
        self.przydzielenie_okienka_dla_statka()
        # przydzielenie_bramy dla ciezarowki
        for okienko in self.okienka:
            okienko.zabierz_kontenery_z_magazynu()
            okienko.rozladuj_statek()

    def statystyka(self):
        # return statystyka, wskazniki jakosci
        pass