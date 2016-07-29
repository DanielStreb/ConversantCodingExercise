"""CSV File Reader."""

import csv

testData = r'DummyData(no_header).csv'

with open(testData, 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)  # Resets the read/write pointer within the file
    reader = csv.reader(csvfile, dialect)
    print("Header: {}".format(csv.Sniffer().has_header(csvfile.read(1024))))
