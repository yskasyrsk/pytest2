from blessed import Terminal
import time

term = Terminal()
string = "Hello from Blessed"
y = 10

#define visible part
def visible(x, string):
    if x < 0:
        return string[-x:]
    elif x + len(string) > term.width:
        return string[:term.width - x]
    else:
        return string

with term.fullscreen(), term.hidden_cursor():
    for i in range(-len(string),term.width):
        #clean the line before printing new
        print(term.move_xy(0,y) + term.clear_eol, end='', flush=True)

        vis_text = visible(i,string)
        print(term.move_xy(max(0, i), y) + vis_text + term.color(i%15) +
              ' ' * (term.width - (max(0, i) + len(vis_text))), end='', flush=True)
        time.sleep(0.05)




