from year2020.day04.functions import (
    preprocessing,
    valid_byr,
    valid_ecl,
    valid_eyr,
    valid_hcl,
    valid_hgt,
    valid_iyr,
    valid_passport,
    valid_pid,
    validate_data_passport,
)


def test_preprocessing():
    data = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
    ]
    assert preprocessing(data) == [
        {
            "ecl": "gry",
            "pid": "860033327",
            "eyr": "2020",
            "hcl": "#fffffd",
            "byr": "1937",
            "iyr": "2017",
            "cid": "147",
            "hgt": "183cm",
        }
    ]


def test_valid_passport():
    data = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        "",
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
    ]
    passports = preprocessing(data)

    assert sum(1 for passport in passports if valid_passport(passport)) == 2


def test_valid_byr():
    assert valid_byr(2002) == True
    assert valid_byr(2003) == False


def test_valid_iyr():
    assert valid_iyr(2000) == False
    assert valid_iyr(2015) == True


def test_valid_eyr():
    assert valid_eyr(1993) == False
    assert valid_eyr(2025) == True


def test_valid_hgt():
    assert valid_hgt("60in") == True
    assert valid_hgt("190cm") == True
    assert valid_hgt("190in") == False
    assert valid_hgt("190") == False


def test_valid_hcl():
    assert valid_hcl("#123abc") == True
    assert valid_hcl("#123abz") == False
    assert valid_hcl("123abc") == False


def test_valid_ecl():
    assert valid_ecl("brn") == True
    assert valid_ecl("wat") == False


def test_valid_pid():
    assert valid_pid("000000001") == True
    assert valid_pid("0123456789") == False


def test_validate_data_passport():
    data = [
        "eyr:1972 cid:100",
        "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
        "",
        "iyr:2019",
        "hcl:#602927 eyr:1967 hgt:170cm",
        "ecl:grn pid:012533040 byr:1946",
        "",
        "hcl:dab227 iyr:2012",
        "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
        "",
        "hgt:59cm ecl:zzz",
        "eyr:2038 hcl:74454a iyr:2023",
        "pid:3556412378 byr:2007",
        "",
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
        "hcl:#623a2f",
        "",
        "eyr:2029 ecl:blu cid:129 byr:1989",
        "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "",
        "hcl:#888785",
        "hgt:164cm byr:2001 iyr:2015 cid:88",
        "pid:545766238 ecl:hzl",
        "eyr:2022",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    ]
    passports = preprocessing(data)

    assert sum(1 for passport in passports if validate_data_passport(passport)) == 4
