def read_input(file):
    with open(file) as f:
        return f.read()


data = read_input("input.txt")

wide = 25
tall = 6

layers = [data[i * wide * tall : (i + 1) * wide * tall] for i in range(len(data) // (wide * tall))]

result = [None] * wide * tall
print(result)

for column in range(wide * tall):
    for row in range(len(layers)):
        if (layers[row][column] == "0" or layers[row][column] == "1") and result[column] is None:
            result[column] = layers[row][column]

result_layers = [result[i * wide : (i + 1) * wide] for i in range(tall)]

for elem in result_layers:
    print(elem)


# 0110001100100101110011110
# 1001010010101001001000010
# 1001010000110001001000100
# 1111010000101001110001000
# 1001010010101001000010000
# 1001001100100101000011110
# ACKPZ
