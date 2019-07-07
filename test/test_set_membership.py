import unittest
from more_fun_with_collections import set_membership

class SetMembershipTestCase(unittest.TestCase):
    def test_in_set_true(self):
        test_set = {2, 4, 5}
        self.assertEqual(True, set_membership.in_set(test_set, 5))
    def test_in_set_false(self):
        test_set = {2, 4, 5}
        self.assertEqual(False, set_membership.in_set(test_set, 6))
