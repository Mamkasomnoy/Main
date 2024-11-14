first = int(input("Введите любое число: "))
second = int(input("Введите любое второе число: "))
third = int(input("Введите любое третье число: "))
if first == second == third:
    print("У Вас 3 одинаковых числа")
elif first == second or first == third or third == second:
    print("У Вас 2 одинаковых числа")
else:
    print("У Вас все числа разные")
