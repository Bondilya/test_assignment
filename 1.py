# Задание 1
# имеется текстовый файл f.csv, по формату похожий на .csv с разделителем |

"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...
"""
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одиннаковым id присутствуют разные данные - найти такие записи
import csv


unique_records = dict()

with open('f.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='|')

    for row in reader:
        record_id = row['id'].strip()
        record = (
            row['lastname'].strip(),
            row['name'].strip(),
            row['patronymic'].strip(),
            row['date_of_birth'].strip(),
        )

        if record_id not in unique_records:
            unique_records.update({record_id: record})
        else:
            print(f'Duplicated record with id: {record_id} - {record}')


print(unique_records)
