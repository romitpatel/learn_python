fname = input('Please enter a file name: ')
fhand = open(fname)

count = 0
for line in fhand:
    word = line.split()
    if not line.startswith('From ') or len(word) == 0:continue
    print(word[1])
    count +=1

print('There were', count,'lines with From as the first word')
