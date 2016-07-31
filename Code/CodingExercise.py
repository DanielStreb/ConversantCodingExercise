"""CodingExercise.py."""

from DataParser import DataParser
from Grapher import Grapher

# Take file name as raw string
test_file = r'Data(Relevant).csv'

# List of valid data centers
dataCenters = ('A', 'S')

dp = DataParser(test_file, dataCenters)
dataset = dp.get_dataset()
gr = Grapher(dataset, dataCenters)
gr.graph_dataset()
