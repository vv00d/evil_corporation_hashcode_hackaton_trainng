path_b = "input_data/b_basic.in.txt"
path_c = "input_data/c_coarse.in.txt"
path_d = "input_data/d_difficult.in.txt"
from parser import read_file, parse_people
from pprint import pprint

if __name__ == "__main__":
    lines = read_file(path_d)
    clients, ingredients = parse_people(lines)
    pprint(len(ingredients))
