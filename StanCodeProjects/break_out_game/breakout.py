"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is a game to get score from hitting a brick.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    num = 0
    while True:
        while 0 < graphics.ball.y < graphics.window.height:
            if not graphics.switch:
                if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                    graphics.dx = -graphics.dx
                elif graphics.ball.y <= 0:
                    graphics.dy = -graphics.dy
                graphics.ball_hit()
                graphics.ball.move(graphics.dx, graphics.dy)
                pause(FRAME_RATE)
            pause(FRAME_RATE)
        num += 1
        if num == NUM_LIVES:
            break
        else:
            graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                y=(graphics.window.height - graphics.ball.height) / 2)
            graphics.switch = True
    label = GLabel('GAME OVER !')
    label.color = 'red'
    graphics.window.add(label, x=(graphics.window.width - label.width) / 2,
                        y=(graphics.window.height - label.height) / 2)
    graphics.window.add(graphics.label, x=(graphics.window.width - label.width) / 2,
                        y=(graphics.window.height - label.height)*0.75)


if __name__ == '__main__':
    main()
