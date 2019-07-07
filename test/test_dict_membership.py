import unittest
from more_fun_with_collections import dict_membership

class DictMembershipTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        test_dict = {'A':1, 'B':2, 'C':3}
        self.assertEqual(True, dict_membership.in_dict(test_dict, 'B'))
    def test_in_dict_false(self):
        test_dict = {'A':1, 'B':2, 'C':3}
        self.assertEqual(False, dict_membership.in_dict(test_dict, 'D'))
