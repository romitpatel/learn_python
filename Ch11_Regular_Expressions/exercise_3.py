import re

fhand = open('example-short.txt')

count = 0
tot = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('([0-9])',line)
    if len(x) > 0:
        for value in x:
            count += 1

            number = int(value)
            tot += number

print(count)
print(tot)
avg = tot/count
print(avg)
