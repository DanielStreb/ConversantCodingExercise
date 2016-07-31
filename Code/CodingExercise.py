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
    my_regex = r'[^A|^I|^S][ A| S| I]?[ A$| I$| S$]'

    while True:
        dc_string = input("Data Centers to graph: ")
        if re.search(my_regex, dc_string + ' '):
            break
        else:
            print("Valid DCs: 'I' 'A' 'S'")

    data_centers = set(dc_string.split())
    print(data_centers)

    dp = DataParser(test_file, data_centers)
    dataset = dp.get_dataset()
    gr = Grapher(dataset, data_centers)
    gr.graph_dataset()

if __name__ == "__main__":
    # execute only if run as a script
    main()
