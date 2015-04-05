import unittest
import tools

class TestTools(unittest.TestCase):
    def setUp(self):
        pass

    def test_custom_escape_html(self):
        """
        test escape_html function for:
        - escaping <, >, &, "
        """

        self.assertEqual(tools.custom_escape_html("egk;erg"), "egk;erg")
        self.assertEqual(tools.custom_escape_html('x<>&"y'), "x&lt;&gt;&amp;&quot;y")

if __name__ == '__main__':
    unittest.main()
