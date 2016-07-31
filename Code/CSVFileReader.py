"""Test File."""

from csv import Sniffer, DictReader

import matplotlib.dates as dt
import matplotlib.pyplot as plt

from matplotlib.dates import HourLocator, MinuteLocator, DateFormatter

# Take file name as raw string
test_file = r'Data(Relevant).csv'

# List of valid data centers
dataCenters = ('I', 'A', 'S')


def format_axes(ax=None):
    """
    Summary: helper function for customizing graph display.

    Create and set major/minor locators for graph's major/minor ticks.
    Format dates/times of x axis.
    Autoscale graph view.
    Show grid on graph.
    """
    # HourLocator creates major ticks every 2 hours in a 24 hour period
    hours = HourLocator(byhour=range(24), interval=2)
    ax.xaxis.set_major_locator(hours)

    # MinuteLocator creates minor ticks every 30 minutes in a 1 hour period
    minutes = MinuteLocator(byminute=range(60), interval=30)
    ax.xaxis.set_minor_locator(minutes)

    # Creates format 'Hour:MinutePeriod Month/Day/Year' x-axis ticks
    # Example: '5:30PM 9/23/15'
    time_fmt = DateFormatter('%H:%M%p %x')
    ax.xaxis.set_major_formatter(time_fmt)

    # Formats x-axis information 'Weekday Month Day Hour:MinutePeriod'
    # Example: 'Tuesday Sep 23 12:15PM'
    ax.fmt_xdata = DateFormatter('%A %b %d %H:%M%p')

    ax.autoscale_view()

    ax.grid(True)


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
        '\tFile has Header: {}\n\tFile Delimiter: "{}"'.format(
            Sniffer().has_header(csvfile.read(1024)),
            file_dialect.delimiter
        )
    )

    # Resets the read/write pointer within the file
    csvfile.seek(0)

    # Creates a DictReader object with the csvfile provided, and the
    # dialect object to define the parameters of the reader instance.
    reader = DictReader(csvfile, dialect=file_dialect)

    # Return DictReader object
    return reader


def create_dataset(reader=None, data_centers=None):
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


def plot_dataset(name=None, dataset=[], ax=None):
    """Function to plot data for a specified Data Center."""
    values = []
    times = []
    for record in dataset[:]:
        if record[0] == name:
            times.append(dt.epoch2num(record[1]))
            values.append(record[2])
            dataset.remove(record)
        else:
            pass
    ax.plot_date(times, values, xdate=True)


def graph_dataset(data_center_list=None, dataset_to_graph=None):
    """
    Summary: function that graphs data center dataset.

    Arguments: 'dc_dataset_to_graph' is a list containing dictionary
    instances holding specific datacenter attributes for value and time
    """
    # List of plotted data centers for dynamic legend creation
    plotted_dc = []

    # Creating figure and axes objects for display
    fig, ax = plt.subplots()

    # Formatting y and x axis for effective plotting
    format_axes(ax)

    # Iterating through list of data centers to be plotted together.
    for dc in data_center_list:
        # For each data center, 'dc', plot it's data from dataset.
        plot_dataset(dc, dataset_to_graph, ax)

        # Add data center to list of plotted dcs for dynamic legend
        plotted_dc.append(dc)

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
    accepted_records = create_dataset(reader, dataCenters)

    # Graphing Data Center Data
    graph_dataset(dataCenters, accepted_records)
