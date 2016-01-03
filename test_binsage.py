import unittest
import binsage

class Test(unittest.TestCase):

    def test_encode0(self):
        self.assertEqual(binsage.encode("a"), '01100001')
        self.assertEqual(binsage.encode("z"), '01111010')

    def test_encode1(self):
        self.assertEqual(binsage.encode("az"), '0110000101111010')

    def test_decode0(self):
        self.assertEqual(binsage.decode('01100001'), 'a')
        self.assertEqual(binsage.decode('01111010'), 'z')

    def test_decode1(self):
        self.assertEqual(binsage.decode('0110000101111010'), "az")
        
if __name__ == "__main__":
    unittest.main();
