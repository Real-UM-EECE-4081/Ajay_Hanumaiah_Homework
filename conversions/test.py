
from util import convert_to_C
from util import convert_to_F
import unittest

class TestConversions(unittest.TestCase):

    def testGoodC(self):
      Temp = convert_to_C(32)
      self.assertEqual(Temp,0, "Wrong Temp")

    def testGoodF(self):
        Temp = convert_to_F(30)
        self.assertEqual(Temp,86, "Wrong Temp")

    def testBelowAbC(self):
      self.assertRaises(ValueError, convert_to_C, -460)

    def testBelowAbF(self):
      self.assertRaises(ValueError, convert_to_F, -280)


unittest.main()
