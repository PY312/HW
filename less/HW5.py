ru_en = {'монета': 'money',
         'красный': 'red',
         'кружка': "cup"}
ru_kg = {'монета': "тыйын",
         'красный':'кызыл',
         'нож':'бычак'}
kg_ru = {'акча':'деньги',
         'тамак': 'еда',
         'бала':'мальчик'}
kg_en = {'акча': 'money',
         'тамак': 'food',
         'эркек':'man',
         'money':'btcnjdsq'}
en_ru = {'money':'деньги',
         'red':'красный',
         'key':'ключ'}
en_kg = {'money': 'акча',
         'red': 'кызыл',
         'girl':'кыз'}
en = list(en_ru.keys())+list(en_kg.keys())
ru = list(ru_kg.keys())+list(ru_en.keys())
kg = list(kg_en.keys())+list(kg_ru.keys())
dictionary = en+ru+kg
while True:
    word = input('Введите слово для перевода :')
    if word in en:
        print ('Язык оригинала английский!')
        try:
              print (en_kg[word])
        except KeyError:
            print ('Нет перевода данного слова на кыргызский язык')
            action = input('Хотите ввести перевод на кыргызском языке? Y/N ')
            if action == 'Y':
                en_kg[word] = input(f'Введите перевод к слову {word} ')
        try:
            print(en_ru[word])
        except KeyError:
               print('Нет перевода данного слова на русский язык')
               action = input('Хотите ввести перевод на русском языке? Y/N ')
               if action == 'Y':
                    en_ru[word] = input(f'Введите перевод к слову {word} ')
    elif word in ru:
        print('Язык оригинала русский!')
        try:
            print(ru_kg[word])
        except KeyError:
            print('Нет перевода данного слова на кыргызский язык')
            action = input('Хотите ввести перевод на кыргызском языке? Y/N ')
            if action == 'Y':
                ru_kg[word] = input(f'Введите перевод к слову {word} ')
        try:
            print(ru_en[word])
        except KeyError:
            print('Нет перевода данного слова на английский язык')
            action = input('Хотите ввести перевод на англиском языке? Y/N ')
            if action == 'Y':
                ru_en[word] = input(f'Введите перевод к слову {word} ')
    elif word in kg:
        print('Язык оригинала кыргызский')
        try:
            print(kg_en[word])
        except KeyError:
            print('Нет перевода данного слова на английский язык')
            action = input('Хотите ввести перевод на английском языке? Y/N ')
            if action == 'Y':
                kg_en[word] = input(f'Введите перевод к слову {word} ')
        try:
            print(kg_ru[word])
        except KeyError:
            print('Нет перевода слова на русский язык')
            action = input('Хотите ввести перевод на русском языке? Y/N ')
            if action == 'Y':
                kg_ru[word] = input(f'Введите перевод к слову {word} ')
    else:
        print('Такого слова нет в словаре')
        action = input('Хотите ввести новое слово словарь? Y/N ')
        if action == 'Y':
            lang = (input('Выберите язык оригинала en, ru, kg    '))
            if lang == 'en':
                en_ru[word] = input(f'Введите перевод к слову {word} на русском языке ')
                en_kg[word] = input(f'Введите перевод к слову {word} на кыргызском языке ')
            elif lang == 'ru':
                ru_en[word] = input(f'Введите перевод к слову {word} на английском языке ')
                ru_kg[word] = input(f'Введите перевод к слову {word} на кыргызском языке ')
            elif lang == 'kg':
                en_ru[word] = input(f'Введите перевод к слову {word} на русском языке ')
                en_ru[word] = input(f'Введите перевод к слову {word} на английском языке ')