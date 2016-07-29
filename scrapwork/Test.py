"""CSV File Reader."""

from csv import Sniffer, DictReader

# Take file name as raw string
# test_file = r'DummyData.csv'
test_file = r'DummyData(negative numbers+decimal numbers+letters).csv'


def valid_number(s):
    """
    Summary: Checks that value is a valid positive number.

    Description: Accepts positive whole and decimal numbers.
    """
    try:
        float(s)
        if float(s) > 0:
            return True
        return False
    except ValueError:
        return False

with open(test_file, 'rb') as csvfile:
    csvfile.seek(0)
    file_dialect = Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = DictReader(csvfile, dialect=file_dialect)
    csvfile.seek(0)

    column = 'C'
    for row in reader:
        value = row.get(column)
        if not valid_number(value):
            print("Bad Value: {}".format(value))
        else:
            print("Good Value: {}".format(value))
