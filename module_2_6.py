def get_password(number):
    password = ""
    for i in range(1, number):
        for j in range(1, number):
            if i <= j:
                continue
            elif number % (i+j) == 0:
                password += str(j) + str(i)
    return password
new_number = int(input("Введите любое число от 3 до 20: "))
result = get_password(new_number)
print("Для вашего числа:", new_number, "Подобран пароль: ", result)
