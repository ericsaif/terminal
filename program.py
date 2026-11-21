import time

from classes.terminal import terminal
MAKS_POJEMNOSC_MAGAZYNU = 1200000  # [0-12000]
MAKS_LICZBA_OKIENEK_S = 60  # [0-60]
MAKS_LICZBA_BRAM = 2  # [0-30]
LICZBA_DZWIGOW_PRZY_KAZDYM_OKIENKU_S = 3  # [0-3]
LICZBA_DZWIGOW_PRZY_KAZDEJ_BRAMIE = 1  # [0-1]

# Zmienne
LICZBA_CIEZAROWEK = 100  # [0-100]
PREDKOSC_ROZLADOWANIA_KONTENEROW = 2  # [1-2]
PREDKOSC_ZALADOWANIA_KONTENEROW = 2  # [1-2]
LICZBA_WOLNYCH_OKIENEK_S = MAKS_LICZBA_OKIENEK_S  # [0-60]
LICZBA_WOLNYCH_BRAM = MAKS_LICZBA_BRAM  # [0-30]
LICZBA_PRACUJACYCH_DZWIGOW_PRZY_KAZDYM_OKIENKU_S = LICZBA_DZWIGOW_PRZY_KAZDYM_OKIENKU_S  # [0-3]
LICZBA_PRACUJACYCH_DZWIGOW_PRZY_KAZDEJ_BRAMIE = LICZBA_DZWIGOW_PRZY_KAZDEJ_BRAMIE  # [0-1]

# LICZBA_KONTENEROW_NA_STATKU = 25000  # [3000-25000]
# CZAS_ZMIANY_STATKU = 1  # [rozkład normalny, czas]

CZESTOTLIWOSC_STATKOW = 5
CZESTOTLIWOSC_CIEZAROWEK=2

Terminal = terminal(MAKS_POJEMNOSC_MAGAZYNU, MAKS_LICZBA_OKIENEK_S, MAKS_LICZBA_BRAM)

godzin_w_dniu = 24
liczba_dni = 10

start = time.time()
for i in range(liczba_dni * godzin_w_dniu):
    Terminal.krok()

end = time.time()

print(end - start)

statki, kontenery, prz_statki = Terminal.statystyka()

print("statki=", statki, "kontenery=",kontenery, "prz_statki=", prz_statki)