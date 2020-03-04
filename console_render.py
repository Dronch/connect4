import os
import time


class ConsoleRender(object):

    @staticmethod
    def draw_field(field, players):
        os.system('cls||clear')
        rows, cols = field.shape
        for x in range(rows):
            print(''.join([str(players[field[x, y]]) if field[x, y] else 'o' for y in range(cols)]))

    @staticmethod
    def player_input(player, field, players):
        while True:
            ConsoleRender.draw_field(field, players)
            col = input(f'\nTurn {player}: ')
            if col.isdigit():
                return int(col)
            else:
                print('Invalid input')
                time.sleep(1)

    @staticmethod
    def win(player, line, field):
        print(f'!!! {player} WIN !!!')

    @staticmethod
    def error(error):
        print(error)
        time.sleep(1)
