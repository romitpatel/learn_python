import string

fname = input('Please enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Please provide a valid file name.')
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1               # alternatively we can use this: counts[word] = counts[word].get(word,0) + 1
        else:
            counts[word] += 1

print(counts)