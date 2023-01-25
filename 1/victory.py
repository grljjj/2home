d = {'pushkin \n': 1799, 'lermontov \n': 1814, 'tolstoi \n': 1828, 'chehov \n': 1860, 'gogol\n': 1809}

while True:

    counter = 0
    for i in d:
        year = input(f'Введите год рождения {i}')
        if year == str(d[i]):
            counter +=1

    print('Количество верных ответов: ', counter)
    print('Количество верных ошибок: ', 5 - counter)
    print('Процент правильных ответов: ', counter*100/5)
    print('Процент неправильных ответов: ', 100-counter*100/5)

    zanovo = input('Начать игру снова? \n')

    if zanovo == 'Да':
        continue
    elif zanovo == "Нет":
        break