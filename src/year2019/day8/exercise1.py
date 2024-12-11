def read_input(file):
    with open(file) as f:
        return f.read()


data = read_input("input.txt")

wide = 25
tall = 6
min_zeros = 150

layers = [data[i * wide * tall : (i + 1) * wide * tall] for i in range(len(data) // (wide * tall))]

for layer in layers:
    if layer.count("0") < min_zeros:
        min_zeros = layer.count("0")
        layer_num = layers.index(layer)

ones = layers[7].count("1")
twos = layers[7].count("2")

print(ones * twos)
