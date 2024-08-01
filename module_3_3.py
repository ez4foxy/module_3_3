def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# print_params(1, 2, 4, 5) - Ошибка
print_params()
print_params(1, 10)
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = ["Foxy", 31, True]
values_dict = {"a": False, "b": 50, "c": "Пирог"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [18.5, "Loona"]
print_params(*values_list_2, 42)