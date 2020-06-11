class citizen:

#example of a class variable
    benefit_percent = 0.01
    num_of_citizens = 0

    def __init__(self, name, aadhar_num, dob, income):
        self.name = name
        self.aadhar_num = aadhar_num
        self.dob = dob
        self.income = income
        citizen.num_of_citizens += 1

    def get_bracket(self):
        if int(self.income) >= 20000:
            return 'A'
        elif int(self.income) >= 10000:
            return 'B'
        elif int(self.income) >= 5000:
            return 'C'
        else:
            return 'D'

    def get_benefit(self):  #when a class variable is accessed inside a method it has to be accessed through the class itself or the instance
        self.benefit = float(self.income) * self.benefit_percent  #or citizen.benefit_percent
        return self.benefit

print(citizen.num_of_citizens)
citizen_1 = citizen('Romit', '123456', '12/04/1991', '15000')
citizen_2 = citizen('Sush', '1234561', '07/21/1991', '6000')
citizen_2.benefit_percent = 3

print('Citizen 1 has an income of $', citizen_1.income)
print(citizen_1.get_bracket())
print(citizen_2.get_bracket())
print(citizen_1.get_benefit())
print(citizen.num_of_citizens)
print(citizen_2.get_benefit())
