from blessed import Terminal
import time

term = Terminal()

with term.fullscreen():
    print(term.move_xy(10, 10) + term.color(2) + term.on_color(4) + term.bold('Welcome to the Matrix'))
    time.sleep(2)