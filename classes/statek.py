
import random

from classes.ciezarowka import element_kolejki


class statek(element_kolejki):
    def __init__(self, mu=14000,sigma=3667):
        element_kolejki.__init__(self)
        # self.ilosc_kontenerow = 10
        self.ilosc_kontenerow = int(random.gauss(mu,sigma))
        self.typ="A"

    def rozladuj_kontener(self, liczba_kontenerow):
        if liczba_kontenerow>self.ilosc_kontenerow:
            return self.ilosc_kontenerow, True
        # print(self.ilosc_kontenerow,  liczba_kontenerow, self.ilosc_kontenerow)

        self.ilosc_kontenerow-=liczba_kontenerow
        return liczba_kontenerow, False

    def zwroc_czas_oczekiwania(self):
        return super().zwroc_czas_oczekiwania()
