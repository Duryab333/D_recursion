"""
Run unit tests with discovery (-m) or from __main__() with verbosity level 2
 - python -m unittest test_numbers.py
 - python test_numbers.py

Output with verbosity level < 2:
================================
...........
----------------------------------------------------------------------
Ran 11 tests in 0.002s
OK
<unittest.runner.TextTestResult run=11 errors=0 failures=0>
"""
import unittest
from expressions import Expressions
from expressions import __file__ as numbers__file__
from __init__ import PACKAGE_DIR, PROJECT_PATH, import_sol_module


class TestCase_test_data:
    """
    Class with test data (objects under test, instances of class Numbers: ut1...)
    """
    # objects "under test" or "tested objects" are instances
    # of class Numbers initialized with varying lists
    ut1 = Expressions(Expressions.default_numbers)  # [4, 12, 3, 8, 17, 12, 1, 8, 7]
    ut2 = Expressions([1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8])
    ut3 = Expressions([6, 67, 6, 8, 17, 3, 6, 8])
    ut4 = Expressions([8, 3, 9])
    ut5 = Expressions([1, 1, 1])
    ut6 = Expressions([0, 0])
    ut7 = Expressions([0])
    ut8 = Expressions([])


class Test_Expressions(unittest.TestCase):
    """
    Top-level class that inherits from class unittest.TestCase
    and injects test data into derived test classes.
    Sub-classes of unittest.TestCase are discovered as unit tests.
    """
    def setUp(self):
        # TestCase_test_data.inject_test_data_into(self)
        td_ = TestCase_test_data
        self.ut1 = td_.ut1
        self.ut2 = td_.ut2
        self.ut3 = td_.ut3
        self.ut4 = td_.ut4
        self.ut5 = td_.ut5
        self.ut6 = td_.ut6
        self.ut7 = td_.ut7
        self.ut8 = td_.ut8


class Disabled_test:
    """
    Class does not inherit from unittest.TestCase and
    is hence ignored by test discovery.
    """
    pass


try:
    mod = import_sol_module(numbers__file__)
    verbosity_level = 1
    Test_class = Test_Expressions
#
except ImportError:
    verbosity_level = 2
    Test_class = Disabled_test

# initialize test cases as tests (Test_Numbers) or disabled
TestCase_a = TestCase_b = TestCase_c = TestCase_d = Test_class
TestCase_e = TestCase_f = TestCase_g = TestCase_h = Test_class
TestCase_i = TestCase_j = TestCase_k = Test_class

# uncomment tests, one after the other as you progress from b) through k)
TestCase_a = Test_Expressions   # test a) passes, solution is given in numbers.py
TestCase_b = Test_Expressions
TestCase_c = Test_Expressions
TestCase_d = Test_Expressions
TestCase_e = Test_Expressions
TestCase_f = Test_Expressions
TestCase_g = Test_Expressions
TestCase_h = Test_Expressions
TestCase_i = Test_Expressions
TestCase_j = Test_Expressions
TestCase_k = Test_Expressions



class TestCase_a_number_of_numbers(TestCase_a):
    # 
    # tests a): number of numbers tests (lengths of numbers lists)
    def test_a_number_of_numbers(self):
        self.assertEqual(self.ut1.a, 9)
        self.assertEqual(self.ut2.a, 22)
        self.assertEqual(self.ut3.a, 8)
        self.assertEqual(self.ut4.a, 3)
        self.assertEqual(self.ut5.a, 3)
        self.assertEqual(self.ut6.a, 2)
        self.assertEqual(self.ut7.a, 1)
        self.assertEqual(self.ut8.a, 0)


class TestCase_b_first_three_numbers(TestCase_b):
    # 
    # tests b): first three numbers
    def test_b_first_three_numbers(self):
        self.assertEqual(self.ut1.b, [4, 12, 3])
        self.assertEqual(self.ut2.b, [1, 4, 6])
        self.assertEqual(self.ut3.b, [6, 67, 6])
        self.assertEqual(self.ut4.b, [8, 3, 9])
        self.assertEqual(self.ut5.b, [1, 1, 1])
        self.assertEqual(self.ut6.b, [0, 0])
        self.assertEqual(self.ut7.b, [0])
        self.assertEqual(self.ut8.b, [])


class TestCase_c_last_three_numbers(TestCase_c):
    # 
    # tests c): last three numbers
    def test_c_last_three_numbers(td):
        td.assertEqual(td.ut1.c, [1, 8, 7])
        td.assertEqual(td.ut2.c, [67, 6, 8])
        td.assertEqual(td.ut3.c, [3, 6, 8])
        td.assertEqual(td.ut4.c, [8, 3, 9])
        td.assertEqual(td.ut5.c, [1, 1, 1])
        td.assertEqual(td.ut6.c, [0, 0])
        td.assertEqual(td.ut7.c, [0])
        td.assertEqual(td.ut8.c, [])


class TestCase_d_last_threeClass_in_reverse(TestCase_d):
    # 
    # tests d): last three numbers in reverse
    def test_d_last_threeClass_in_reverse(td):
        td.assertEqual(td.ut1.d, [7, 8, 1])
        td.assertEqual(td.ut2.d, [8, 6, 67])
        td.assertEqual(td.ut3.d, [8, 6, 3])
        td.assertEqual(td.ut4.d, [9, 3, 8])
        td.assertEqual(td.ut5.d, [1, 1, 1])
        td.assertEqual(td.ut6.d, [0, 0])
        td.assertEqual(td.ut7.d, [0])
        td.assertEqual(td.ut8.d, [])


class TestCase_e_odd_numbers(TestCase_e):
    # 
    # tests e): odd numbers
    def test_e_odd_numbers(td):
        td.assertEqual(td.ut1.e, [3, 17, 1, 7])
        td.assertEqual(td.ut2.e, [1, 67, 23, 49, 67, 23, 37, 67, 19, 67])
        td.assertEqual(td.ut3.e, [67, 17, 3])
        td.assertEqual(td.ut4.e, [3, 9])
        td.assertEqual(td.ut5.e, [1, 1, 1])
        td.assertEqual(td.ut6.e, [])
        td.assertEqual(td.ut7.e, [])
        td.assertEqual(td.ut8.e, [])


class TestCase_f_number_of_odd_numbers(TestCase_f):
    # 
    # tests f): number of odd numbers
    def test_f_number_of_odd_numbers(td):
        td.assertEqual(td.ut1.f, 4)
        td.assertEqual(td.ut2.f, 10)
        td.assertEqual(td.ut3.f, 3)
        td.assertEqual(td.ut4.f, 2)
        td.assertEqual(td.ut5.f, 3)
        td.assertEqual(td.ut6.f, 0)
        td.assertEqual(td.ut7.f, 0)
        td.assertEqual(td.ut8.f, 0)


class TestCase_g_sum_of_odd_numbers(TestCase_g):
    # 
    # tests g): sum of odd numbers
    def test_g_sum_of_odd_numbers(td):
        td.assertEqual(td.ut1.g, 28)
        td.assertEqual(td.ut2.g, 420)
        td.assertEqual(td.ut3.g, 87)
        td.assertEqual(td.ut4.g, 12)
        td.assertEqual(td.ut5.g, 3)
        td.assertEqual(td.ut6.g, 0)
        td.assertEqual(td.ut7.g, 0)
        td.assertEqual(td.ut8.g, 0)


class TestCase_h_duplicateClass_removed(TestCase_h):
    # 
    # tests h): duplicate numbers removed
    def test_h_duplicateClass_removed(td):
        td.assertEqual(td.ut1.h, [4, 12, 3, 8, 17, 1, 7])
        td.assertEqual(td.ut2.h, [1, 4, 6, 67, 8, 23, 34, 49, 37, 19])
        td.assertEqual(td.ut3.h, [6, 67, 8, 17, 3])
        td.assertEqual(td.ut4.h, [8, 3, 9])
        td.assertEqual(td.ut5.h, [1])
        td.assertEqual(td.ut6.h, [0])
        td.assertEqual(td.ut7.h, [0])
        td.assertEqual(td.ut8.h, [])


class TestCase_i_number_of_duplicate_numbers(TestCase_i):
    # 
    # tests i): number of duplicate numbers
    def test_i_number_of_duplicate_numbers(td):
        td.assertEqual(td.ut1.i, 2)
        td.assertEqual(td.ut2.i, 12)
        td.assertEqual(td.ut3.i, 3)
        td.assertEqual(td.ut4.i, 0)
        td.assertEqual(td.ut5.i, 2) # [1, 1, 1] has 2 duplicates 1
        td.assertEqual(td.ut6.i, 1) # [0, 0] has one duplicate number 0
        td.assertEqual(td.ut7.i, 0)
        td.assertEqual(td.ut8.i, 0)


class TestCase_j_ascending_squaredClass_no_duplicates(TestCase_j):
    # 
    # tests j): ascending list of squared numbers with no duplicates
    def test_j_ascending_squaredClass_no_duplicates(td):
        td.assertEqual(td.ut1.j, [1, 9, 16, 49, 64, 144, 289])
        td.assertEqual(td.ut2.j, [1, 16, 36, 64, 361, 529, 1156, 1369, 2401, 4489])
        td.assertEqual(td.ut3.j, [9, 36, 64, 289, 4489])
        td.assertEqual(td.ut4.j, [9, 64, 81])
        td.assertEqual(td.ut5.j, [1])
        td.assertEqual(td.ut6.j, [0])
        td.assertEqual(td.ut7.j, [0])
        td.assertEqual(td.ut8.j, [])


class TestCase_k_classifyClass_as_odd_even_empty(TestCase_k):
    # 
    # tests k): classify as "ODD_LIST", "EVEN_LIST" or "EMPTY_LIST" depending on numbers length
    def test_k_classifyClass_as_odd_even_empty(td):
        td.assertEqual(td.ut1.k, "ODD_LIST")
        td.assertEqual(td.ut2.k, "EVEN_LIST")
        td.assertEqual(td.ut3.k, "EVEN_LIST")
        td.assertEqual(td.ut4.k, "ODD_LIST")
        td.assertEqual(td.ut5.k, "ODD_LIST")
        td.assertEqual(td.ut6.k, "EVEN_LIST")
        td.assertEqual(td.ut7.k, "ODD_LIST")
        td.assertEqual(td.ut8.k, "EMPTY_LIST")


if __name__ == '__main__':
    # 
    # discover tests in this package
    test_classes = unittest.defaultTestLoader \
        .discover(PACKAGE_DIR, pattern='test_*.py', top_level_dir=PROJECT_PATH)
    # 
    suite = unittest.TestSuite(test_classes)
    runner = unittest.runner.TextTestRunner(verbosity=verbosity_level)
    result = runner.run(suite)
    print(result)
