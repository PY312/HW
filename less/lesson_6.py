ru_en = {'монета': 'money',
         'красный': 'red',
         'кружка':"cup"}
ru_kg = {'монета': "тыйын",
         'красный' :'кызыл',
         'нож':'бычак'}
kg_ru = {'акча':'деньги',
         'тамак': 'еда',
         'бала':'мальчик'}
kg_en = {'акча': 'money',
         'тамак': 'food',
         'эркек':'man'}
en_ru = {'money':'деньги',
         'red':'красный',
         'key':'ключ'}
en_kg = {'money': 'акча',
         'red': 'кызыл',
         'girl':'кыз'}
while True:
    lang = input('Выберите язык  : ')
    if lang == 'en':
        word_en = input('Введите слово для перевода :')
        try:
            print ('На русском языке это -   ' + en_ru[word_en])
        except KeyError:
            print('Нет такого слова в в английском словаре.')
            action = input('Хотите ввести новое слово на английском языке языке? Y/N ')
            if action == 'Y':
                en_ru[word_en] = input(f'Введите первод к слову {word_en} ')
        try:
            print ('на кыргызском языке это -' + en_kg[word_en])
        except KeyError:
            print('Нет такого слова в кыргызском словаре.')
            action = input('Хотите ввести новое слово на кыргызском языке? Y/N ')
            if action == 'Y':
                en_kg[word_en] = input(f'Введите первод к слову {word_en} ')
    elif lang == 'kg':
        word_kg = input('Введите слово для перевода :')
        try:
            print('На английском это -   ' + kg_en[word_kg])
        except KeyError:
            print('Нет такого слова в в англиском словаре.')
            action = input('Хотите ввести новое слово на англиском языке языке? Y/N ')
            if action == 'Y':
                kg_en[word_kg] = input(f'Введите первод к слову {word_kg} ')
        try:
            print('на русском языке это -' + kg_ru[word_kg])
        except KeyError:
            print('Нет такого слова в русском словаре.')
            action = input('Хотите ввести новое слово на русском языке языке? Y/N ')
            if action == 'Y':
                kg_ru[word_kg] = input(f'Введите перевод к слову {word_kg} ')
    elif lang == 'ru':
        word_ru = input('Введите слово :')
        try:
            print('на английском языке это -' + ru_en[word_ru])
        except KeyError:
            print('Нет такого слова в в английском словаре.')
            action = input('Хотите ввести новое слово на английском языке языке? Y/N ')
            if action == 'Y':
                ru_en[word_ru] = input(f'Введите перевод к слову {word_ru} ')
        try:
            print ('на кыргызском языке это -' + ru_kg[word_ru])
        except KeyError:
            print('Нет такого слова в кыргызском языке.')
            action = input('Хотите ввести новое слово на кыргызском языке? Y/N ')
            if action == 'Y':
                ru_kg[word_ru] = input(f'Введите перевод к слову {word_ru} ')
    else:
        print('Не верно выбран язык :-( ')