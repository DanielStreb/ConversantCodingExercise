"""CodingExercise.py."""

from DataParser import DataParser
from Grapher import Grapher


def main():
    """Main Function."""
    # Take file name as raw string
    test_file = r'Data(Relevant).csv'

    # List of valid data centers
    data_centers = ('I', 'A', 'S')

    dp = DataParser(test_file, data_centers)
    dataset = dp.get_dataset()
    gr = Grapher(dataset, data_centers)
    gr.graph_dataset()

if __name__ == "__main__":
    # execute only if run as a script
    main()
