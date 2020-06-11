import re
str = input('Please enter a regular expression: ')
count = 0
fhand = open('example-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search(str,line):
        count +=1

print('example-short.txt has',count,'lines that matched',str)
