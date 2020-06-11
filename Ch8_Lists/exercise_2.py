fhand = open('example2.txt')

for line in fhand:
    word = line.split()
    if not line.startswith('From') or len(word) < 2 : continue
    print(word[2])