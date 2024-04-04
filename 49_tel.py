# Задача №49. Создать телефонный справочник с возможностью импорта
# и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска
# определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """"
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''

    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """"
    Поиск записи по критериям data.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    # for i in list_1:
    #    if data in i:
    #        result.append(i)
    if not result:
        return "Совпадений не найдено"
    return "\n".join(result)


def transfer_data(source: str, dest: str, num_row: int):
    """
    Функция для переноса указанной строки из одного файла
    в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """
    with open(source, 'r', encoding="utf-8") as file:
        with open(dest, 'w', encoding="utf-8") as file_1:
            for i, line in enumerate(file, 1):
                if i == num_row:
                    file_1.write(line)


INFO_STRING = """
Выберите режим работы:
1 - вывести данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
"""

file = "49_tel.txt"

if file not in os.listdir():
    print("Указанное имя файла отсутствует")
    sys.exit()


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("Введите имя: ")
        phone = input("Введите номер телефонв: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите искомое значение: ")
        print(search_user(file, data))
    elif mode == 4:
        # Тут нужно вызвать функцию с аргументами
        num_row = int(input("Введите номер строки для копирования: "))
        dest = str(input("Введите полностью название файла: "))
        if dest not in os.listdir():
            print("Указанное имя файла отсутствует")
            sys.exit()
        transfer_data(file, dest, num_row)
