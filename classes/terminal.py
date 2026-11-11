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
            if okienko.sprawdz():
                statek = self.kolejka_s.pop()
                okienko.zajac(statek)
                
    def przydzielenie_bramy(self, ciezarowka):
        self.kolejka_c.append(ciezarowka)

    def krok(self):
        for okienko in self.okienka:
            # przydzielenie_bramy
            okienko.zabierz_kontenery_z_magazynu()
            okienko.rozladuj_statek()