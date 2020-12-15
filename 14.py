from common import lines
import re


def binary_expand(value: int) -> str:
    return format(value, "b").zfill(36)


def apply_value_mask(mask: str, value: int) -> int:
    masked_value = "".join(
        mbit if mbit in "01" else vbit for mbit, vbit in zip(mask, binary_expand(value))
    )
    return int(masked_value, 2)


def apply_offset_mask(mask: str, offset: int) -> list[int]:
    offsets = [""]
    for mbit, obit in zip(mask, binary_expand(offset)):
        if mbit == "0":
            offsets = [off + obit for off in offsets]
        if mbit == "1":
            offsets = [off + "1" for off in offsets]
        if mbit == "X":
            offsets = [off + x for off in offsets for x in "01"]
    return [int(off, 2) for off in offsets]


def simulate(instructions, mode):
    mem = {}
    mask = ""

    for instruction in instructions:
        location, value = instruction.split(" = ")
        if location == "mask":
            mask = value
        else:
            offset = int(re.fullmatch(r"mem\[(\d+)]", location).group(1))
            value = int(value)
            if mode == 1:
                mem[offset] = apply_value_mask(mask, value)
            if mode == 2:
                for off in apply_offset_mask(mask, offset):
                    mem[off] = value

    return sum(mem.values())


instructions = lines("14")

part1 = simulate(instructions, mode=1)
print(f"{part1=}")

part2 = simulate(instructions, mode=2)
print(f"{part2=}")
