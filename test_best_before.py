from datetime import date
from unittest import TestCase

from best_before import possible_dates


__author__ = 'Tomasz Jakub Rup'


class TestPossibleDates(TestCase):
    def test_possible_dates(self):
        dates = possible_dates('01/01/01')
        self.assertEqual(len(dates), 1)
        self.assertTrue(date(2001, 1, 1) in dates)

        dates = possible_dates('01/01/99')
        self.assertEqual(len(dates), 1)
        self.assertTrue(date(2099, 1, 1) in dates)

        dates = possible_dates('12/11/10')
        self.assertEqual(len(dates), 6)
        self.assertTrue(date(2010, 11, 12) in dates)
        self.assertTrue(date(2010, 12, 11) in dates)
        self.assertTrue(date(2011, 10, 12) in dates)
        self.assertTrue(date(2011, 12, 10) in dates)
        self.assertTrue(date(2012, 10, 11) in dates)
        self.assertTrue(date(2012, 11, 10) in dates)

        dates = possible_dates('12/13/10')
        self.assertEqual(len(dates), 4)
        self.assertTrue(date(2010, 12, 13) in dates)
        self.assertTrue(date(2012, 10, 13) in dates)
        self.assertTrue(date(2013, 10, 12) in dates)
        self.assertTrue(date(2013, 12, 10) in dates)

        dates = possible_dates('2999/1/1')
        self.assertEqual(len(dates), 1)
        self.assertTrue(date(2999, 1, 1) in dates)

        dates = possible_dates('99/99/99')
        self.assertEqual(len(dates), 0)

        dates = possible_dates('01/01/01', separator='-')
        self.assertEqual(len(dates), 0)

        dates = possible_dates('01-01-01', separator='-')
        self.assertEqual(len(dates), 1)
        self.assertTrue(date(2001, 1, 1) in dates)
