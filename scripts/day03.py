import numpy as np


def load_input(filename: str) -> np.ndarray:
    with open(filename, "r", encoding="utf8") as file_open:
        lines = file_open.readlines()
    cols, rows = len(lines[0]), len(lines)
    array = np.zeros((rows, cols))
    for idx_row, line in enumerate(lines):
        for idx_col, char in enumerate(line.rstrip()):
            if char.isdigit():
                array[idx_row, idx_col] = int(char)
            elif char == ".":
                array[idx_row, idx_col] = -2
            else:
                array[idx_row, idx_col] = -1
    return array


def check_dir(direction: str, data: np.ndarray, idx_row: int, idx_col: int) -> int:
    if direction == "left":
        left = 0
        go_left = True
        while go_left:
            if idx_col - left - 1 >= 0 and data[idx_row, idx_col - left - 1] >= 0:
                left += 1
            else:
                go_left = False
        return left
    if direction == "right":
        right = 0
        go_right = True
        while go_right:
            if (
                idx_col + right + 1 < data.shape[1]
                and data[idx_row, idx_col + right + 1] >= 0
            ):
                right += 1
            else:
                go_right = False
        return right
    return 0


def apply_mask_part1(data: np.ndarray, i: int, j: int) -> int:
    sum_engine_numbers = []
    for idx_row in [i - 1, i, i + 1]:
        for idx_col in [j - 1, j, j + 1]:
            if not (idx_row == i and idx_col == j):
                if data[idx_row, idx_col] != -2:
                    # check left
                    left = check_dir("left", data, idx_row, idx_col)
                    # check right
                    right = check_dir("right", data, idx_row, idx_col)
                    digits = data[idx_row, idx_col - left : idx_col + right + 1]
                    number = ""
                    for digit in digits:
                        number += str(int(digit))
                    sum_engine_numbers.append(int(number))
                    data[idx_row, idx_col - left : idx_col + right + 1] = -2
    summed = 0
    for number in sum_engine_numbers:
        summed += number
    return summed


def solve_part1(input_data_part1: np.ndarray) -> int:
    engine_nb_set = 0
    for i in range(input_data_part1.shape[0]):
        for j in range(input_data_part1.shape[1]):
            if input_data_part1[i, j] == -1:
                engine_nb_set += apply_mask_part1(input_data_part1, i, j)
    return engine_nb_set


if __name__ == "__main__":
    input_data = load_input("../data/day03.txt")

    # part 1
    sum_part1 = solve_part1(input_data)
    print(f"Part 1: {sum_part1}")
    print("done")
