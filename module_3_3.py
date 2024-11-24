def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(2, 'Привет', False)
print_params([12, 3, 5], 'Пока')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [False, 10, 4.5]
values_dict = {'a': True, 'b': 6.6, 'c': [7, 10, 40]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 'Никита']
print_params(*values_list_2, 42)