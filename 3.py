import re

with open("3.input", "r") as f:
    lines = f.readlines()

symbol_positions = []
stars = dict()
numbers_near_symbols = []

symbol_pattern = r"[^\d\.\n]"
number_pattern = r"\d+"

for line_number, line in enumerate(lines):
    for symbol_match in re.finditer(symbol_pattern, line):
        symbol_positions.append((line_number, symbol_match.start()))
        if symbol_match.group() == "*":
            stars[(line_number, symbol_match.start())] = []

for line_number, line in enumerate(lines):
    for number_match in re.finditer(number_pattern, line):
        symbol_nearby = False
        stars_nearby = set()

        line_min = line_number - 1
        line_max = line_number + 1
        column_min = number_match.start() - 1
        column_max = number_match.end()

        for line_check in range(line_min, line_max + 1):
            for column_check in range(column_min, column_max + 1):
                if (line_check, column_check) in symbol_positions:
                    symbol_nearby = True
                    if (line_check, column_check) in stars:
                        stars_nearby.add((line_check, column_check))

        if symbol_nearby:
            numbers_near_symbols.append(int(number_match.group()))

        for star in stars_nearby:
            stars[star].append(int(number_match.group()))

print(sum(numbers_near_symbols))
print(
    sum(numbers[0] * numbers[1] for star, numbers in stars.items() if len(numbers) == 2)
)
