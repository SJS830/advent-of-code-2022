lines = open("input.txt").read().split("\n")
lines = [line for line in lines if line]

"""
sum = 0

for line in lines:
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    duplicates = [a for a in compartment1 if a in compartment2]
    duplicates = list(set(duplicates))
    print(compartment1, compartment2)
    print(duplicates)
    for duplicate in duplicates:
        if ord("a") <= ord(duplicate) <= ord("z"):
            sum += ord(duplicate) - ord("a") + 1
        elif ord("A") <= ord(duplicate) <= ord("Z"):
            sum += ord(duplicate) - ord("A") + 27
    print(sum)
"""

sum = 0
for i in range(0, len(lines), 3):
    compartments = lines[i:i+3]
    common = [x for x in compartments[0] if x in compartments[1] and x in compartments[2]][0]
    print(compartments, common)
    if ord("a") <= ord(common) <= ord("z"):
        sum += ord(common) - ord("a") + 1
    elif ord("A") <= ord(common) <= ord("Z"):
        sum += ord(common) - ord("A") + 27
    print(sum)
