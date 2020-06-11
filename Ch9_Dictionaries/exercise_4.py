fname = input('Please enter a file name: ')
fhand = open(fname)

# fhand = open('example-short.txt')

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From ') or len(words) < 3 :continue

    for word in words:

        if words[2] not in counts:
            counts[words[2]] = 1
        else:
            counts[words[2]] += 1

print(counts)


