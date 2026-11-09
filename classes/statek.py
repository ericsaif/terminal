
import random


class statek():
    def __init__(self, mu,sigma):
        self.ilosc_kontenerow = random.gauss(mu,sigma)
    def rozladuj_kontener(self):
        if self.ilosc_kontenerow==0:
            return -1
        self.ilosc_kontenerow-=1
        return 1
