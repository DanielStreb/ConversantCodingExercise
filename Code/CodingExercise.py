"""CodingExercise.py."""
import re
from DataParser import DataParser
from Grapher import Grapher


def main():
    """Main Function."""
    # Take file name as raw string
    test_file = r'Data(Relevant).csv'

    # Regular expression that only accepts strings with valid DC
    # names 'I', 'A', and 'S' separated by spaces
    my_regex = r'^[IAS]$'

    dcs = []

    print('Enter data centers to be graphed')

    while True:
        dc_string = input("\t> ")
        if re.search(my_regex, dc_string):
            dcs.append(dc_string)
        elif dc_string == '':
            break
        else:
            print("Valid DCs: 'I' 'A' 'S'")

    dcs = set(dcs)

    dp = DataParser(test_file, dcs)
    dataset = dp.get_dataset()
    gr = Grapher(dataset, dcs)
    gr.graph_dataset()

if __name__ == "__main__":
    # execute only if run as a script
    main()
