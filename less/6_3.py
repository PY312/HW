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


def check_winner(plane):
    for i in range(3):
        if plane[i][0] != '*'and plane[i][0] == plane[i][1] == plane[i][2]:
            return plane[i][0]

    for i in range(3):
        if plane[0][i] != '*' and plane[0][i] == plane[1][i] == plane[2][i]:
            return plane[0][i]

    if plane[0][0] != '*' and plane[0][0] == plane[1][1] == plane[2][2]:
        return plane[0][0]
    if plane[0][2] != '*' and plane[0][2] == plane[1][1] == plane[2][0]:
        return plane[2][0]


def save_result(winner):
    player1, player2 = input(), input()
    file = open('results.txt', 'a+')
    file.write(f"{player1} {player2} - {winner}")


def main():
    for i in range(9):
        print_plane(plane)
        print('Первый игрок')
        player_1_x, player_1_y = input_x_y()
        if i % 2 == 0:
            player = "X"
        else:
            player = 'O'
        plane[player_1_x][player_1_y] = player
        is_win = check_winner(plane)
        if is_win:
            save_result(is_win)
            break
    save_result("Draw")


main()
