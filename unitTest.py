import unittest
from Grok_TwoHeaps_SlidingWindowMedian_hard import *
class test_TwoHeaps_SlidingWindowMedian(unittest.TestCase):
    def setUp(self):
        """
        : you can instanciate the obj to be shared by all test methods here instead of instanciate one in each method
        :return:
        """
        print("this member will be call in the beginning before all the test cases.")
    def tearDown(self):
        print("this will be called after all test cases")
    def test_1(self):
        print("Hello Test Case 1")
        s=SlidingWindowMedian()
        nums = [1, 2, -1, 3, 5]
        k = 3
        self.assertEqual("0", s.find_sliding_window_median(nums, k))

    def test_raise_keyError(self):
        with self.assertRaises(KeyError): #if KeyError is raised, the test will pass
            pass  # some statement that raises KeyError

    @unittest.skip("SomeComments") #to skip this test case
    def test_assertTrue(self):
        print("hello test assertTrue")
        self.assertTrue(True)