# SkillFactory QAP-89 задание 13.8.19

count = 0  # Количество билетов
summ = 0  # Сумма
i = 1  # Счётчик итераций

# Запрашиваем у пользователя количество билетов
while count <= 0:
    try:  # Проверка на ввод циферок
        count = int(input('Добрый день, сколько всего билетов желаете приобрести: '))
        if count <= 0:
            print('Невозможно купить 0 или меньше билетов, давайте попробуем ещё раз.')
    except ValueError:
        print('Что-то пошло не так, пожалуйста введите натуральное число')

# Запрос возрастов и подсчёт суммы
while i <= count:
    age = None  # "Зануляем" возраст оставшийся с прошлой итерации
    # Запрос возраста
    while age is None:
        try:  # Проверка на ввод циферок
            age = int(input(f'Пожалуйста укажите возраст постителя {i}: '))
        except ValueError:
            print('Что-то пошло не так, пожалуйста введите натуральное число')
    # Определение цены билета
    if age < 0:
        print('Похоже что посетитель ещё не родился, пожалуйста повторите ввод.')
    elif age < 18:
        print('Возраст посетителя меньше 18 лет, билет бесплатный.')
        i += 1
    elif age < 25:
        print('Возраст посетителя от 18 лет до 25 лет, цена билета 990 руб.')
        summ += 990
        i += 1
    elif age < 100:
        print('Возраст посетителя 25 лет или больше, цена билета 1390 руб.')
        summ += 1390
        i += 1
    else:
        print('Вероятно Вы ошиблись во вводе или посетитель очень стар, пожалуйста повторите ввод.')

# Вывод суммы
print()
if count > 3:
    print('Спасибо что пришли с друзьями, Ваша скидка 10%')
    print(f'Сумма к оплате за {count} билета(ов) {summ * 0.9} руб.')
else:
    print(f'Сумма к оплате за {count} билет(а) {summ} руб.')
