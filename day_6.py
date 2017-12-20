#!/usr/bin/env python3

puzzle_input = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"


def loop(puzzle):
    banks = list(map(int, puzzle.split("\t")))

    max_value = max(banks)
    max_index = banks.index(max_value)

    # deplete it
    banks[max_index] = 0

    index = 0
    reach_index = 0
    skip = True
    while True:
        if skip and reach_index <= max_index:
            if index == len(banks) - 1:
                index = 0
            else:
                index += 1
            reach_index += 1
        else:
            skip = False
            banks[index] += 1
            if index == len(banks) - 1:
                index = 0
            else:
                index += 1
            max_value -= 1

            if max_value == 0:
                break

    return banks


def part_1(puzzle, part2=False):
    iteration = 1
    seen = list([puzzle])

    while True:
        puzzle = "\t".join(map(str, loop(puzzle)))
        if puzzle in seen:
            if part2:
                return iteration - seen.index(puzzle)
            else:
                return iteration
        else:
            seen.append(puzzle)
            iteration += 1

tests = "0	2	7	0"

assert part_1(tests) == 5
assert part_1(tests, True) == 4

print(part_1(puzzle_input))
print(part_1(puzzle_input, True))
