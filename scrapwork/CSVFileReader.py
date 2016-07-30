"""Test File."""

from csv import Sniffer, DictReader

import matplotlib.dates as dt
import matplotlib.pyplot as plt

from matplotlib.dates import HourLocator, MinuteLocator, DateFormatter

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
    print(
        "\tFile has Header: {}".format(
            Sniffer().has_header(csvfile.read(1024))
        )
    )
    print(
        '\tFile Delimiter: "{}"'.format(
            file_dialect.delimiter)
    )

    # Resets the read/write pointer within the file
    csvfile.seek(0)

    # Creates a DictReader object with the csvfile provided, and the
    # dialect object to define the parameters of the reader instance.
    reader = DictReader(csvfile, dialect=file_dialect)

    # Return DictReader object
    return reader


def valid_value(number):
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


def create_dc_dataset(reader=None, data_centers=None):
    """
    Summary: Creates a dataset of dcs and their respective times, values.

    Arguments: 'reader' defines a reader object used to read a csv file.
    'dataCenters' is a list containing data center names that are to be
    graphed.
    """
    accepted_records = []
    ignored_records = []

    for row in reader:
        # Checking that the 'DC' matches one defined in "data_centers" list
        if row.get('DC') in data_centers:
            # Validating DC's recorded value is a positive nonnegative number.
            if not valid_value(row.get('Value')):
                ignored_records.append(row)  # Archiving ignored records
            else:
                accepted_records.append(
                    [
                        row.get('DC'),
                        float(row.get('Time')),
                        float(row.get('Value'))
                    ]
                )

    return accepted_records


def plot_dc(name=None, records=[], ax=None):
    """Function to plot data for a specified Data Center."""
    values = []
    times = []
    for r in records[:]:
        if r[0] == name:
            times.append(dt.epoch2num(r[1]))
            values.append(r[2])
            records.remove(r)
        else:
            pass
    ax.plot_date(times, values, xdate=True)


def graph_dataset(dc_dataset_to_graph=None):
    """
    Summary: function that graphs data center dataset.

    Arguments: 'dc_dataset_to_graph' is a list containing dictionary
    instances holding specific datacenter attributes for value and time
    """
    # List to keep track of plotted data centers for legend creation
    plotted_dc = []

    hours = HourLocator(byhour=range(24), interval=2)
    minutes = MinuteLocator(byminute=range(60), interval=30)
    time_fmt = DateFormatter('%H:%M%p %x')
    fig, ax = plt.subplots()

    for dc in dataCenters:
        plot_dc(dc, dc_dataset_to_graph, ax)
        plotted_dc.append(dc)

    ax.xaxis.set_major_locator(hours)
    ax.xaxis.set_major_formatter(time_fmt)
    ax.xaxis.set_minor_locator(minutes)
    ax.autoscale_view()

    ax.fmt_xdata = DateFormatter('%A %b %d %H:%M%p')
    ax.grid(True)

    fig.autofmt_xdate()

    # Giving scatterplot a title
    plt.title("Data Centers(Value vs. Time)")
    # Making axis labels
    plt.xlabel('Time')
    plt.ylabel('Value')

    # Making a legend for the graph
    plt.legend(['Data Center: ' + dc for dc in plotted_dc])

    plt.show()

# Opening data binary file for reading, hence 'rb', as 'csvfile'.
with open(test_file, 'r') as csvfile:
    # Creates a reader object for later data manipulation
    reader = create_reader(csvfile)

    # Resetting read/write pointer to beginning of file
    csvfile.seek(0)

    # Creating list for graphing data center's dataset
    accepted_records = create_dc_dataset(reader, dataCenters)

    # Graphing Data Center Data
    graph_dataset(accepted_records)
