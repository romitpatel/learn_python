"""
reading through a file can be done through either using
a loop like for or by using the read function.
"""

fhand = open('example-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    print(line)

"""
searching through a file is another type of commonly
used feature in python and that can be done by using the for loop
along with find
"""

fhand = open('example-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:continue
    print(line)

fname = input('Please enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Given file name does not exist. please enter a valid file name.')
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
