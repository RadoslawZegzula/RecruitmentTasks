import argparse

parser = argparse.ArgumentParser(description = 'Gui to query person database')
parser.add_argument("category", help = "Category of query")
parser.add_argument("-f", "--firstOptional", help = "First optional argument")
parser.add_argument("-s", "--secondOptional", help = "Second optional argument")
args = parser.parse_args()
