import importlib
from unittest import TestCase
from unittest.mock import patch


class Evaluate(TestCase):
    def test_evens(self):
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('q',)
                try:
                    from exercise import evens
                except ImportError:
                    self.assertTrue(False,
                                    "Make sure to not delete the 'evens' variable—you can reset the code to the starting state by pressing the 'Reset code' at the bottom of the editor. This will erase your changes though!")
                self.assertEqual(evens, [2, 4, 6, 8],
                                 "Your 'evens' variable did not return only a list of even numbers. It returned {}.".format(
                                     evens))

    def test_user_menu_quits(self):
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('q',)
                try:
                    import exercise
                    importlib.reload(exercise)
                except ImportError:
                    self.assertTrue(False,
                                    "An unknown error happened, we were unable to find your solution file. Please write a question in the Course Q&A with a full screenshot of this coding exercise!")
                expected_call_args = [(('Quit',),)]
                self.assertEqual(mocked_print.call_args_list, expected_call_args,
                                 "When the user enters 'q', your code isn't printing 'Quit'. Remember that Python cares about uppercase and lowercase, so make sure you're using the right one!")

    def test_user_menu_adds(self):
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('a',)
                try:
                    import exercise
                    importlib.reload(exercise)
                except ImportError:
                    self.assertTrue(False,
                                    "An unknown error happened, we were unable to find your solution file. Please write a question in the Course Q&A with a full screenshot of this coding exercise!")
                expected_call_args = [(('Add',),)]
                self.assertEqual(mocked_print.call_args_list, expected_call_args,
                                 "When the user enters 'a', your code isn't printing 'Add'. Make sure your if statement still supports the initial condition. You can reset the code by clicking the 'Reset code' button at the bottom of the editor, although that will erase all your changes!")
