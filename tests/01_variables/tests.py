from unittest import TestCase


class Evaluate(TestCase):
    def test_exercise(self):
        try:
            from exercise import var1, var2
        except ImportError:
            self.assertTrue(
                False, "Make sure you have created two variables, var1 and var2."
            )
        self.assertEqual(
            var1,
            var2,
            "Your variables var1 and var2 have different values. Make sure they have the same values.",
        )

    def test_multiply(self):
        try:
            from exercise import num1, num2
        except ImportError:
            self.assertTrue(
                False, "Make sure you have created two variables, num1 and num2."
            )
        self.assertEqual(
            num1 * num2,
            16,
            f"num1*num2 should be equal to 16, but it was equal to {num1 * num2}.",
        )