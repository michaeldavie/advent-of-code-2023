with open("1.input", "r") as f:
    lines = f.readlines()

line_ints = []

for line in lines:
    first_digit = next((c for c in line if c.isdigit()))
    last_digit = next((c for c in line[::-1] if c.isdigit()))
    line_ints.append(int(first_digit + last_digit))

print(sum(line_ints))

#################################

import re

digit_map = {
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

pattern = re.compile(
    r"(?=(one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9))"
)

line_ints = []

for line in lines:
    line_digits = pattern.findall(line)

    def word_to_num(digit: str):
        return digit if digit.isdigit() else digit_map[digit]

    first_digit = word_to_num(line_digits[0])
    last_digit = word_to_num(line_digits[-1])

    line_ints.append(int(first_digit + last_digit))

print(sum(line_ints))
