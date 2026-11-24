import unittest

from classes.dzwig import dzwig
from classes.statek import statek

class TestSum(unittest.TestCase):

  def test_dzwig_instance(self):
    dzwig_instance = dzwig(1)
    self.assertEqual(dzwig_instance.jaka_szybkosc(),60)


if __name__ == '__main__':
  unittest.main()