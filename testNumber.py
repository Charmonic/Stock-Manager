import unittest
from generateNumber import *


class NumberTest(unittest.TestCase):
    def test_is_five_a_number(self):
        self.assertTrue(isNumber("5"))
        
    def test_is_Y_a_number(self):
        self.assertFalse(isNumber("Y"))

    def test_is_6_point_6_a_number(self):
        self.assertTrue(isNumber("6.6"))

    def test_is_6_comma_6_a_number(self):
        self.assertFalse(isNumber("6,6"))
        
class UpcTest(unittest.TestCase):
    def test_is_123456789123_correct(self):
        self.assertTrue(isCorrectUPC("123456789123"))

    def test_is_123456789_correct(self):
        self.assertFalse(isCorrectUPC("123456789"))

    def test_is_12345678912A_correct(self):
        self.assertFalse(isCorrectUPC("12345678912A"))

    def test_is_azertyuiopqs_correct(self):
        self.assertFalse(isCorrectUPC("azertyuiopqs"))

class GenerateUpcTest(unittest.TestCase):
    def test_is_the_generated_upc_correct(self):
        self.assertTrue(isCorrectUPC(generateUPC()))

class GeneratePriceTest(unittest.TestCase):
    def test_is_price_positive_number(self):
        self.assertTrue(generatePrice() >= 0)

    def test_is_price_a_float(self):
        self.assertEqual(type(generatePrice()), float)

class GenerateStockAndStockLimitTest(unittest.TestCase):
    def test_is_stock_a_int(self):
        self.assertEqual(type(generateStockandStockLimit()[0]), int)

    def test_is_stock_limit_a_int(self):
        self.assertEqual(type(generateStockandStockLimit()[1]), int)

class generateNameProductTest(unittest.TestCase):
    def test_is_the_name_in_the_list(self):
        names = ["Asparagus","Broccoli", "Carrots", "Corn", "Potatoes", "Spinach", "Zucchini"]
        self.assertIn(generateNameProduct(), names)
    
if __name__ == '__main__':
    unittest.main()
