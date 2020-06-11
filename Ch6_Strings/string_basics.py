# traversing through a string
# traverse through a string and print the last character first to the first character

name = 'banana'
i = len(name)-1
while i > -1:
    print(name[i])
    i-=1

i = 0
while len(name) > i:
    print(name[i])
    i+=1

i = -1
while i >= -(len(name)):
    print(name[i])
    i-=1

for i in name:
    print(i)
