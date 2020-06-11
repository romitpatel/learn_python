fname = input('Please enter a file name: ')
fhand = open(fname)

#fhand = open('example-short.txt')

sum_of_spams = 0
count = 0
avg = 0
for line in fhand:
    line = line.rstrip()

    if line.startswith('X-DSPAM-Confidence: '):
        space = line.find(' ')
        val = line[space+1:]
        sum_of_spams += float(val)
        count +=1
        avg = sum_of_spams/float(count)

print('Average spam confidence: ',avg)



