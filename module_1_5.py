#Неизменяемые и изменяемые объекты. Кортежи и списки
immutable_var = (1, 2, True, "Привет", [1])
print("Кортеж разных типов данных: ", immutable_var)
#immutable_var[0] = 3
#TypeError: 'tuple' object does not support item assignment - объект 'tuple' - (Кортеж) не поддерживает назначение (изменение) элементов
mutable_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Пока', False]
print("Список: ", mutable_list)
mutable_list[0] = 3; mutable_list[2] = 5; mutable_list[6] = 9; mutable_list[-2] = 'Привет'; mutable_list[-1] = True
print("Изменённый список: ", mutable_list)
