def string_representation_length(data):
    return sum(len(elem[0]) for elem in data)


def difference_string_memory(data):
    return string_representation_length(data) - memory_representation_length(data)


def remove_double_quotes(elem):
    return elem[1 : len(elem) - 1]

def memory_representation_length(data):
    memory_length = 0
    for elem in data:

        if len(elem[0]) > 2:

            memory_elem = remove_double_quotes(elem[0])

            i = 1
            while i <= len(memory_elem):
                if memory_elem[i - 1] == "\\":
                    if memory_elem[i] == "x":
                        i += 3
                    elif memory_elem[i] in ["\\", '"']:
                        i += 1
                memory_length += 1
                i += 1
    return memory_length
