# SkillFactory QAP-89 задание 17.9.1
#
# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
# 1. Преобразование введённой последовательности в список
# 2. Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# 3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.
#
# Подсказка
# Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае необходимо вывести соответствующее сообщение
#

def bubble_sort(array):  # Сортировка пузырьком
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right):  # Поиск числа в массиве двоичным алгоритмом (только в отсортированном)
    middle = (right + left) // 2  # находим середину
    if array[middle] < element <= array[middle + 1]:  # если элемент удовлетворяет условиям - возвращаем этот индекс
        return middle
    elif element <= array[middle]:  # если элемент меньше элемента в середине, рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


usernumber = None  # Инициализируем переменные для ввода
array = []  # Инициализируем переменные для ввода

while not array:
    try:  # Проверка на ввод циферок
        array = list(map(int, input('Введите последовательность натуральных чисел через пробел: ').split()))
    except ValueError:
        print('Что-то пошло не так, пожалуйста введите последовательность натуральных чисел через пробел: ')

while not usernumber:
    try:  # Проверка на ввод циферок
        usernumber = int(input('Введите любое натуральное число: '))
    except ValueError:
        print('Что-то пошло не так, пожалуйста введите натуральное число: ')

array = bubble_sort(array)  # Сортируем массив по возрастанию

if usernumber <= array[0]:  # Проверяем не выходит ли пользовательское число за рамки последовательности
    print(f"Заданное число {usernumber} <= минимального элемента последовательности {array[0]}")
elif usernumber > array[-1]:
    print(f"Заданное число {usernumber} > максимального элемента последовательности {array[-1]}")
else:
    print(f"Позиция максимального элемента последовательности меньше заданного числа: {binary_search(array, usernumber, 0, len(array)-1)} (нумерация элементов с нуля).")