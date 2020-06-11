fname =input('Please enter a valid file name: ')
try:
    fhand = open(fname)
except:
    print('Please provide an existing file name.')
    exit()

counts = dict()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From ') or len(words) < 1 : continue
    for word in words:
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1

d_list = list()
t = counts.items()
for key,val in t:
    d_list.append((val, key))

d_list.sort(reverse=True)

for val, key in d_list[:1]:
    print(key,val)