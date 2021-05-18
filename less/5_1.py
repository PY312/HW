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
         'эркек':'man'}
en_ru = {'money':'деньги',
         'red':'красный',
         'key':'ключ'}
en_kg = {'money': 'акча',
         'red': 'кызыл',
         'girl':'кыз'}

dictionary = ['English', en_kg, 'Kyrgyz'], \
             ['English', en_ru, 'Russian'], \
             ['Кыргызский',kg_ru, 'Russian'] ,\
             ['Кыргызский',kg_en, 'English'], \
             ['Русский', ru_en, 'English'],\
             ['Русский', ru_kg, 'Kyrgyz']

while True:
    word = input('Введите слово для перевода :')
    for i in dictionary:
        for key in i[1]:
            if key == word:
                print("Язык оригинал: " + i[0])
                print("Язык перевода: " + i[2])
                print(i[1][key])