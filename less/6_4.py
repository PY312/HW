plane = {'11':'-','21':'-','31':'-',
         '12':'-','22':'-','32':'-',
         '13':'-','23':'-','33':'-'}


def print_plane():

    print("  1 2 3")
    print("1 %c %c %c" % (plane['11'], plane['21'], plane['31']))
    print("2 %c %c %c" % (plane['12'], plane['22'], plane['32']))
    print("3 %c %c %c" % (plane['13'], plane['23'], plane['33']))
    print('---------------------')


def player_1():

    while True:
        vvod = int(input("Игрок 1, введите № столбца и строки без пробела чтобы поставить Х :"))
        print(vvod)
        check = str(vvod)
        if check in plane:
            if plane[check] == '-':
                print('ура эта ячейка %c пуста' % (plane[check]))
                return vvod
            else:
                print('Эта ячейка уже занята')
        else:
            print("Вы ввели недопустимое знавение координаты!\n Введите № столбца и строки без пробела с 1 до 3-х:")




def player_2():

    while True:
        vvod = int(input("Игрок 2, введите № столбца и строки без пробела чтобы поставить O :"))
        print(vvod)
        check = str(vvod)
        if check in plane:
            if plane[check] == '-':
                print('ура эта ячейка %c пуста' % (plane[check]))
                return vvod
            else:
                print('Эта ячейка уже занята')
        else:
            print("Вы ввели недопустимое знавение координаты!\n Введите № столбца и строки без пробела с 1 до 3-х:")

def win_check(name):
         if (plane['11']  == plane['12'] == plane['13']) and (plane['11']  !=  '-'):
              print('Игрок %s выйграл' % (name))
              rezult = input('Введите Ваше имя для записи в таблице результатов  :')
              return True

         elif (plane['21']  == plane['22'] == plane['23']) and (plane['21']  !=  '-'):
               print('Игрок %s выйграл' % (name))
               rezult = input('Введите Ваше имя для записи в таблице результатов  :')
               return True

         elif (plane['31'] == plane['32'] == plane['33']) and (plane['31']  !=  '-'):
              print('Игрок %s выйграл' % (name))
              rezult = input('Введите Ваше имя для записи в таблице результатов  :')
              return True

         elif (plane['11'] == plane['21'] == plane['31']) and (plane['11']  !=  '-'):
              print('Игрок %s выйграл' % (name))
              rezult = input('Введите Ваше имя для записи в таблице результатов  :')
              return True

         elif (plane['12'] == plane['22'] == plane['32']) and (plane['12']  !=  '-'):
              print('Игрок %s выйграл' % (name))
              rezult = input('Введите Ваше имя для записи в таблице результатов  :')
              return True

         elif (plane['13'] == plane['23'] == plane['33']) and (plane['13']  !=  '-'):
              print('Игрок %s выйграл' % (name))
              rezult = input('Введите Ваше имя для записи в таблице результатов  :')
              return True

         elif (plane['11'] == plane['22'] == plane['33']) and (plane['11']  !=  '-'):
              print('Игрок %s выйграл' % (name))
              rezult = input('Введите Ваше имя для записи в таблице результатов  :')
              return True

         elif (plane['31'] == plane['22'] == plane['13']) and (plane['31']  !=  '-'):
              print('Игрок %s выйграл' % (name))
              rezult = input('Введите Ваше имя для записи в таблице результатов  :')
              return True

         elif '-' not in plane.values():
              print('Ничья!')
              return True

         else:
            print('---------------------')

while True:

    print_plane()
    step_x = str(player_1())
    print("Игрок 1, ваш ход",step_x)
    plane[step_x] = 'X'

    if win_check('Игрок 1'):
        print_plane()
        break


    print_plane()
    step_O = str(player_2())
    print("Игрок 2, ваш ход", step_O)
    plane[step_O] = 'O'

    if win_check('Игрок 2'):
        print_plane()
        break