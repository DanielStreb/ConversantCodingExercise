"""CSV File Reader."""

import csv

# Take file name as raw string
testData = r'DummyData(no_header).csv'

with open(testData, 'rb') as csvfile:
    # Determines the dialect of the csv file for processing
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    # Resets the read/write pointer within the file
    csvfile.seek(0)
    # Creates a reader object with the csvfile provided, and the dialect
    # object to define the parameters of the reader instance.
    reader = csv.reader(csvfile, dialect)
    print("Header: {}".format(csv.Sniffer().has_header(csvfile.read(1024))))
