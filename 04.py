import re

with open("input/04.txt") as f:
    passports = [
        dict(field.split(":") for field in passport.split())
        for passport in f.read().split("\n\n")
    ]


def valid1(passport):
    return {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= set(passport.keys())


def valid2(passport):
    return valid1(passport) and (
        1920 <= int(passport["byr"]) <= 2002
        and 2010 <= int(passport["iyr"]) <= 2020
        and 2020 <= int(passport["eyr"]) <= 2030
        and (
            passport["hgt"].endswith("cm")
            and 150 <= int(passport["hgt"][:-2]) <= 193
            or passport["hgt"].endswith("in")
            and 59 <= int(passport["hgt"][:-2]) <= 76
        )
        and bool(re.fullmatch(r"#[0-9a-f]{6}", passport["hcl"]))
        and passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        and bool(re.fullmatch(r"[0-9]{9}", passport["pid"]))
    )


part1 = sum(map(valid1, passports))
print(f"{part1=}")

part2 = sum(map(valid2, passports))
print(f"{part2=}")
