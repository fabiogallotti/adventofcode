from utils import check_double, check_no_decrease, check_no_larger_group

INPUT = range(136818,685980,1)

result = [elem for elem in INPUT if check_no_decrease(str(elem)) and check_double(str(elem))]

result2 = [elem for elem in result if check_no_larger_group(str(elem))]

print(len(result2))