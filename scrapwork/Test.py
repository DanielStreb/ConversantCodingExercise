"""Test File."""

from csv import Sniffer, DictReader

import numpy as np
import pylab as pl

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


def valid_number(number):
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


def create_dc_graph_dataset(reader=None, data_centers=None):
    """
    Summary: Creates a dataset of dcs and their respective times, values.

    Arguments: 'reader' defines a reader object used to read a csv file.
    'dataCenters' is a list containing data center names that are to be
    graphed.
    """
    dcs_to_graph = []
    ignored_records = []

    for dc in data_centers:
        dcs_to_graph.append({'Name': dc, 'Time_data': [], 'Value_data': []})

    for row in reader:
        # Checking that the 'DC' matches one defined in "dataCenters" list
        if row.get('DC') in dataCenters:
            # Validating DC's recorded value is a positive nonnegative number.
            if not valid_number(row.get('Value')):
                ignored_records.append(row)  # Archiving ignored records
            else:
                for data_cent in dcs_to_graph:
                    if data_cent['Name'] == row.get('DC'):
                        data_cent['Time_data'].append(float(row.get('Time')))
                        data_cent['Value_data'].append(float(row.get('Value')))

    return dcs_to_graph


def graph_dataset(dc_dataset_to_graph=None):
    """
    Summary: function that graphs data center dataset.

    Arguments: 'dc_dataset_to_graph' is a list containing dictionary
    instances holding specific datacenter attributes for value and time
    """
    # List storing tuples of color values and names for use in graph title
    colors = [
        ('b', 'blue'), ('g', 'green'), ('r', 'red'),
        ('c', 'cyan'), ('m', 'magenta'), ('y', 'yellow'),
        ('k', 'black'), ('w', 'white')
    ]

    # Declaring empty data centers' graph title string
    graphed_dcs_title = "Data Centers: "

    for i, dc in enumerate(dc_dataset_to_graph):
        # Modding i by 8 to maintain valid index range
        # in colors list(contains 8 colors).
        index = i % 8

        # Line_color variable for varying line color among graphed data
        line_color = colors[index][0]

        # Making an array of x values(time axis)
        x = dc['Time_data']
        # Making an array of y values(value axis)
        y = dc['Value_data']

        # Using pylab to plot time(x) vs. value(y) as red circles
        pl.plot(x, y, line_color)

        # Appending Data Center Names and associated line color for
        # valid graph title.
        graphed_dcs_title += dc['Name'] + '({}), '.format(colors[index][1])

    # Giving scatterplot a title
    pl.title(graphed_dcs_title)
    # Making axis labels
    pl.xlabel('Time axis')
    pl.ylabel('Value axis')

    # Displaying plot on the screen
    pl.show()

# Opening data binary file for reading, hence 'rb', as 'csvfile'.
with open(test_file, 'r') as csvfile:
    # Creates a reader object for later data manipulation
    reader = create_reader(csvfile)

    # Resetting read/write pointer to beginning of file
    csvfile.seek(0)

    # Creating list for graphing data center's dataset
    dcs_to_graph = create_dc_graph_dataset(reader, dataCenters)

    # Graphing Data Center Data
    graph_dataset(dcs_to_graph)
