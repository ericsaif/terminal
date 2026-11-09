from classes import brama
import okienko


class terminal():
    def __init__(self, pojemnosc_magazynu, liczba_okienek=60, liczba_bram=30):
        self.okienka = [okienko() for _ in range(liczba_okienek)]
        self.bramy = [brama() for _ in range(liczba_bram)]
        self.pojemnosc_magazynu = pojemnosc_magazynu
    def przydzielenie_okienka_dla_statka(self):
        for okienko in self.okienka:
            if okienko.sprawdz():
                okienko.zajac()