"""CSV File Reader."""

from csv import Sniffer, DictReader

# Take file name as raw string
test_file = r'Data(Relevant).csv'

# List of valid data centers
dataCenters = ('I', 'A', 'S')


def create_reader(csvfile=None):
    """
    Summary: Validates a csv file, returns a DictReader object.

    Description: Takes one argument: "data" (Should be a csv file)
    """
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

    # Return DictReader object
    return reader


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
    # Creates a reader object for later data manipulation
    reader = create_reader(csvfile)

    # Resetting read/write pointer to beginning of file
    csvfile.seek(0)

    dcs_to_graph = []
    ignoredRecords = []

    for dc in dataCenters:
        dcs_to_graph.append({'Name': dc, 'Times': [], 'Values': []})

    for row in reader:
        # Checking that the 'DC' matches one defined in "dataCenters" list
        if row.get('DC') in dataCenters:
            # Validating DC's recorded value is a positive nonnegative number.
            if not valid_number(row.get('Value')):
                ignoredRecords.append(row)
            else:
                for dc in dcs_to_graph:
                    if dc['Name'] == row.get('DC'):
                        dc['Times'].append(float(row.get('Time')))
                        dc['Values'].append(float(row.get('Value')))

    for dc in dcs_to_graph:
        print(dc['Name'])
        print(max(dc['Times']))
        print(max(dc['Values']))

"""with open(test_file, 'rb') as csvfile:
    try:
        if not Sniffer().has_header(csvfile.read(1024)):
            raise NameError("No header row in file detected")
    except NameError:
        print('An exception flew by!')
        raise
    print("Header: {}".format(Sniffer().has_header(csvfile.read(1024))))
"""
