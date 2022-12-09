moves = open("input.txt").readlines()

def simulate_rope(num_knots):
    knot_positions = [(0, 0)] * num_knots
    visited_positions_tail = [(0, 0)]

    offsets = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    for move in moves:
        move = move.strip()
        dir, amount = move.split(" ")

        for n in range(int(amount)):
            offset = offsets[dir]

            knot_positions[-1] = (knot_positions[-1][0] + offset[0], knot_positions[-1][1] + offset[1])

            for i in range(len(knot_positions) - 2, -1, -1):
                if abs(knot_positions[i + 1][0] - knot_positions[i][0]) > 1 or abs(knot_positions[i + 1][1] - knot_positions[i][1]) > 1:
                    U = 0
                    R = 0

                    if knot_positions[i + 1][0] > knot_positions[i][0]:
                        R = 1
                    elif knot_positions[i + 1][0] < knot_positions[i][0]:
                        R = -1

                    if knot_positions[i + 1][1] > knot_positions[i][1]:
                        U = 1
                    elif knot_positions[i + 1][1] < knot_positions[i][1]:
                        U = -1

                    knot_positions[i] = (knot_positions[i][0] + R, knot_positions[i][1] + U)

                    if i == 0:
                        visited_positions_tail.append(knot_positions[i])

    visited_positions_tail = list(set(visited_positions_tail))
    return len(visited_positions_tail)

print("Part 1: ", simulate_rope(2))
print("Part 2: ", simulate_rope(10))
