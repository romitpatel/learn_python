import string
fname = input('Please enter a file name: ')

try:
    fhand = open(fname)
except:
    print('Please provide an existing file name.')
    exit()

counts = dict()
for line in fhand:
    line = line.strip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter.isnumeric(): continue
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1

t = counts.items()
dl = list()

for key,val in t:
    dl.append((val,key))

dl.sort(reverse=True)

for val,key in dl:
    print (key,val)


