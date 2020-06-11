
#Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
import re

fhand = open('example-short.txt')

for line in fhand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)',line)
    if len(x):
        print(x)