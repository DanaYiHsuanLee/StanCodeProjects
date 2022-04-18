"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This is a game to get score from hitting a brick.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of tBhe ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 8       # Maximum initial horizontal speed for the ball
new_score = 0          # global variable


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.bo = brick_offset
        self.pd = GRect(width=paddle_width, height=paddle_height, x=(self.window.width-paddle_width)/2,
                        y=self.window.height-paddle_height-paddle_offset)
        self.window.add(self.pd)
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2, x=(self.window.width-ball_radius*2)/2, y=(self.window.height-ball_radius*2)/2)
        self.window.add(self.ball)
        self.bs = brick_spacing
        self.bo = brick_offset
        self.brick = GRect(width=brick_width, height=brick_height, y=self.bo)
        self.br = brick_rows
        self.bc = brick_cols
        self.ini_x = 0      # initial x position of brick
        self.ini_y = self.bo         # initial y position of brick
        self.between_x = self.brick.width + self.bs   # space x distance of brick
        self.between_y = self.brick.height + self.bs  # space y distance of brick
        self.brick_wall()
        self.label = GLabel(f'My Score: {new_score}')
        self.dx = random.randint(1, MAX_X_SPEED)
        self.dy = random.randint(INITIAL_Y_SPEED, 10)
        self.switch = True
        self.window.add(self.label, x=0, y=self.label.height)

        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_drop)

    def ball_drop(self, mouse):
        if self.switch:
            if random.random() > 0.5:
                self.dx = -self.dx
        self.switch = False

    def get_switch(self):    # control if start the game
        return self.switch

    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy

    def paddle_move(self, event):
        if event.x <= self.pd.width:
            self.window.add(self.pd, x=0, y=self.pd.y)
        elif event.x >= self.window.width-self.pd.width:
            self.window.add(self.pd, x=self.window.width-self.pd.width, y=self.pd.y)
        else:
            self.window.add(self.pd, x=event.x-self.pd.width/2, y=self.pd.y)

    def brick_wall(self):
        for i in range(self.bc):
            brick = GRect(width=self.brick.width, height=self.brick.height)
            self.window.add(brick, x=self.ini_x, y=self.ini_y)
            for j in range(self.br):
                self.ini_x += self.between_x
                brick = GRect(width=self.brick.width, height=self.brick.height)
                self.window.add(brick, x=self.ini_x, y=self.ini_y)
            self.ini_x = 0
            self.ini_y += self.between_y

    def ball_hit(self):
        global new_score
        for i in range(0, self.ball.width + 1, self.ball.width):
            for j in range(0, self.ball.height + 1, self.ball.height):
                ball_x = self.ball.x + i
                ball_y = self.ball.y + j
                obj = self.window.get_object_at(ball_x, ball_y)
                if obj is self.pd:
                    self.dy = -self.dy
                    return
                elif obj is not self.label and obj is not None:  # brick collision
                    new_score += 1
                    self.window.remove(self.label)
                    self.window.remove(obj)
                    self.label = GLabel(f'My Score: {new_score}')
                    self.window.add(self.label, x=0, y=self.label.height)
                    self.dy = -self.dy
                    self.dy += 0.5
                    return






























