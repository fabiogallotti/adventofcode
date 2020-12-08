from utils import read_input, calculate_path, find_intersection

data = read_input("input.txt")

path_you = []
path_you = calculate_path(data, data["YOU"], "COM", path_you)

path_san = []
path_san = calculate_path(data, data["SAN"], "COM", path_san)

intersection = find_intersection(path_you, path_san)

path_rel_you = []
path_rel_you = calculate_path(data, data["YOU"], intersection, path_rel_you)

path_rel_san = []
path_rel_san = calculate_path(data, data["SAN"], intersection, path_rel_san)

print(len(path_rel_san+path_rel_you))