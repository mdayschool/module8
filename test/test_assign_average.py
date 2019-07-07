import unittest
from more_fun_with_collections import assign_average

class SwitchAverageTestCase(unittest.TestCase):
    def test_switch_a(self):
        self.assertEqual(90, assign_average.switch_average('A'))
    def test_switch_b(self):
        self.assertEqual(80, assign_average.switch_average('B'))
    def test_switch_c(self):
        self.assertEqual(70, assign_average.switch_average('C'))
    def test_switch_d(self):
        self.assertEqual(60, assign_average.switch_average('D'))
    def test_switch_f(self):
        self.assertEqual(50, assign_average.switch_average('F'))
    def test_switch_invalid(self):
        with self.assertRaises(ValueError):
            assign_average.switch_average('E')

