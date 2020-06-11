fname = input('Please enter a file name: ')
fhand = open(fname)

'''
For traversing through a dictionary and finding the word count which is the most common use case for it
we need two loops, one outer loop that loops through the file and splits lines into words and then another loop
that loops through the words and calculates the count.
'''
d = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] +=1

print(d)

d2 = {'chuck':1,'hello':2,'there':3}
list1 = list(d2.keys())
list1.sort()
for keys in list1:
    print(keys, d2[keys])