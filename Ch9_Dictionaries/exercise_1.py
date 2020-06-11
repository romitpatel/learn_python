fname = input('Please provide a file name: ')
fhand = open(fname)

word_dict = dict()
for line in fhand:
    word = line.split()
    for element in word:
        word_dict[element] = 1

print(word_dict)