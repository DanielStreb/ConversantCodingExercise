"""
Program file: DataParser.

This program parses and returns a dataset for a plotting program
"""

from sys import exit
from csv import Sniffer, DictReader


class DataParser:
    """
    Summary: parses a data file, and returns list of the filtered data.

    Instances:
    1. accepted_records
    2. ignored_records

    Methods:
    1. valid_value
    2. create_reader
    3. create_dataset
    4. get_dataset
    """

    def __init__(self, csvfile, data_centers):
        """DataParser constructor."""
        self.accepted_records = []
        self.ignored_records = []

        with open(csvfile, 'r') as file:
            # Creates a reader object for later data manipulation
            reader = self.create_reader(file)

            # Resetting read/write pointer to beginning of file
            file.seek(0)

            # Creating list for graphing data center's dataset
            self.create_dataset(reader, data_centers)

    def valid_value(self, number):
        """
        Summary: Checks that value is a valid positive number.

        Description: Accepts positive whole and decimal numbers.
        """
        try:
            # Checking that entered value can be converted to a float.
            # Excludes letters and symbols.
            float(number)

            # Checking that validated number is nonnegative.
            if float(number) > 0:
                return True
            return False
        except ValueError:
            return False

    def create_reader(self, csvfile):
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
        if not Sniffer().has_header(csvfile.read(1024)):
            print('Imported csv file lacks header row')
            exit()

        # Resets the read/write pointer within the file
        csvfile.seek(0)

        # Creates a DictReader object with the csvfile provided, and the
        # dialect object to define the parameters of the reader instance.
        reader = DictReader(csvfile, dialect=file_dialect)

        # Return DictReader object
        return reader

    def create_dataset(self, reader=None, data_centers=None):
        """
        Summary: Creates a dataset of dcs and their respective times, values.

        Arguments: 'reader' defines a reader object used to read a csv file.
        'dataCenters' is a list containing data center names that are to be
        graphed.
        """
        for row in reader:
            # Checking that the 'DC' matches one defined in "data_centers" list
            if row.get('DC') in data_centers:
                # Validating DC's value is a positive nonnegative number.
                if not self.valid_value(row.get('Value')):
                    # Archiving ignored records for later analysis
                    self.ignored_records.append(row)
                else:
                    self.accepted_records.append(
                        [
                            row.get('DC'),
                            float(row.get('Time')),
                            float(row.get('Value'))
                        ]
                    )

    def get_dataset(self):
        """Getter for accepted_records list."""
        return self.accepted_records
