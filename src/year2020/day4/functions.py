import string

required_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}


def preprocessing(data):
    data = [elem.split(" ") for elem in data]

    passports = [[]]
    i = 0
    for elem in data:
        if elem[0] != "":
            passports[i].extend(elem)
        else:
            i += 1
            passports.append([])

    dict_passports = []
    for passport in passports:
        dict_ = {}
        for elem in passport:
            key, value = elem.split(":")
            dict_[key] = value
        dict_passports.append(dict_)

    return dict_passports

def valid_passport(passport):
    return required_fields <= passport.keys()

def valid_byr(byr):
    return 1920 <= byr <= 2002


def valid_iyr(iyr):
    return 2010 <= iyr <= 2020


def valid_eyr(eyr):
    return 2020 <= eyr <= 2030


def valid_hgt(hgt):
    num = int(hgt[: len(hgt) - 2])
    if hgt[-2:] == "in":
        return 59 <= num <= 76
    elif hgt[-2:] == "cm":
        return 150 <= num <= 193
    return False


def valid_hcl(hcl):
    if len(hcl) == 7 and hcl[0] == "#":
        allowed = set(string.ascii_lowercase[:6] + string.digits)

        return set(hcl[1:]) <= allowed

    return False


def valid_ecl(ecl):
    return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def valid_pid(pid):
    if len(pid) == 9:
        allowed = set(string.digits)

        return set(pid) <= allowed
    return False


def validate_data_passport(passport):
    if valid_passport(passport):
        return (valid_byr(int(passport["byr"]))
            and valid_iyr(int(passport["iyr"]))
            and valid_eyr(int(passport["eyr"]))
            and valid_hgt(passport["hgt"])
            and valid_hcl(passport["hcl"])
            and valid_ecl(passport["ecl"])
            and valid_pid(passport["pid"])
        )