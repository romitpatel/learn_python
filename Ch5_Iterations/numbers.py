count = 0
total = 0.0
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        val = float(number)
    except:
        print('Invalid input')
        continue
    count = val + 1
    total = total + val


print(count,total,total/count)

