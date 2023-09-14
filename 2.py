# Задание 2
# в наличии список множеств. внутри множества целые числа
# посчитать
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все множества в один кортеж

m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

total_number_count = 0
total_number_sum = 0
for numbers in m:
    total_number_count += len(numbers)
    total_number_sum += sum(numbers)

average_value = total_number_sum / total_number_count
numbers_tuple = tuple(number for numbers in m for number in numbers)

print(
    f'1. Общее количество чисел = {total_number_count}\n'
    f'2. Общая сумма чисел = {total_number_sum}\n'
    f'3. Среднее значение = {average_value}\n'
    f'4. Все множества в одином кортеже = {numbers_tuple}'
)
