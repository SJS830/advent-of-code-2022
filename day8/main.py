grid = [line.strip() for line in open("input.txt").read().splitlines()]

totalVisibleTrees = 0
maxScenic = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        visible = False
        ss = [0, 0, 0, 0]

        if x in [0, len(grid[0]) - 1] or y in [0, len(grid) - 1]:
            visible = True

        for dx in range(x - 1, -1, -1):
            ss[0] += 1

            if grid[y][dx] >= grid[y][x]:
                break
        else:
            visible = True

        for dx in range(x + 1, len(grid[0])):
            ss[1] += 1

            if grid[y][dx] >= grid[y][x]:
                break
        else:
            visible = True

        for dy in range(y - 1, -1, -1):
            ss[2] += 1

            if grid[dy][x] >= grid[y][x]:
                break
        else:
            visible = True

        for dy in range(y + 1, len(grid)):
            ss[3] += 1

            if grid[dy][x] >= grid[y][x]:
                break
        else:
            visible = True

        if visible:
            totalVisibleTrees += 1

        maxScenic = max(maxScenic, ss[0] * ss[1] * ss[2] * ss[3])

print("Part 1: ", totalVisibleTrees)
print("Part 2: ", maxScenic)
