input = open("input.txt").read()
input = input.split("\n")

"""
score = 0
for round in input:
    if not round:
        continue

    round = round.split(" ")
    round[0] = ord(round[0]) - ord("A")
    round[1] = ord(round[1]) - ord("X")

    score += round[1] + 1

    if round[0] == round[1]:
        score += 3
    elif [2, 0, 1][round[1]] == round[0]:
        score += 6

    print(round, score)
"""

score = 0
for round in input:
    if not round:
        continue

    round = round.split(" ")
    round[0] = ord(round[0]) - ord("A")
    round[1] = ord(round[1]) - ord("X")

    score += 3 * round[1]

    if round[1] == 0:
        score += [3, 1, 2][round[0]]
    elif round[1] == 1:
        score += round[0] + 1
    elif round[1] == 2:
        score += [2, 3, 1][round[0]]

    print(round, score)
