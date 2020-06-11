fname = input('Please enter a file name: ')
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From ') or len(words) < 1: continue
    index = words[1].find('@')
    word_length = len(words[1])

    for word in words:
        if word.find('@') == -1:continue
        else:
            index = word.find('@')
            word_length = len(word)
            dom_addr = word[index+1:word_length]
            if dom_addr not in counts:
                counts[dom_addr] = 1
            else:
                counts[dom_addr] += 1



print(counts)

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From ') or len(words) < 1: continue
    index = words[1].find('@')
    word_length = len(words[1])

    for word in words:
        if word.find('@') == -1: continue
        else:
            dom_addr = word[index+1:word_length]
            if dom_addr not in counts:
                counts[dom_addr] = 1
            else:
                counts[dom_addr] += 1


print(counts)