#!/usr/bin/env python3

import math
import itertools
from operator import add

puzzle_input = 277678


def manhattan_distance(node, goal_node):
    return abs(goal_node[0] - node[0]) + abs(goal_node[1] - node[1])


def sum_neighbors(matrix, position):
    around = [
        (0, 1),
        (1, 1),
        (1, 0),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 1)
    ]

    result = 0

    for neighbor in around:
        coordinates = list(map(add, neighbor, position))
        try:
            if matrix[coordinates[0]][coordinates[1]]:
                result += matrix[coordinates[0]][coordinates[1]]
        except:
            # do not exist
            pass

    return result


def spiral(number, neighbor=False):
    # initialize matrix
    size = math.ceil(math.sqrt(number))
    matrix = [[None for _ in range(size)] for _ in range(size)]

    # initialize start
    start = position = (size // 2, size // 2)
    matrix[position[0]][position[1]] = 1

    directions = itertools.cycle([
        (0, 1),  # right
        (-1, 0),  # up
        (0, -1),  # left
        (1, 0)  # down
    ])

    # start with right
    next_direction = next(directions)
    previous_direction = (0, 0)

    if neighbor:
        i = 1
    else:
        i = 2

    while i <= number:
        coordinates = list(map(add, next_direction, position))
        if matrix[coordinates[0]][coordinates[1]]:
            # not availlable, keep going in previous direction
            while matrix[coordinates[0]][coordinates[1]] and i <= number:
                coordinates = list(map(add, previous_direction, position))
                if neighbor:
                    i = sum_neighbors(matrix, coordinates)
                matrix[coordinates[0]][coordinates[1]] = i
                if not neighbor:
                    i += 1
                position = coordinates
                # we will try again
                coordinates = list(map(add, next_direction, position))

        if i > number:
            if neighbor:
                return i
            else:
                # avoid messing up here
                break

        # we got a slot
        if neighbor:
            i = sum_neighbors(matrix, coordinates)
        if i > number:
            # only on neighbor case
            return i

        matrix[coordinates[0]][coordinates[1]] = i
        if not neighbor:
            i += 1
        position = coordinates

        # changing directions
        previous_direction = next_direction
        next_direction = next(directions)

    # only in not neighbor case
    return manhattan_distance(start, position)


print(spiral(puzzle_input))
print(spiral(puzzle_input, True))
