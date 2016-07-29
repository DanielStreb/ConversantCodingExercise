"""CSV File Reader."""

from csv import Sniffer, DictReader

# Take file name as raw string
# test_file = r'DummyData.csv'
test_file = r'DummyData(negative numbers+decimal numbers+letters).csv'


def create_reader(data=None):
    """
    Summary: Validates a csv file, returns a DictReader object.

    Description: Takes one argument: "data" (Should be a csv file)
    """
    # Opening data binary file for reading, hence 'rb', as 'csvfile'.
    with open(data, 'rb') as csvfile:
        # Determines the dialect of the csv file for processing
        file_dialect = Sniffer().sniff(csvfile.read(1024))

        # Resets the read/write pointer within the file
        csvfile.seek(0)

        # Checks to see that the csv file imported has a header row,
        # that will be used for later parsing.
        print("Header: {}".format(Sniffer().has_header(csvfile.read(1024))))
        print('Delimiter: "{}"'.format(file_dialect.delimiter))

        # Resets the read/write pointer within the file
        csvfile.seek(0)

        # Creates a DictReader object with the csvfile provided, and the
        # dialect object to define the parameters of the reader instance.
        reader = DictReader(csvfile, dialect=file_dialect)

        # Turn this block into a function for filtering columns of data
        column = 'Time'
        for row in reader:
            print(row.get(column))  # Returns all values from column.
            # print(row['Time'])

        # Return DictReader object
        return reader

# data = create_reader(test_file)
# print(data)

"""with open(test_file, 'rb') as csvfile:
    try:
        if not Sniffer().has_header(csvfile.read(1024)):
            raise NameError("No header row in file detected")
    except NameError:
        print('An exception flew by!')
        raise
    print("Header: {}".format(Sniffer().has_header(csvfile.read(1024))))
"""

