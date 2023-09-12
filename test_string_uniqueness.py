import unittest

from string_uniqueness import is_unique

class TestUniqueString(unittest.TestCase):


    def test_if_string_unique(self):
        unique_string = "qwerty"
        self.assertTrue(is_unique(unique_string))

    def test_if_string_not_unique(self):
        not_unique_string = "qwertyqwerty"
        self.assertFalse(is_unique(not_unique_string))
    

if __name__ == '__main__':
    unittest.main()
