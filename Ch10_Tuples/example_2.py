import string

fname = input('Please enter a valid file name: ')
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

decorate_list = list()
for key, val in list(counts.items()):
    decorate_list.append((val,key))

decorate_list.sort(reverse=True)

top10_elements = decorate_list[:10]

for key, val in top10_elements:
    print(key, val)
