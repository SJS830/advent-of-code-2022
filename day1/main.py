input = open("input.txt").read()
input = input.split("\n\n")

calories = [sum([int(f) if f else 0 for f in elf.split("\n")]) for elf in input]
calories.sort()

print("Part 1: ", calories[-1])
print("Part 2: ", sum(calories[-3:]))
