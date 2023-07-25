from unittest import TestCase


class Evaluate(TestCase):
    def test_list(self):
        try:
            from exercise import my_list
        except ImportError:
            self.assertTrue(
                False,
                "Make sure a variable called my_list has been created and contains three numbers. The three numbers added together should equal 100.",
            )
        self.assertEqual(
            sum(my_list),
            100,
            "The elements of the list added together do not add up to 100.",
        )
        self.assertEqual(
            len(my_list),
            3,
            "The list has {} elements, but it should have only 3 elements.".format(
                len(my_list)
            ),
        )

    def test_tuple(self):
        try:
            from exercise import my_tuple
        except ImportError:
            self.assertTrue(
                False,
                "Make sure a variable my_tuple exists, and it only has a single element in it.",
            )
        self.assertEqual(
            len(my_tuple),
            1,
            "The tuple created has {} elements in it, but it should have only 1.".format(
                len(my_tuple)
            ),
        )
        self.assertTrue(
            isinstance(my_tuple, tuple),
            "The variable my_tuple is not a tuple, it is a {}.".format(
                type(my_tuple).__name__
            ),
        )

    def test_set(self):
        try:
            from exercise import set1, set2
        except ImportError:
            self.assertTrue(
                False,
                "Make sure two variables, set1 and set2, have been defined and are sets.",
            )
        self.assertEqual(
            set1.intersection(set2),
            {5, 77, 9, 12},
            "The intersection of the two sets should be equal to {5, 77, 9, 12}. This means that these elements must be present in both sets.",
        )
