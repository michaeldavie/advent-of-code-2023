import re

with open("2.input", "r") as f:
    lines = f.readlines()

limits = {"red": 12, "green": 13, "blue": 14}

all_games = set()
impossible_games = set()
game_powers = []

for line in lines:
    match = re.search(r"Game (\d+):(.*)", line)
    game_number = int(match.group(1))
    all_games.add(game_number)

    game_max = {"red": 0, "green": 0, "blue": 0}
    draws = [d.lstrip() for d in match.group(2).split(";")]

    for d in draws:
        for c in d.split(", "):
            colour = re.search(r"([a-z]+)", c).group(1)
            count = int(re.search(r"(\d*)", c).group(1))
            if count > limits[colour]:
                impossible_games.add(game_number)
            if count > game_max[colour]:
                game_max[colour] = count

    game_powers.append(game_max["red"] * game_max["green"] * game_max["blue"])

print(sum(all_games) - sum(impossible_games))
print(sum(game_powers))
