import re

file = open("input.txt", "r")
file = file.read()
result = re.findall("do\(\)|mul\(\d{1,3},\d{1,3}\)|don't\(\)", file)
print(result)
total = 0
do = 1
dont = 0
for i in result:
    if "do()" == i:
        do = 1
        dont = 0
        continue
    elif "don't()" == i:
        do = 0
        dont = 1
        continue
    if do:
        newresult = re.findall("\d{1,3}", i)
        print(newresult)
        total += int(newresult[0]) * int(newresult[1])
print(total)
