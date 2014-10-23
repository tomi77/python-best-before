__author__ = 'Tomasz Jakub Rup'

import sys
import datetime
import itertools


def possible_dates(date, separator=None):
    if separator is None:
        separator = '/'

    dates = []

    parts = date.split(separator)
    if len(parts) != 3:
        return dates

    input_parts = [int(part) for part in parts]

    for year, month, day in itertools.permutations(input_parts):
        try:
            if year < 2000:
                year += 2000

            dates.append(datetime.date(year=year, month=month, day=day))
        except ValueError:
            pass

    return dates


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Run with 'filename' parameter"
        sys.exit(1)

    filename = sys.argv[1]
    f = open(filename, 'r')

    for line in f:
        try:
            print min(possible_dates(line.strip()))
        except ValueError:
            print 'is illegal'