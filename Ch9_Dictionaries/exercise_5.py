fname = input('Please enter an existing file: ')
try:
    fhand = open(fname)
except:
    print('Provided file name does not exist.')
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From ') or len(words) < 1: continue
    for word in words:
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] +=1

'''
def maximum(d):
    largest = None
    for keys in d:
        if largest is None or d[keys] > largest:
            largest = d[keys]

    return largest
'''
maximum = None
minimum = None

for keys in counts:
    if maximum is None or counts[keys] > maximum:
        maximum = counts[keys]
    if minimum is None or counts[keys]<minimum:
        minimum = counts[keys]


for keys in counts:
    if counts[keys] == maximum:
        print(keys,counts[keys])
    if counts[keys] == minimum:
        print(keys, counts[keys])

print(counts)

