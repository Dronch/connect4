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
        ConsoleRender.draw_field(field, players)
        return input(f'\nTurn {player}: ')

    @staticmethod
    def win(player, line, field, players):
        ConsoleRender.draw_field(field, players)
        print(f'!!! {player} WIN !!!')
        time.sleep(2)
        os.system('cls||clear')
        rows, cols = field.shape
        for x in range(rows):
            print(
                ''.join([
                    ('*' if (x, y) in line else str(players[field[x, y]])) if field[x, y] else 'o'
                    for y in range(cols)
                ])
            )
        print(f'!!! {player} WIN !!!')
        print('* - final line')

    @staticmethod
    def error(error):
        print(error)
        time.sleep(1)
