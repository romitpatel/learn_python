class state:
    def __init__(self, name, population, area, capital):
        self.name = name
        self.population = population
        self.area = area
        self.capital = capital

    def calc_density(self):
        return self.area/self.population

state_1 = state('guj', 50000000, 40000000, 'gandhinagar')
state_2 = state('maharashtra', 80000000, 100000000, 'mumbai')

print(state_1.name)
print(state_2.calc_density())

