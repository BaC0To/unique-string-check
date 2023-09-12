import unittest

from string_uniqueness import UniqueString


class TestUniqueString(unittest.TestCase):

    def setUp(self) -> None:
        self.string_to_be_tested = UniqueString()

    def tearDown(self) -> None:
        del self.string_to_be_tested

    def test_string_is_unique(self):
        """
        Test whether a string is a unique or not --> True/False
        """
        dummy_string = "abcd"
        result = self.string_to_be_tested.unique(dummy_string)
        self.assertTrue(result)

    def test_string_is_not_unique(self):
        """
        Test whether a string is a unique or not --> True/False
        """
        dummy_string = "abcdabcd"
        result = self.string_to_be_tested.unique(dummy_string)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()