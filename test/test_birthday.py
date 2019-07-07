import unittest
from more_fun_with_collections import birthday
import datetime as dt

class HalfBirthdayTestCase(unittest.TestCase):
    def test_half_birthday(self):
        bday = dt.datetime(2019, 4, 20)
        hbday = dt.datetime(2019, 10, 19)
        self.assertEqual(hbday, birthday.half_birthday(bday))

