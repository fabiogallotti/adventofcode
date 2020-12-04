def string_representation_length(data):
    return sum(len(elem) for elem in data)


def difference_string_memory(data):
    return string_representation_length(data) - memory_representation_length(data)


def remove_double_quotes(elem):
    return elem[1: len(elem) - 1]


def memory_representation_length(data):
    memory_length = 0
    for elem in data:

        if len(elem) > 2:

            memory_elem = remove_double_quotes(elem)

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


def new_representation_length(data):
    new_length = 0
    for elem in data:
        for i in range(1, len(elem) + 1):
            if elem[i - 1] in ["\\", '"']:
                new_length += 1
            new_length += 1
        new_length += 2
    return new_length


def difference_new_string(data):
    return new_representation_length(data) - string_representation_length(data)
