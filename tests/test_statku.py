import unittest

from classes.statek import statek

class TestSum(unittest.TestCase):
    def setUp(self):
        self.statek_instance = statek()
        return super().setUp()

    def test_statek_instance(self):
        statek_instance = self.statek_instance
        self.assertGreater(statek_instance.ilosc_kontenerow, 3000)

    def test_czas_oczekiwania(self):
        statek_instance = self.statek_instance
        statek_instance.zwieksz_czas_oczekiwania()

        self.assertEqual(statek_instance.zwroc_czas_oczekiwania(),1)

    def test_rozladuj_kontener(self):
        statek_instance= self.statek_instance
        il_kont = statek_instance.ilosc_kontenerow
        self.assertEqual(statek_instance.rozladuj_kontener(il_kont), (il_kont, True))
if __name__ == '__main__':
  unittest.main()