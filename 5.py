"""
# Задание 5*
Имеется текстовый файл с набором русских слов(имена существительные, им.падеж)
Одна строка файла содержит одно слово.
Написать программу которая выводит список слов, каждый элемент списка которого - это новое слово,
которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
Порядок вывода слов НЕ имеет значения

Например, текстовый файл содержит слова: ласты, стык, стыковка, баласт, кабала, карась

Пользователь вводмт первое слово: ласты
Программа выводит:
ластык
ластыковка

Пользователь вводмт первое слово: кабала
Программа выводит:
кабаласты
кабаласт

Пользователь вводмт первое слово: стыковка
Программа выводит:
стыковкабала
стыковкарась
"""
from typing import Optional, Union, Tuple


def get_words_collision(word_1: str, word_2: str) -> Optional[Union[str, Tuple[str, str]]]
    word_1_last_two_chars = word_1[-2:]
    if word_1_last_two_chars in word_2 and word_1 != word_2:
        word2_chars_collision_position = word_2.find(word_1_last_two_chars) + 2
        chars_collision = word_2[:word2_chars_collision_position]

        if word_1.endswith(chars_collision):
            word_2_without_collision_chars = word_2[word2_chars_collision_position:]
            # recursive for similar cases: "запара" - "параллель"
            new_collision = get_words_collision(word_1, word_2_without_collision_chars)

            if new_collision:
                return new_collision
            else:
                return word_1 + word_2_without_collision_chars


words = []
with open('words.txt', 'r', encoding='utf-8') as file:
    for line in file:
        words.append(line.strip())

entered_word = str(input('Enter a word->'))

for word in words:
    collision_word = get_words_collision(entered_word, word)
    if collision_word:
        print(collision_word)
