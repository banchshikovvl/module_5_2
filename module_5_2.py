
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def go_to(self, new_floor):
        list_ = []
        for i in range(1, self.number_of_floors + 1):
            list_.append(i)
        if new_floor in list_:
            for j in range(1, new_floor + 1):
                if j != new_floor:
                    print(j)
                else:
                    print(f'Приехали на {new_floor} этаж {self.name}')
                    print()
        else:
            print(f'В {self.name},такого этажа не существует')


dom1 = House('ЖК Эльбрус', 30)
dom2 = House('ЖК Уют', 10)

House.go_to(dom1, 31)
House.go_to(dom2, 0)

print()
print(f'{dom1.name}, количество этажей: {dom1.number_of_floors}')
print(f'{dom2.name}, количество этажей: {dom2.number_of_floors}')
print()
print('Магический метод __str__:')
print(dom1)
print(dom2)
print()
print('Магический метод __len__:')
print(len(dom1))
print(len(dom2))
