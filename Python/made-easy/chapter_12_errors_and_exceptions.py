# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---
"""Глава 12."""


# # Ошибки и исключения

# Программа на Python останавливается сразу, как только обнаруживает ошибку. Существуют два различных типа ошибок: синтаксические ошибки и исключения
#
# # Синтаксические ошибки

# ![image.png](attachment:image.png)

# # Исключения

# ![image.png](attachment:image.png)

# # Вызов исключений
#
# **Оператор raise**
#
# Оператор raise позволяет программисту вызвать встроенное исключение или собственное

# # Исключение AssertionError

# Вместо того, чтобы ждать, пока программа сломается при выполнении, мы можем заранее использовать утверждения. Мы словно 'утверждаем' с помощью оператора assert, что здесь должно выполняться определенное условие. Если условие, которое мы указали, оказывается истинным, программа продолжает выполнение. Если условие окажется ложным, программ сгенерирует исключение AssertionError.
#
# # Обработка исключений
#
# **Операторы try и except**
#
#
# Конструкция try-except в Python используется для перехвата и обработки исключе­ний. Python выполняет блок try как обычную часть программы. Код, следующий за оператором except, является ответом программы на любое исключе­ние, которое могло возникуть в блоке try.

# Конструкция try-except работает следующим образом:
#
# 1. Сначала выполняется блок try (инструкции между ключевыми словами try И except).
#
# 2. Если не возникает исключения, блок except пропускается и выполнение завершается.
#
# 3. Если во время выполнения блока try возникает исключение, остальная часть блока пропускается. Затем, если тип возникшего исключения соответствует ука­занному после ключевого слова except, выполняется блок except, а затем про­должает выполняться следующий код за пределами блока.
#
# 4. Если возникает исключение, отличное от указанного в блоке except, оно передается во внешние операторы try. Если исключение так и не будет перехвачено, это означает, что программа встретила необработанное исключение и ее выпол­нение останавливается с сообщением об ошибке.
#
# После оператора try может быть более одного блока except, в которых можно обра­ботать разные исключения. В любом случае будет выполнено не более одного бло­ ка except. При этом обрабатывают только те исключения, которые возникли в соот­ветствующем блоке try, но не в других блоках except того же оператора try.
#
# **Блок else**
#
# У конструкции try-except есть необязательный блок else, который может следовать после всех блоков except. В нем указывается код, который должен выполниться, если блок try не вызвал исключения
#
# **Финальный блок**
#
# У оператора try есть еще один необязательный блок finally, предназначенный для выполнения какой-либо очистки, которую требуется выполнить в любом случае.
#
# Приведем несколько более сложных случаев.
#
# ♦ Если во время выполнения блока try возникает исключение, оно может быть обработано с помощью блока except. Если исключение не обрабатывается бло­ком except, исключение повторно вызывается после выполнения блока finally.
#
# ♦ Исключение могло произойти во время выполнения блока except или else. В этом случае, опять же, исключение повторно возникает после выполнения блока finally.
#
# ♦ Если в блоке try встретился оператора break, continue или return, блок finally будет выполнен непосредственно перед выполнением оператора break, continue return.
#
# ♦ Если блок finally содержит оператор return, то вернется значение из оператора
#
# # Практическая часть

# 1 . Напишите функцию с именем oops(), которая явно вызывает исключение IndexError при вызове. Затем напишите другую функцию, которая вызывает oops() внутри конструкции try-except и перехватывает ошибку. Что произойдет, если в функции oops() вместо
# IndexError будет вызываться KeyError?


def oops() -> None:
    """_summary_.

    Raises:
        IndexError: _description_
    """
    raise IndexError("non-existent index")


def get_item(your_list: list[int], index: int) -> int:
    """.

    Args:
        your_list (list[int]): _description_
        index (int): _description_
    Returns:
        int: _description_
    """
    try:
        return your_list[index]
    except IndexError:
        oops()
        return -1


# (рекомендуется открывать в заданном порядке - сверху вниз)
#
# https://drive.google.com/file/d/1XSFMBGTeHQTvONQT5qAArlxgUN3EN8rZ/view?usp=share_link
#
# https://drive.google.com/file/d/1sBsq-ZjpWOaGPTQIYgj_As3NeWfZmC1f/view?usp=sharing
#
# https://drive.google.com/file/d/1tugakWTFS31QH9cd9oj-bVnvj-o2EWOo/view?usp=sharing
#
# https://drive.google.com/file/d/1W9OUvn87MnlCBjuE5j8K7v85OBM0ukiS/view?usp=sharing

# +
# get_item([1, 2, 3, 4, 5], 7)
# -

# Вывод - если вместо IndexError мы ставим KeyError - блок except не выполняется, и при нахождении исключения в блоке try вызывается встроенное исключение

# 2. Напишите функцию нахождения среднего значения списка чисел. Ваша функция должна иметь возможность обрабатывать пустой список, а также список, содер­жащий строку.


def med(your_list: list[int]) -> str:
    """_summary_.

    Args:
        your_list (list[int]): _description_
    Returns:
        float: _description_
    """
    try:
        # чтобы не было проблем с линтером, так как функция
        # может вернуть несколько типов данных
        # перевожу вывод в str
        return str(sum(your_list) / len(your_list))

    except ZeroDivisionError:
        return "your list is empty"
    except TypeError:
        return "use int type instead"


med([1, 2, 3, 4, 5])


# 3 . Напишите программу, принимающую дату от пользователя в виде дня, месяца и года и вызывающую соответствующие ошибки, если передано недопустимое значение. Выводите сообщения об ошибке, пока пользователь не введет пра­вильные значения.


def is_leap(num_year: int) -> bool:
    """_summary_.

    Args:
        num_year (int): _description_
    """
    if num_year in list(range(4, 3001, 4)):
        return True
    return False


# +
# Версия, которая мне нравится больше, но она не проходит
# по линтерам из-за постоянного переназначения переменной

try:
    months31: list[int] = [1, 3, 5, 7, 8, 10, 12]
    day: int = int(input("Введите день: "))
    month: int = int(input("Введите номер месяца: "))
    year: int = int(input("Введите год: "))
    while day > 31 or day < 1:
        print("в месяцах нет столько дней")
        months31 = [1, 3, 5, 7, 8, 10, 12]
        day = int(input("Введите день: "))
        month = int(input("Введите номер месяца: "))
        year = int(input("Введите год: "))
    while month > 12 or month < 1:
        print("в году  всего 12 месяцев")
        months31 = [1, 3, 5, 7, 8, 10, 12]
        day = int(input("Введите день: "))
        month = int(input("Введите номер месяца: "))
        year = int(input("Введите год: "))
    while day == 31 and month not in months31:
        print("в этом месяце нет 31 дня")
        months31 = [1, 3, 5, 7, 8, 10, 12]
        day = int(input("Введите день: "))
        month = int(input("Введите номер месяца: "))
        year = int(input("Введите год: "))
    while month == 2 and day > 29:
        print("в феврале нет столько дней")
        months31 = [1, 3, 5, 7, 8, 10, 12]
        day = int(input("Введите день: "))
        month = int(input("Введите номер месяца: "))
        year = int(input("Введите год: "))
    while month == 2 and day == 29:
        if not is_leap(year):
            print("этот код не является високосным")
            months31 = [1, 3, 5, 7, 8, 10, 12]
            day = int(input("Введите день: "))
            month = int(input("Введите номер месяца: "))
            year = int(input("Введите год: "))
    print(str(day) + "/" + str(month) + "/" + str(year))
except TypeError:
    print("тип введенных вами данных не поддерживается, используйте int")


# -

# 4. Создайте класс Person для хранения личной информации (по вашему выбору) о человеке. Убедитесь, что ввод некорректных данных обрабатывается должным образом.


class Person:
    """_summary_."""

    def __init__(self, name: str, age: int, sex: str) -> None:
        """_summary_.

        Args:
            name (str): _description_
            age (int): _description_
            sex (str): _description_
        """
        if not isinstance(name, str):
            raise TypeError("use str type for name")
        if not isinstance(age, int):
            raise TypeError("use int type for age")
        if not isinstance(sex, str):
            raise TypeError("use str type for sex")

        self.name = name
        self.age = age
        self.sex = sex