import re
fhand = open('example-short.txt')

for line in fhand:
    line = line.rstrip()
    x = re.findall('^From.* ([0-9][0-9]):',line)
    if len(x)> 0: print(x)
