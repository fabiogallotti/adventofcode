from pydantic import BaseModel


class File(BaseModel):
    value: int
    times: int


class Free(BaseModel):
    value: str
    times: int


def preprocessing(data):
    row = data[0]

    files = [row[i] for i in range(len(row)) if i % 2 == 0]
    free = [row[i] for i in range(len(row)) if i % 2 != 0]
    files_expanded = [File(value=i, times=int(files[i])) for i in range(len(files))]
    free_expanded = [Free(value=".", times=int(free[i])) for i in range(len(free))]

    complete_list = [item for pair in zip(files_expanded, free_expanded) for item in pair]

    complete_list.extend(files_expanded[len(free_expanded) :])

    return complete_list


def part_1(data):
    complete_list = preprocessing(data)
    complete_list = [
        f.__class__(value=f.value, times=1) for f in complete_list for _ in range(f.times)
    ]

    new_complete_list = complete_list.copy()

    for i in range(len(complete_list)):
        for j in range(len(complete_list) - 1, i, -1):
            free = new_complete_list[i]
            full = new_complete_list[j]
            if (
                isinstance(free, Free)
                and free.times > 0
                and isinstance(full, File)
                and full.times > 0
            ):
                new_complete_list[i] = File(value=full.value, times=1)
                new_complete_list[j] = Free(value=".", times=1)

    new_files = [f for f in new_complete_list if isinstance(f, File)]

    return sum(new_files[i].value * i for i in range(len(new_files)))


def part_2(data):
    complete_list = preprocessing(data)
    new_complete_list = complete_list.copy()

    max_full = new_complete_list[-1].value + 1
    full = new_complete_list[-1]

    for j in range(len(complete_list) - 1, 0, -1):
        for i in range(j):
            free = new_complete_list[i]
            full = new_complete_list[j]
            if (
                isinstance(full, File)
                and full.times > 0
                and full.value == max_full - 1
                and isinstance(free, Free)
                and free.times == full.times
            ):
                new_complete_list[i] = File(value=full.value, times=full.times)
                new_complete_list[j] = Free(value=".", times=full.times)
                max_full -= 1
                break
            elif (
                isinstance(full, File)
                and full.times > 0
                and full.value == max_full - 1
                and isinstance(free, Free)
                and free.times > full.times
            ):
                new_complete_list[i] = File(value=full.value, times=full.times)
                new_complete_list[j] = Free(value=".", times=full.times)

                times = free.times - full.times
                if times > 0:
                    new_complete_list.insert(i + 1, Free(value=".", times=times))
                max_full -= 1
                break
            elif (
                isinstance(full, File)
                and full.times > 0
                and full.value == max_full - 1
                and i == j - 1
            ):
                max_full -= 1
                break

    new_complete_list = [
        f.__class__(value=f.value, times=1) for f in new_complete_list for _ in range(f.times)
    ]

    return sum(
        new_complete_list[i].value * i
        for i in range(len(new_complete_list))
        if isinstance(new_complete_list[i], File)
    )
