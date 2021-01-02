# unit-testing in python
# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods
import unittest
import addition


class TestAddition(unittest.TestCase):
    # make sure all test methods are named differently because otherwise only the first one is run
    def setUp(self):
        print("about to test a function")

    def test_do_stuff(self):
        """
        should return 11 when function is called with args (1,2,3)
        """
        test_params = [1, 2, 3]
        result = addition.do_stuff(*test_params)
        self.assertEqual(result, 11)

    # def test_do_stuff2(self):
    #     """
    #     should throw TypeError if too few arguments
    #     """
    #     test_params = [1, "2"]
    #     # self.assertRaises(TypeError, addition.do_stuff, *test_params)
    #     with self.assertRaises(TypeError):
    #         addition.do_stuff(*test_params)

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

    # def test_do_stuff5(self):
    #     """
    #     should throw TypeError if too few arguments
    #     """
    #     test_params = [1]
    #     # self.assertRaises(TypeError, addition.do_stuff, *test_params)
    #     with self.assertRaisesRegex(TypeError, "2 required positional arguments"):
    #         addition.do_stuff(*test_params)

    def test_do_stuff6(self):
        """
        should throw TypeError if wrong kwarg is passed
        """
        # self.assertRaises(TypeError, addition.do_stuff, *test_params)
        with self.assertRaisesRegex(TypeError, "an unexpected keyword argument 'num4'"):
            addition.do_stuff(1, 2, num4=2)

    # def test_do_stuff7(self):
    #     """
    #     should throw TypeError if arg is instance of "NoneType"
    #     """
    #     test_params = [1, 2, None]
    #     # self.assertRaises(TypeError, addition.do_stuff, *test_params)
    #     with self.assertRaisesRegex(TypeError, "not 'NoneType'"):
    #         addition.do_stuff(*test_params)

    def test_do_stuff8(self):
        result = addition.do_stuff()
        self.assertEqual(result, 5)

    def test_do_stuff9(self):
        """
        args should default to 0 if they are of type <class 'NoneType'>
        """
        test_params = [1, 2, None]
        result = addition.do_stuff(*test_params)
        self.assertEqual(result, 8)

    def tearDown(self):
        print("cleaning up")


# unit tests should only be run if they are executed from this file directly
# if this code is run through an accidental import then unit tests shouldn't be triggered
if __name__ == "__main__":
    unittest.main()
