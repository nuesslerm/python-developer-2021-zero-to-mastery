# unit-testing in python
# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods
import unittest
from random_game_pure import guess_numbers


# Important: By default, only functions whose name that start with test are run
class TestRandomGame(unittest.TestCase):
    def test_guess_numbers1(self):
        """
        should return False if input is not convertible to int
        """
        float_input = "asdf"
        to_guess = 8
        result = guess_numbers(float_input, to_guess)
        self.assertEqual(result, False)

    def test_guess_numbers2(self):
        """
        should return False if guess is incorrect
        """
        float_input = 5
        to_guess = 6
        result = guess_numbers(float_input, to_guess)
        self.assertEqual(result, False)

    def test_guess_numbers3(self):
        """
        should return True if guess is correct
        """
        float_input = 5
        to_guess = 5
        result = guess_numbers(float_input, to_guess)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()