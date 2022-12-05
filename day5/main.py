input = open("input.txt").read()

config, moves = input.split("\n\n")

columns = []

for line in config.split("\n"):
    line = line.strip()

    for i in range(0, len(line) // 4 + 1):
        item = line[i*4+1:i*4+2]

        if len(columns) < i + 1:
            columns.append([item])
        else:
            columns[i].append(item)

for i in range(len(columns)):
    columns[i] = [x for x in columns[i][:-1] if len(x.strip()) > 0]

for line in moves.split("\n"):
    if not line:
        continue

    line = line.split(" ")
    amount, src, dst = int(line[1]), int(line[3]), int(line[5])
    src -= 1
    dst -= 1

    """
    for i in range(amount):
        if len(columns[src]) == 0:
            break

        t = columns[src][0]
        columns[src] = columns[src][1:]
        columns[dst] = [t] + columns[dst]
    """

    t = columns[src][:amount]
    columns[src] = columns[src][amount:]
    columns[dst] = t + columns[dst]

for column in columns:
    print(column[0])
