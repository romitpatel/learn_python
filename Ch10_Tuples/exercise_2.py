fname = input('Please enter a valid file name: ')
try:
    fhand = open(fname)
except:
    print('Please enter an existing file name')
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From ') or len(words) < 1: continue
    for word in words:
        if word.find(':') == -1:continue
        hour, min, sec = word.split(':')
        if hour not in counts:
            counts[hour] = 1
        else:
            counts[hour] += 1

t = counts.items()
dl = list()

check = sorted(t)

# This approach uses the sorted method instead of using a list of tuples and the sort method used by list to sort the items.

for key,val in check:
    print(key,val)

