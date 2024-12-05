first = []
second = []
totaldistance = 0
with open("input.txt", "r") as listfile:
    for line in listfile:
        splited = line.split()
        first.append(int(splited[0]))
        second.append(int(splited[1]))


first.sort()
second.sort()
check = {}
for i in range(0, len(first)):
    totaldistance += abs(first[i] - second[i])
for i in range(0, len(second)):
    x = check.get(second[i])
    if x is None:
        check[second[i]] = 1
    else:
        check[second[i]] += 1

# print(check)
total = 0
for i in first:
    if check.get(i) != None:
        total += i * check.get(i)
print(totaldistance)
print(total)
