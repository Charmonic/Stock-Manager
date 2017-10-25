import unittest


    class returnNewStock(unittest.TestCase):
        def runTest(self):
            cStock = 18
            pStock = 8
            assert cStock - pStock == 10, 'correct amount'
