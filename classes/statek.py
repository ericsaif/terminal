
import random


class statek():
    def __init__(self, mu,sigma):
        self.ilosc_kontenerow = random.gauss(mu,sigma)
    def rozladuj_kontener(self, liczba_kontenerow):
        if liczba_kontenerow>self.ilosc_kontenerow:
            return self.ilosc_kontenerow
        self.ilosc_kontenerow-=liczba_kontenerow
        return liczba_kontenerow
