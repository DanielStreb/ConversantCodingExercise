"""CodingExercise.py."""
import re
from DataParser import DataParser
from DatasetDisplay import DatasetDisplay


def main():
    """Parse and graph data provided in Data(Relevant).csv file."""
    # Take file name as raw string
    data_file = r'Data(Relevant).csv'

    # Regular expression that only accepts strings with valid DC
    # names 'I', 'A', and 'S'.
    my_regex = r'^[IAS]$'

    # List to store user inputed data center names
    dc_name_list = []

    print('Enter data centers to be graphed')

    while True:  # Loop until user enters valid Data center name
        user_input = input("\t> ")
        # Checking if user_input matches defined regular expression
        if re.search(my_regex, user_input):
            dc_name_list.append(user_input)
        # Breaking from loop when user enters nothing.
        elif user_input == '':
            break
        else:
            print("Valid dc_name_list: 'I' 'A' 'S'")

    # Modifying data center name list to only have unique dc names
    dc_name_list = set(dc_name_list)

    # Creating data parser to parse data_file, returning records
    # corresponding to the data centers specified in the dc_name_list
    dc_data_parser = DataParser(data_file, dc_name_list)
    dc_dataset = dc_data_parser.get_dataset()

    # Creating a DatasetDisplay object for plotting and displaying
    # the data center dataset.
    dc_data_display = DatasetDisplay(dc_dataset, dc_name_list)
    dc_data_display.show_plot()

if __name__ == "__main__":
    # execute only if run as a script
    main()
