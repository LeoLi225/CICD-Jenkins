import unittest
from io import StringIO
import sys
import app

class TestApp(unittest.TestCase):
    def test_main_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        app.main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello, Jenkins!")

if __name__ == "__main__":
    unittest.main()
