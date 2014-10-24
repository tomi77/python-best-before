import sys
import datetime
import itertools


__author__ = 'Tomasz Jakub Rup'


def possible_dates(date, separator=None):
    if separator is None:
        separator = '/'

    dates = set()

    parts = date.split(separator)
    if len(parts) != 3:
        return []

    input_parts = [int(part) for part in parts]

    for year, month, day in itertools.permutations(input_parts):
        if year < 2000:
            year += 2000

        try:
            new_date = datetime.date(year=year, month=month, day=day)
        except ValueError:
            pass
        else:
            dates.add(new_date)

    return dates


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Run with 'filename' parameter"
        sys.exit(1)

    filename = sys.argv[1]
    f = open(filename, 'r')

    for line in f:
        dates = possible_dates(line.strip())
        if len(dates) > 0:
            print min(dates).strftime('%Y-%m-%d')
        else:
            print 'is illegal'
