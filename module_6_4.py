class House:
    houses_history = []


    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)


    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors


    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)


    def __radd__(self, value):
        return House(self.name, self.number_of_floors + value)


    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __del__(self):
        House.houses_history.remove(self.name)
        print(f"{self.name} снесён, но он останется в истории")



h1 = House('ЖК Горский', 10)
print(House.houses_history)
h2 = House("Домик  в деревне", 20)
print(House.houses_history)
h3 = House("ЖК Акация", 11)
print(House.houses_history)
h4 = House("ЖК Матрёшки", 27)
print(House.houses_history)
h5 = House("ЖК Кристал", 24)
print(House.houses_history)
h6 = House("ЖК Дербенёв", 64)
print(House.houses_history)


del h3
del h4
del h5




print(House.houses_history)
