import unittest
from rot13 import Rot13

class TestTools(unittest.TestCase):
    def setUp(self):
        pass

    def test_custom_escape_html(self):
        """
        test rot13 encryption function to:
        - normal mixed case 
        - non-alphabet chars only
        - mixed alphabet - non-alphabet
        """

        rot = Rot13()
        self.assertEqual(rot.encrypt("Hello,"), "Uryyb,")
        self.assertEqual(rot.encrypt('<>&"'), '<>&"')
        self.assertEqual(rot.encrypt("Helx</>&'ylo,"), "Uryk</>&'lyb,")

if __name__ == '__main__':
    unittest.main()
