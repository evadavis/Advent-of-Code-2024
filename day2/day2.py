def part1():
    safe = 0
    with open(
        r"C:\Users\evad2\OneDrive\Documents\AOC\day2\input.txt", "r"
    ) as puzzleinput:
        for line in puzzleinput:
            unsafe = 0
            decreasing = 0
            increasing = 0
            split = line.split()
            for i in range(0, len(split) - 1):
                diff = int(split[i]) - int(split[i + 1])
                if diff == 0:
                    unsafe = 1
                    break
                if diff > 3 or diff < -3:
                    unsafe = 1
                    break
                if decreasing == 0 and increasing == 0:
                    if diff < 0:
                        decreasing = 1
                    elif diff > 0:
                        increasing = 1
                elif decreasing == 1 and diff > 0:
                    unsafe = 1
                    break
                elif increasing == 1 and diff < 0:
                    unsafe = 1
                    break
            if unsafe == 1:
                continue
            else:
                safe += 1
    print(safe)


def part2():
    safe = 0
    unsafecount = 0
    with open(
        r"C:\Users\evad2\OneDrive\Documents\AOC\day2\input.txt", "r"
    ) as puzzleinput:
        for line in puzzleinput:
            unsafe = 0
            split = line.split()

            unsafe, a, b, i = checker(split)
            if unsafe == 0:
                print("safe1")
                print(split, "!")
                safe += 1
                continue

            else:
                newlist = split.copy()
                newlist.pop(i)
                unsafe, c, d, j = checker(newlist)
                if unsafe == 0:
                    safe += 1
                    print("safee")
                    print(unsafe, a, b)
                    print(newlist)
                    print(split)
                    continue

                else:
                    newlist = split.copy()

                    newlist.pop(i + 1)

                    unsafe, e, d, k = checker(newlist)
                    if unsafe == 0:
                        print("safe2")
                        print(newlist)
                        print(split)
                        safe += 1
                    else:
                        newlist = split.copy()
                        newlist.pop(0)
                        unsafe, f, g, l = checker(newlist)
                        print(unsafe)
                        if unsafe == 1:

                            unsafecount += 1
                        else:
                            print("unsafe")
                            print(split)
                            print(newlist)
                            safe += 1
            # print(safe)

    print(safe)
    print(unsafecount)


def checker(alist):
    unsafe = 0
    decreasing = 0
    increasing = 0
    for i in range(0, len(alist) - 1):
        diff = int(alist[i]) - int(alist[i + 1])
        if diff == 0:
            unsafe = 1
            return unsafe, alist[i], alist[i + 1], i
        if diff > 3 or diff < -3:
            unsafe = 1
            # print(alist[i], alist[i + 1])
            return unsafe, alist[i], alist[i + 1], i
        if decreasing == 0 and increasing == 0:
            if diff < 0:
                decreasing = 1
                print("de")
            elif diff > 0:
                increasing = 1
                print("in")
        elif decreasing == 1 and diff > 0:
            unsafe = 1
            return unsafe, alist[i], alist[i + 1], i
        elif increasing == 1 and diff < 0:
            unsafe = 1
            return unsafe, alist[i], alist[i + 1], i
    # print(unsafe, alist[i], alist[i + 1])
    # print("UNSAFE:", unsafe)
    return unsafe, None, None, 0


part1()
part2()
