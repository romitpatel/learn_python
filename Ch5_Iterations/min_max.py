# writing a function to find the maximum and minmimum integer in a list

numbers = []
while True:
        inp = (input('Please enter a number: '))
        if inp == 'done!':
            break
        try:
            val = int(inp)
        except:
            print('Invalid input')
            print('Please provide a number')
            continue
        numbers.append(val)

print(numbers)

# the problem with this loop is this would not work when creating a loop for smallest

"""
largest = 0
for i in numbers:
    print('Before the largest is: ', largest, i)
    if i > largest:
        largest = i
"""
largest = None
for i in numbers:
    if largest is None or i > largest:
        largest = i


"""
smallest = 0
for i in numbers:
    print('Before the smallest is: ', smallest, i)
    if i < smallest:
        smallest = i
    else:
        smallest = smallest
"""
smallest = None
for i in numbers:
    if smallest is None or i < smallest:
        smallest = i

print('After the loop, largest: ', largest)

print('After the loop, smallest: ', smallest)




