import unittest
from main import add
class TestMain (unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)  

if __name__ == '_main_':
    unittest.main()