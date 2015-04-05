import unittest
import validations

class TestValidations(unittest.TestCase):
  # """test package for my udacity web app"""
  
  def setUp(self):
    pass

  def test_valid_month(self):
    """
    test month validator functions for:
    - arbitrary invalid strings
    - None
    - empty strings
    - exactly valid month string
    - different case month string
    """

    self.assertEqual(validations.valid_month("egk;erg"), None)
    self.assertEqual(validations.valid_month(None), None)
    self.assertEqual(validations.valid_month(""), None)
    self.assertEqual(validations.valid_month("January"), "January")
    self.assertEqual(validations.valid_month("jaNuary"), "January")
    self.assertEqual(validations.valid_month("jAn"), "January")

  def test_valid_day(self):
    """
    test day validator functions for:
    - day < 1
    - None
    - empty strings
    - 1 <= day <= 31
    - day > 31
    """

    self.assertEqual(validations.valid_day('-100'), None)
    self.assertEqual(validations.valid_day('0'), None)
    self.assertEqual(validations.valid_day(None), None)
    self.assertEqual(validations.valid_day(''), None)
    self.assertEqual(validations.valid_day('5'), 5)
    self.assertEqual(validations.valid_day('31'), 31)
    self.assertEqual(validations.valid_day('1'), 1)
    self.assertEqual(validations.valid_day('3000'), None)

  def test_valid_year(self):
    """
    test year validator functions for:
    - year < 1900
    - None
    - empty strings
    - 1900 <= year <= 2020
    - day > 2020
    """

    self.assertEqual(validations.valid_year('-100'), None)
    self.assertEqual(validations.valid_year('0'), None)
    self.assertEqual(validations.valid_year(None), None)
    self.assertEqual(validations.valid_year(''), None)
    self.assertEqual(validations.valid_year('1500'), None)
    self.assertEqual(validations.valid_year('1900'), 1900)
    self.assertEqual(validations.valid_year('2020'), 2020)
    self.assertEqual(validations.valid_year('3000'), None)

if __name__ == '__main__':
	unittest.main()
    