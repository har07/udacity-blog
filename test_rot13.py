import unittest
from rot13 import Rot13

class TestRot13(unittest.TestCase):
    def setUp(self):
        pass

    def test_custom_escape_html(self):
        """
        test rot13 encryption function to:
        - normal mixed case 
        - non-alphabet chars only
        - mixed alphabet - non-alphabet
        - multiline mixed
        """

        rot = Rot13()
        self.assertEqual(rot.encrypt("Hello,"), "Uryyb,")
        self.assertEqual(rot.encrypt('<>&"'), '<>&"')
        self.assertEqual(rot.encrypt("Helx</>&'ylo,"), "Uryk</>&'lyb,")
        multilineInput = """Hello, world!

</textarea>"""
        multilineOutput = """Uryyb, jbeyq!

</grkgnern>"""
        self.assertEqual(rot.encrypt(multilineInput), multilineOutput)

if __name__ == '__main__':
    unittest.main()
