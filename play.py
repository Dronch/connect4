from connect4.game import Game
from console_render import ConsoleRender


g = Game(6, 7, ('A', 'B'), 4)

try:
    g.play(
        input_func=ConsoleRender.player_input,
        win_callback=ConsoleRender.win,
        error_callback=ConsoleRender.error
    )
except KeyboardInterrupt:
    pass
