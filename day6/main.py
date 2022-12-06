input = open("input.txt").read()

def first_n_unique(n):
    for i in range(len(input)):
        if len(set(input[i:i+n])) == n:
            return i + n

print("Part 1: ", first_n_unique(4))
print("Part 2: ", first_n_unique(14))
