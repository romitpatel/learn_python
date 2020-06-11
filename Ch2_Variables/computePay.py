hours_prompt = 'Enter hours:'
hours = input(hours_prompt)
pay_prompt = 'Enter pay:'
pay = input(pay_prompt)
rate = int(hours) * int(pay)
print('Rate is ' + str(rate))
