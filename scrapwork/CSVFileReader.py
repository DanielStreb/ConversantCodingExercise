"""CSV File Reader."""

import csv

# Take file name as raw string
testData = r'DummyData.csv'

with open(testData, 'rb') as csvfile:
    # Determines the dialect of the csv file for processing
    file_dialect = csv.Sniffer().sniff(csvfile.read(1024))
    # Resets the read/write pointer within the file
    csvfile.seek(0)
    # Creates a reader object with the csvfile provided, and the dialect
    # object to define the parameters of the reader instance.
    reader = csv.DictReader(csvfile, dialect=file_dialect)
    # Checks to see that the csv file imported has a header row,
    # that will be used for later parsing.
    print("Header: {}".format(csv.Sniffer().has_header(csvfile.read(1024))))
    print('Delimiter: "{}"'.format(file_dialect.delimiter))
    # Resets the read/write pointer within the file
    csvfile.seek(0)

    for row in reader:
        print(row['Time'])
