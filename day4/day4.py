def checkerpt2(inputlist, i, j, pos):
    # print(pos)
    if (
        (i + (pos[0][1])) >= 0
        and (i + (pos[0][1])) < len(inputlist)
        and (j + (pos[0][0])) >= 0
        and (j + (pos[0][0])) < len(inputlist[0])
    ):
        if (
            (i + (pos[1][1])) >= 0
            and (i + (pos[1][1])) < len(inputlist)
            and (j + (pos[1][0])) >= 0
            and (j + (pos[1][0])) < len(inputlist[0])
        ):
            if inputlist[i + pos[0][1]][j + pos[0][0]] == "M":
                if inputlist[i + pos[1][1]][j + pos[1][0]] == "S":
                    return 1
            elif inputlist[i + pos[0][1]][j + pos[0][0]] == "S":
                if inputlist[i + pos[1][1]][j + pos[1][0]] == "M":
                    return 1

    return 0


def checker(inputlist, i, j, pos):
    # print(pos)
    if (
        (i + (pos[1] * 3)) >= 0
        and (i + (pos[1] * 3)) < len(inputlist)
        and (j + (pos[0] * 3)) >= 0
        and (j + (pos[0] * 3)) < len(inputlist[0])
    ):
        if inputlist[i + pos[1]][j + pos[0]] == "M":
            if inputlist[i + 2 * pos[1]][j + 2 * pos[0]] == "A":
                if inputlist[i + 3 * pos[1]][j + 3 * pos[0]] == "S":
                    return 1

    return 0


def part1(inputlist):
    checks = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    counter = 0
    for i in range(0, len(inputlist)):
        for j in range(0, len(inputlist[i])):
            # print(j)
            if inputlist[i][j] == "X":

                for k in checks:
                    # print(checker(inputlist, i, j, k))
                    if checker(inputlist, i, j, k):
                        counter += 1

    print(counter)


def part2(inputlist):
    check1 = [[-1, 1], [1, -1]]
    check2 = [[1, 1], [-1, -1]]
    counter = 0
    for i in range(0, len(inputlist)):
        for j in range(0, len(inputlist[i])):
            # print(j)
            if inputlist[i][j] == "A":

                first = checkerpt2(inputlist, i, j, check1)
                second = checkerpt2(inputlist, i, j, check2)
                # print(checker(inputlist, i, j, k))
                if first == second and first == 1:
                    counter += 1
    print(counter)


inputlist = [line.strip() for line in open("input.txt", "r")]

xcount = 0

part1(inputlist)
part2(inputlist)
