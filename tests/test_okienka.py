import unittest

from classes.okienko import okienko
from classes.statek import statek

class TestSum(unittest.TestCase):
    def setUp(self):
        self.okienko_instance = okienko(5,2000)
        return super().setUp()

    def test_okienko_instance(self):
        okienko_instance = self.okienko_instance
        self.assertEqual(okienko_instance.liczba_kontenerow_w_magazynie, 0)

    def test_statek_in_okienko(self):
        okienko_instance = self.okienko_instance
        self.assertIsNone(okienko_instance.statek)

    def test_wolne_bramy(self):
        okienko_instance = self.okienko_instance
        self.assertEqual(len(okienko_instance.wolne_bramy()),5)

    def test_szybkosc_dzwigow(self):
        okienko_instance = self.okienko_instance
        self.assertEqual(okienko_instance.laczna_szybkosc_dzwigow(),540)

    def test_zabierz_kontenery(self):
        okienko_instance = self.okienko_instance
        okienko_instance.zamagazynuj_kontenery(540)
        kont = min(okienko_instance.liczba_kontenerow_w_magazynie, 5*180)
        self.assertEqual(kont, okienko_instance.zabierz_kontenery_z_magazynu())
        okienko_instance.liczba_kontenerow_w_magazynie=0

    def test_rozladuj_None_statek(self):
        okienko_instance = self.okienko_instance
        self.assertIsNone(okienko_instance.statek)

    def test_calkowity_okienka(self):
        okienko_instance = self.okienko_instance
        statek_inst = statek()
        okienko_instance.zajac(statek_inst)
        okienko_instance.rozladuj_statek()
        self.assertEqual(okienko_instance.liczba_kontenerow_w_magazynie,540)

        okienko_instance.rozladuj_statek()
        self.assertEqual(okienko_instance.liczba_kontenerow_w_magazynie,1080)

        okienko_instance.zabierz_kontenery_z_magazynu()

        self.assertEqual(okienko_instance.liczba_kontenerow_w_magazynie,180)

        self.assertEqual(okienko_instance.liczba_wolnych_miejsc(), 2000-180)
        


if __name__ == '__main__':
  unittest.main()