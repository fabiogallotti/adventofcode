from utils import check_double, check_no_decrease

INPUT = range(136818,685980,1)

result = [elem for elem in INPUT if check_no_decrease(str(elem)) and check_double(str(elem))]

print(len(result))