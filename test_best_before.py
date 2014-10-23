from datetime import date
from unittest import TestCase

from best_before import possible_dates


__author__ = 'Tomasz Jakub Rup'


class TestPossibleDates(TestCase):
    def test_possible_dates(self):
        self.assertEqual(possible_dates('01/01/01'), [date(2001, 1, 1)])
        self.assertEqual(possible_dates('01/01/99'), [date(2099, 1, 1)])
        self.assertEqual(possible_dates('12/11/10'), [date(2010, 11, 12), date(2010, 12, 11), date(2011, 10, 12),
                                                      date(2011, 12, 10), date(2012, 10, 11), date(2012, 11, 10)])
        self.assertEqual(possible_dates('12/13/10'), [date(2010, 12, 13), date(2012, 10, 13), date(2013, 10, 12),
                                                      date(2013, 12, 10)])
        self.assertEqual(possible_dates('2999/1/1'), [date(2999, 1, 1)])
        self.assertEqual(possible_dates('99/99/99'), [])
        self.assertEqual(possible_dates('01/01/01', separator='-'), [])
        self.assertEqual(possible_dates('01-01-01', separator='-'), [date(2001, 1, 1)])
