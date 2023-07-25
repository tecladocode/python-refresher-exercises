from unittest import TestCase

class Evaluate(TestCase):
    def test_multiplication_function(self):
        try:
            from exercise import my_function
        except ImportError:
            self.assertTrue(False, "Make sure to create the function my_function(arg1, arg2). Make sure the function is not created inside the return_42 function.")
        self.assertEqual(my_function(4, 5), 20, "The function my_function does not return the result of its two arguments multiplied together. Make sure that it takes two arguments, and returns them multiplied together.")
        self.assertEqual(my_function("a", 2), "aa", "The function my_function does not return the result of its two arguments multiplied together. Make sure that it takes two arguments, and returns them multiplied together.")

    def test_give_16(self):
        try:
            from exercise import return_42
        except ImportError:
            self.assertTrue(False, "Make sure the return_42 function exists and has not been deleted. You can bring the function back by pressing 'Reset code' at the bottom of the editor. This will delete all your code and put it back to what it was in the beginning.")
        self.assertEqual(return_42(), 42, "The function return_42 did not return 42. Make sure it is returning 42, and not just printing 42.")
