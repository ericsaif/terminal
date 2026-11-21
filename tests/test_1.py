import unittest

class TestSum(unittest.TestCase):

  def test_sum_numbers(self):
    data = [100, 200, 300]
    self.assertEqual(sum(data), 600)


if __name__ == '__main__':
  unittest.main()