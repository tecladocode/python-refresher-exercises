from unittest import TestCase

class Evaluate(TestCase):
    def test_dict(self):
        try:
            from exercise import student
        except ImportError:
            self.assertTrue(False, "Make sure that a variable 'student' exists, and has the value provided in the comments. If it does and you still see this error, check for syntax errors in your code.")
        self.assertTrue(isinstance(student, dict), "The student variable should be a dictionary, but is a {}.".format(type(student).__name__))
        student_name = student.get('name', None)
        student_school = student.get('school', None)
        student_grades = student.get('grades', None)
        self.assertEqual(student_name, 'Jose', "The value for the 'name' key in the student dictionary should be 'Jose', but was '{}'.".format(student_name))
        self.assertEqual(student_school, 'Computing', "The value for the 'school' key in the student dictionary should be 'Computing', but was '{}'.".format(student_school))
        self.assertEqual(student_grades, (66, 77, 88), "The value for the 'grades' key in the student dictionary should be (66, 77, 88), but was '{}'.".format(student_grades))

    def test_average_grade(self):
        try:
            from exercise import student
        except ImportError:
            self.assertTrue(False, "The variable student does not exist. Make sure the variable student exists and has the values as per the comment in the code. If it does and you still see this error, check for syntax errors in your code.")
        try:
            from exercise import average_grade
        except ImportError:
            self.assertTrue(False, "The function average_grade does not exist. Make sure the function exists and has the values as per the comment in the code. If it does and you still see this error, check for syntax errors in your code.")
        self.assertEqual(average_grade(student), 77, "average_age({}) returned {} instead of the expected 77. Make sure the student['grades'] is (66, 77, 88) and the function is calculating and returning the average of these grades.".format(student, average_grade(student)))
        average_single_grade = average_grade({'grades': (50,)})
        self.assertEqual(average_single_grade, 50, "The average_grade function did not calculate the average correctly when there is only one grade in the student list. The function was executed like so: average_grade({}), and it returned {}.".format({'grades': (50,)}, average_single_grade))

    def test_average_grade_all_students(self):
        try:
            from exercise import average_grade_all_students
        except ImportError:
            self.assertTrue(False, "Make sure a method average_grade_all_students exists, and implements the average grade of a list of students. If it does and you still see this error, check for syntax errors in your code.")

        students = [
            {'grades': (1, 2, 3)},
            {'grades': (0, 0, 0)},
            {'grades': (2, 10, 55)}
        ]

        self.assertEqual(int(average_grade_all_students(students)), 8, "Tried to execute average_grade_all_students with the following argument: \n[{'grades': (1, 2, 3)},\n{'grades': (0, 0, 0)},\n{'grades': (2, 10, 55)}]\n," + " but the answer was {} instead of the expected 8.".format(int(average_grade_all_students(students))))
