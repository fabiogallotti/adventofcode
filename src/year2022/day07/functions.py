import contextlib

from pydantic import BaseModel


class File(BaseModel):
    size: int
    name: str


class Dir(BaseModel):
    name: str
    parent: str | None = None
    dirs: list["Dir"] | None = None
    files: list[File] | None = None

    def get_total_size(self):
        size = sum(f.size for f in self.files)
        if self.dirs:
            size += sum(d.get_total_size() for d in self.dirs)

        return size


def preprocessing(data):
    dirs = {}
    current_dir = None
    for e in data:
        if e[0] == "$" and e[1] == "cd":
            if e[2] == "..":
                current_dir = dirs[f"{current_dir.parent}"]

            elif current_dir is None:
                dirs[e[2]] = Dir(name=e[2], parent=None, dirs=[], files=[])
                current_dir = dirs[e[2]]
            else:
                full_name = f"{current_dir.name}/{e[2]}"
                dirs[full_name] = Dir(name=full_name, parent=current_dir.name, dirs=[], files=[])
                current_dir.dirs.append(dirs[full_name])
                current_dir = dirs[full_name]

        else:
            with contextlib.suppress(ValueError):
                if int(e[0]):
                    current_dir.files.append(File(size=int(e[0]), name=e[1]))

    return dirs


def part_1(data):
    dirs = preprocessing(data)
    return sum(d.get_total_size() for d in dirs.values() if d.get_total_size() <= 100000)


def part_2(data):
    dirs = preprocessing(data)

    total = dirs["/"].get_total_size()
    min_size = abs(70000000 - 30000000 - total)
    candidates = [d.get_total_size() for d in dirs.values() if d.get_total_size() > min_size]

    return min(candidates)
