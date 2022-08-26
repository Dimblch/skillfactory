# SkillFactory QAP-89 задание 15.4.1
#
# Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге, читает его
# и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов, и наиболее длинное
# слово на английском языке.

# Подключаем модуль работы с путями, для проверки наличия файла.
import os.path

CHARS_RUS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя-"
CHARS_EN = "abcdefghijklmnopqrstuvwxyz-'"


# Функция: заменяет в строке все символы кроме заданных на пробелы
def remove_non_letter(in_str, char_to_keep):
    out_str = ''
    for l in in_str:
        if l in char_to_keep:
            out_str = out_str + l
        else:
            out_str = out_str + ' '
    return out_str


# Функция: возвращает ключ с наибольшим значением и его значение, при условии длинны ключа более key_length
def find_most_frequent(dic, key_length):
    max_value = 0
    max_value_key = ''
    for k, v in dic.items():
        if len(k) > key_length and v > max_value:
            max_value = v
            max_value_key = k
    return max_value_key, max_value


# Запрашиваем у пользователя имя файла, проверяем его наличие, повторяем до полного удовлетворения.
input_file = input('Введите имя файла с текстом или просто нажмите ввод для значения по умолчанию: ')
while not os.path.exists(input_file) and not input_file == '':
    input_file = input(f'Файл {input_file} не найдем в текущем каталоге, пожалуйста введите имя существующего файла: ')

# Подставляем тестовый файл, если пользователь ничего не ввёл
if not input_file:
    input_file = 'test.txt'
    print(f'Файл не задан, использую значение по умолчанию "{input_file}"')

# Читаем файл в переменную
with open(input_file, 'rt', encoding='utf8') as file:
    text = file.read()

# Приводим все символы к нижнему регистру
text=text.lower()

# Вырезаем из строки "text" всё лишнее и разделяем её на списки
text_all = remove_non_letter(text, CHARS_RUS + CHARS_EN).split()
text_en = remove_non_letter(text, CHARS_EN).split()

# Генерируем из списка словарь и прописываем в значения количество повторов каждого слова
text_all_dic = {word: text_all.count(word) for word in text_all}

# Ищем наиболее часто встречающееся слово из тех, что имеют размер более трех символов
most_frequent, most_frequent_value = find_most_frequent(text_all_dic, 3)

# Ищем наиболее длинное слово на английском языке
word = ''
for w in text_en:
    if len(w) > len(word):
        word = w

# Выводим найденные слова
print(f'Наиболее часто встречающееся слово длиннее трёх символов "{most_frequent}" повторяется в файле {most_frequent_value} раз(а).')
print(f'Наиболее длинное слово на английском языке "{word}"')
