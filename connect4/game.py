import numpy as np
import itertools

from .errors import InvalidInputError


class Game(object):

    def __init__(self, rows: int, cols: int, players: tuple, goal: int):

        if len(players) < 2:
            raise ValueError('More than 2 players required')

        self.rows = rows
        self.cols = cols
        self.goal = goal
        self.field = np.zeros((rows, cols))
        self.players = {idx + 1: name for idx, name in enumerate(players)}

    def turn(self, player: int, col: int):
        empty = len(list(itertools.filterfalse(lambda x: x > 0, self.field[:, col])))

        if empty == 0:
            raise InvalidInputError(f'No available cells on col {col}')

        self.field[empty - 1][col] = player

    def line(self, x, y, direction):
        player = self.field[x, y]
        yield x, y

        for _ in itertools.count(0, 1):
            x, y = x + direction[0], y + direction[1]

            out_of_field = x not in range(self.rows) or y not in range(self.cols)
            if out_of_field or self.field[x, y] != player:
                break

            yield x, y

    def winner(self, player):
        visited = []
        for x in range(self.rows):
            for y in range(self.cols):
                if (x, y) in visited or self.field[x, y] != player:
                    continue

                for step_x in [-1, 0, 1]:
                    for step_y in [-1, 0, 1]:
                        if step_x == 0 and step_y == 0:
                            continue

                        line = list(self.line(x, y, (step_x, step_y)))

                        if len(line) == self.goal:
                            return line

                        visited += line

    def play(self, input_func, win_callback, error_callback):
        for player in itertools.cycle(self.players):

            while True:
                try:
                    col = input_func(self.players[player], self.field, self.players)
                    out_of_field = col not in range(self.cols)
                    if out_of_field:
                        raise InvalidInputError(f'Please enter col number: 0-{self.cols - 1}')
                    self.turn(player, col)
                    break
                except InvalidInputError as e:
                    error_callback(str(e))

            line = self.winner(player)

            if line:
                win_callback(self.players[player], line, self.field)
                break
