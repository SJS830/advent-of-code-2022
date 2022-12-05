"""
total = 0

for line in open("input.txt").readlines():
    line = line.strip()

    first, second = line.split(",")
    first, second = first.split("-"), second.split("-")

    if int(first[0]) <= int(second[0]) <= int(second[1]) <= int(first[1]) or int(second[0]) <= int(first[0]) <= int(first[1]) <= int(second[1]):
        print(first, second)
        total += 1

print(total)
"""

total = 0

for line in open("input.txt").readlines():
    line = line.strip()

    first, second = line.split(",")
    first, second = first.split("-"), second.split("-")

    #it works
    if any([x in range(int(second[0]), int(second[1]) + 1) for x in range(int(first[0]), int(first[1]) + 1)]):
        print(first, second)
        total += 1

print(total)
