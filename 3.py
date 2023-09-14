# Задание 3
# имеется список списков
# a = [[1,2,3], [4,5,6]]
# сделать список словарей
# b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]

a = [[1, 2, 3], [4, 5, 6]]

number_dicts = []
for numbers in a:
    dict_numbers = {}
    for i, number in enumerate(numbers):
        dict_numbers.update({f'k{i + 1}': number})
    number_dicts.append(dict_numbers)
