import re

with open("4.input", "r") as f:
    lines = f.readlines()

total_score = 0

for line in lines:
    sections = re.split(":|\|", line)
    winning_numbers = set(re.findall(r"\d+", sections[1]))
    ticket_numbers = set(re.findall(r"\d+", sections[2]))
    matching_numbers = winning_numbers.intersection(ticket_numbers)
    if len(matching_numbers) > 0:
        total_score += 2 ** (len(matching_numbers) - 1)

print(total_score)
