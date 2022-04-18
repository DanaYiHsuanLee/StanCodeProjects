"""
File: bouncing.ball.py
Name:Dana
-------------------------
This program shows the process of a ball falling down the floor by a mouse click.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = 'black'
window.add(ball)
count = 1
switch = True
ga = 0

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    onmouseclicked(drop)

def drop(mouse):
    global switch
    switch = True
    global count
    while switch:       # if the ball starts to drop
        global ga
        global ball
        if count <= 3:
            ga += GRAVITY
            ball.move(VX, ga)
            pause(DELAY)
            if ball.y + ball.height >= window.height and ga > 0:
                ga = -ga * REDUCE
            if ball.x + ball.width > window.width:
                window.remove(ball)
                ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
                ball.filled = True
                ball.fill_color = 'black'
                window.add(ball)
                count += 1
                switch = False
                break
        else:
            switch = False

if __name__ == "__main__":
    main()
