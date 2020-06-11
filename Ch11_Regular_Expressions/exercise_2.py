import re

fhand = open('example-short.txt')

count =0
for line in fhand:
    line = line.rstrip()
    if re.search('New Revision: 39772', line):
        print(line)
        count +=1

print(count)