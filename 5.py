import re

seed_results = []

with open("5.input", "r") as f:
    seeds = [int(s) for s in re.findall(r"\d+", f.readline())]
    maps = [map.strip().split("\n")[1:] for map in f.read().split("\n\n")]

    for seed in seeds:
        for map in maps:
            for line in map:
                line_values = [int(x) for x in line.split(" ")]
                if seed in range(line_values[1], line_values[1] + line_values[2] + 1):
                    seed = line_values[0] + seed - line_values[1]
                    break
        seed_results.append(seed)

    print(min(seed_results))
