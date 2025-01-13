def add_everything_up(a, b):
    try:
        print(a + b)

    except TypeError as exc:
        print(f'({a}{b}) - ваши данные не одного типа ошибка: {exc}')


add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)