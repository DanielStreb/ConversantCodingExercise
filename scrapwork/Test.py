"""CSV File Reader."""

from csv import Sniffer, DictReader

# Take file name as raw string
# test_file = r'DummyData.csv'
# test_file = r'DummyData(negative numbers+decimal numbers+letters).csv'
test_file = r'Data(Relevant).csv'


def valid_number(s):
    """
    Summary: Checks that value is a valid positive number.

    Description: Accepts positive whole and decimal numbers.
    """
    try:
        # Checking that entered value can be converted to a float.
        # Excludes letters and symbols.
        float(s)

        # Checking that validated number is nonnegative.
        if float(s) > 0:
            return True
        return False
    except ValueError:
        return False

# Opening data binary file for reading, hence 'rb', as 'csvfile'.
with open(test_file, 'rb') as csvfile:
    # Resetting read/write pointer to beginning of file
    csvfile.seek(0)

    file_dialect = Sniffer().sniff(csvfile.read(1024))

    # Resetting read/write pointer to beginning of file
    csvfile.seek(0)

    reader = DictReader(csvfile, dialect=file_dialect)

    # Resetting read/write pointer to beginning of file
    csvfile.seek(0)

    goodRecords = []
    ignoredRecords = []

    dataCenters = ['I', 'A', 'S']
    for row in reader:
        if row.get('DC') in dataCenters:
            value = row.get('Value')
            if not valid_number(value):
                ignoredRecords.append(row)
            else:
                goodRecords.append(row)
