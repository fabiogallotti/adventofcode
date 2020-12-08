def read_input(filename):
    with open(filename, "r") as f:
        return [ int(elem) for elem in f.read().split(",") ]


def calculate(data, ainput):
    i = 0
    while True:
        op_code = int(str(data[i])[-2:])
        modes = str(data[i])[0:-2][::-1]

        if len(modes) == 0:
            modes = "000" 
        if len(modes) == 1:
            modes += "00"       
        if len(modes) == 2:
            modes+="0"

        if op_code == 99:
            return data

        one = data[i+1]
        two = data[i+2]
        three = data[i+3]

        one_modes = (data[one] if not int(modes[0]) else one)

        try:
            two_modes = (data[two] if not int(modes[1]) else two)
        except:
            pass
       
        if op_code == 1:
            result = one_modes + two_modes 
            try:
                data[three] = result
            except:
                pass
            i += 4 
        elif op_code == 2:
            result = one_modes * two_modes
            try:
                data[three] = result
            except:
                pass
            i += 4
        elif op_code == 3:
            if not int(modes[0]):
                data[one] = ainput
            else:
                one = ainput
            i += 2
        elif op_code == 4:
            if not int(modes[0]):
                print(data[one])
            else:
                print(one)
            i += 2
        elif op_code == 5:
            if one_modes != 0:
                i = two_modes
            else:
                i += 3
        elif op_code == 6:
            if one_modes == 0:
                i = two_modes
            else:
                i += 3
        elif op_code == 7:
            if one_modes < two_modes:
                if not int(modes[2]):
                    data[three] = 1
                else:
                    three = 1
            else:
                if not int(modes[2]):
                    data[three] = 0
                else:
                    three = 0
            i += 4
        elif op_code == 8:
            if one_modes == two_modes:
                if not int(modes[2]):
                    data[three] = 1
                else:
                    three = 1
            else:
                if not int(modes[2]):
                    data[three] = 0
                else:
                    three = 0
            i += 4


    return data

           


data = read_input("input.txt")
result1 = calculate(data, 1)

data = read_input("input.txt")
result2 = calculate(data, 5)

