new_list = list()

while True:
    try:
        number = input('Please enter a number: ')
    except:
        print('Invalid input. Please provide a number.')
        continue

    if number == 'done':break
    val = int(number)
    new_list.append(number)


print(new_list)
print('Maximum: ', max(new_list))
print('Minimum: ', min(new_list))



