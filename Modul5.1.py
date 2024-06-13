class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.numbers_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
            else:
                print('Такого этажа не сущетвует')

h1 = House("Солнеынй", 9)
h2 = House("Стрелка", 24)
h1.go_to(6)
h2.go_to(27)




