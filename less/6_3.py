plane = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*'],
]
def input_x_y():
    return int(input('по горизонтали  :')) -1, int(input('по вертикали   :')) - 1

def print_plane(plane):
    for i in range(3):
        row = plane[i]
        print(f'{row[0]} | {row[1]} | {row[2]}')
        if i != 2:
            print('-'*9)
while True:
    print_plane(plane)
    print ('Первый игрок')
    player_1_x, player_1_y = input_x_y()
    plane[player_1_x][player_1_y] = 'X'
    print_plane(plane)
    if
    print('Второй игрок')
    player_2_x, player_2_y = input_x_y()
    plane[player_2_x][player_2_y] = 'O'
    print_plane(plane)

def check_winner(p):
    for i range(3):
        row = plane[i]



