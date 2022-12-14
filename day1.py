

with open("inputs/day1", "r") as f:
    snacks = []
    elf = 0
    for line in f:
        if line == '\n':
            snacks.append(elf)
            elf = 0
        else:
            elf += int(line.rstrip())
    snacks.append(elf)

snacks.sort(reverse=True)

print(f"The elf with the most snakcs has {snacks[0]} calories.")

print(
    f"The top three elves are carrying {sum(snacks[0:3])} calories in total.")
