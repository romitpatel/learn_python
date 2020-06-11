def computePay(hours, rate):
    hours_inp = input('Enter hours:')
    rate_inp = input('Enter rate:')
    hours = int(hours_inp)
    rate = int(rate_inp)
    if hours < 41:
        pay = hours*rate
        print(pay)
    else:
        overtime = hours - 40
        pay = (40*rate) + (1.5*overtime*rate)
        print(pay)

computePay(45, 50)



