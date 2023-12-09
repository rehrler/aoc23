def get_number_from_line(line_str: str) -> int:
    numbers = []
    for character in line_str:
        if character.isdigit():
            numbers.append(character)
    return int(numbers[0] + numbers[-1])


def get_number_from_word(line_str: str) -> int:
    numbers = []
    words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    i = 0
    while i < len(line_str):
        # check for digit
        if line_str[i].isdigit():
            numbers.append(line_str[i])
        else:
            for word in words.items():
                if i + len(word[0]) < len(line_str) + 1:
                    if line_str[i : i + len(word[0])] == word[0]:
                        numbers.append(word[1])
                        break
        i += 1
    if len(numbers) > 1:
        return int(numbers[0] + numbers[-1])
    return int(numbers[0] + numbers[0])


FILE_NAME = "../data/day01.txt"

with open(FILE_NAME, "r", encoding="utf-8") as file_o:
    lines = file_o.readlines()

# part 1
SUM_PART1 = 0
for line in lines:
    SUM_PART1 += get_number_from_line(line.rstrip())

print(f"Part 1: {SUM_PART1}")

# part 2
SUM_PART2 = 0
for line in lines:
    SUM_PART2 += get_number_from_word(line.rstrip())

print(f"Part 2: {SUM_PART2}")
