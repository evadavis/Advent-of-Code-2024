import re


def part1(inputfile):

    inputfileread = open(inputfile, "r").read()
    rules = {}
    ruleslist = re.findall("\d{1,2}\|\d{1,2}", inputfileread)
    # print(ruleslist)
    for i in ruleslist:
        i = i.split("|")
        if rules.get(i[0]) == None:
            rules[i[0]] = [i[1]]
        else:
            rules.get(i[0]).append(i[1])
    # print(inputfile)
    # print(rules)
    saferules = []
    unsaferules = []
    with open(inputfile, "r") as inp:
        for line in inp:
            incorrect = 0
            if "|" in line or len(line) <= 1:
                continue
            # print(line)
            line = line.strip()
            line = line.split(",")
            # print(line)
            for i in range(len(line) - 1, 0, -1):
                for j in range(0, i):
                    # print(line[j], line[i])
                    if rules.get(line[i]) != None:
                        if line[j] in rules.get(line[i]):
                            incorrect = 1
            if incorrect == 0:
                saferules.append(line)
            else:
                unsaferules.append(line)
    total = 0

    for i in range(0, len(saferules)):
        total += int(saferules[i][len(saferules[i]) // 2])

    print(total)

    return unsaferules, rules


def part2(unsafelist, rules):
    for line in unsafelist:
        for i in range(len(line) - 1, 0, -1):
            for j in range(0, i):
                if rules.get(line[i]) != None:
                    if line[j] in rules.get(line[i]):
                        # print("incorrect")
                        temp = line[j]
                        line[j] = line[i]
                        line[i] = temp
    # print(unsafelist)
    total = 0
    for i in range(0, len(unsafelist)):
        total += int(unsafelist[i][len(unsafelist[i]) // 2])
    print(total)


if __name__ == "__main__":
    import timeit

    unsafe, rulesdict = part1("input.txt")

    part2(unsafe, rulesdict)
    t = timeit.timeit(lambda: part1("input.txt"), number=1)

    s = timeit.timeit(lambda: part2(unsafe, rulesdict), number=1)
    print(s + t)
