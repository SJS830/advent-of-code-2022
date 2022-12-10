register_values = [1]
screen = ["."] * 240
num_ops = 0

for line in open("input.txt").readlines():
    line = line.strip().split()

    if line[0] == "noop":
        register_values.append(int(register_values[-1]))

        if abs(num_ops % 40 - register_values[-1]) <= 1:
            screen[num_ops] = "#"

        num_ops += 1
    else:
        register_values.append(int(register_values[-1]))

        if abs(num_ops % 40 - register_values[-1]) <= 1:
            screen[num_ops] = "#"

        num_ops += 1

        if abs(num_ops % 40 - register_values[-1]) <= 1:
            screen[num_ops] = "#"

        register_values.append(int(register_values[-1]) + int(line[1]))

        num_ops += 1

totals = 0

for n in [20, 60, 100, 140, 180, 220]:
    totals += n * register_values[n - 1]

print("Part 1: ", totals)

screen = "".join(screen)

for i in range(10):
    print(screen[40*i:40*i+40])
