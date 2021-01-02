# unit-testing in python
# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods
import unittest
import addition


class TestAddition(unittest.TestCase):
    def test_do_stuff(self):
        test_params = [1, 2, 3]
        result = addition.do_stuff(*test_params)
        self.assertEqual(result, 11)

    def test_do_stuff2(self):
        """
        should throw TypeError if too few arguments
        """
        test_params = [1, "2"]
        # self.assertRaises(TypeError, addition.do_stuff, *test_params)
        with self.assertRaises(TypeError):
            addition.do_stuff(*test_params)

    def test_do_stuff3(self):
        """
        should trow ValueError: invalid literal for int() with base 10,
        if one arg is a non-convertible string
        """
        test_params = [1, "asdf", 3]
        result = addition.do_stuff(*test_params)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_do_stuff4(self):
        """
        should throw TypeError if too many arguments
        """
        test_params = [1, 2, 3, 4]
        # self.assertRaises(TypeError, addition.do_stuff, *test_params)
        with self.assertRaisesRegex(TypeError, "but 4 were"):
            addition.do_stuff(*test_params)

    def test_do_stuff5(self):
        """
        should throw TypeError if too few arguments
        """
        test_params = [1]
        # self.assertRaises(TypeError, addition.do_stuff, *test_params)
        with self.assertRaisesRegex(TypeError, "2 required positional arguments"):
            addition.do_stuff(*test_params)

    def test_do_stuff6(self):
        """
        should throw TypeError if wrong kwarg is passed
        """
        # self.assertRaises(TypeError, addition.do_stuff, *test_params)
        with self.assertRaisesRegex(TypeError, "an unexpected keyword argument 'num4'"):
            addition.do_stuff(1, 2, num4=2)


if __name__ == "__main__":
    unittest.main()