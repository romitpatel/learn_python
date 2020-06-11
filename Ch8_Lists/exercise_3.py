fname = input('please enter a file name: ')
fhand = open('romeo.txt')

new_list = list()
for line in fhand:
    word = line.split()
    for element in word:
        if element not in new_list:
            new_list.append(element)

new_list.sort()

print(new_list)




