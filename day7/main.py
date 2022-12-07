commands = open("input.txt").readlines()[2:]
commands = [c.strip() for c in commands]

filesystem = {"name": "/", "fileSizes": 0, "subDirectories": []}
flattenedDirectories = []

totalOfDirsWithLess100k = 0

def parse_directory(pointer):
    global totalOfDirsWithLess100k

    while len(commands) > 0:
        command = commands.pop(0)

        if command.startswith("$ cd"):
            name = command.split(" ")[-1]

            if name == "..":
                if pointer["fileSizes"] <= 100000:
                    totalOfDirsWithLess100k += pointer["fileSizes"]

                flattenedDirectories.append(pointer["fileSizes"])
                return pointer["fileSizes"]

            pointer["subDirectories"].append({"name": name, "fileSizes": 0, "subDirectories": []})

            pointer["fileSizes"] += parse_directory(pointer["subDirectories"][-1])
        elif command.split(" ")[0].isdigit():
            pointer["fileSizes"] += int(command.split(" ")[0])

    if pointer["fileSizes"] <= 100000:
        totalOfDirsWithLess100k += pointer["fileSizes"]

    flattenedDirectories.append(pointer["fileSizes"])
    return pointer["fileSizes"]

parse_directory(filesystem)

print("Part 1: ", totalOfDirsWithLess100k)

spaceNeededToFree = filesystem["fileSizes"] - (70000000 - 30000000)

print("Part 2: ", min([x for x in flattenedDirectories if x > spaceNeededToFree]))
