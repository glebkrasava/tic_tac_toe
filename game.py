from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def save_result(result):
    with open('results.txt', 'a') as file:
        file.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.size}.'
                )
                print('введите значения для строки и столбца заново.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break
        game.make_move(row, column, current_player)
        game.display()
        result = f'Победили {current_player}!'
        if game.check_win(current_player):
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = 'Ничья!'
            print('Ничья!')
            save_result(result)
            running = False
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
file = open('results.txt', 'r')
content = file.read(-1)
print(content)
file.close()
