"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000



def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    between_x = (width-GRAPH_MARGIN_SIZE*2)/len(YEARS)-1  # the distance between every year
    x = GRAPH_MARGIN_SIZE+between_x*year_index
    return x


def get_y_coordinate(height, rank_index):
    """
    Given the height of the canvas and the index of the current rank
    of the year, returns the y coordinate of the horizontal
    line associated with the rank.

    Input:
        height (int): The height of the canvas
        rank_index (int): The index where the rank of the year
    Returns:
         triple: rank_index,  y coordinate
    """
    between_y = (height-GRAPH_MARGIN_SIZE*2)/(MAX_RANK-1)  # the distance between every rank
    y = GRAPH_MARGIN_SIZE + between_y*rank_index
    return rank_index, y


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=1900+10*i, anchor=tkinter.NW,
                           font='times 10')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    point_xy = {}   # dict, [x:y] coordinates
    for name in lookup_names:
        color = change_color()
        if name in name_data:
            for year in YEARS:
                year_index = (int(year) - 1900) / 10   # transform index of year
                x = get_x_coordinate(CANVAS_WIDTH, year_index)
                if str(year) in name_data[name]:
                    yearr = str(year)  # int>>str
                    rank_index = int(name_data[name][yearr]) - 1   # transform index of rank
                    if rank_index <= MAX_RANK - 1:
                        y = get_y_coordinate(CANVAS_HEIGHT, rank_index)
                    else:
                        y = rank_index, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    y = MAX_RANK+1, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                point_xy[x] = y

            switch = True
            for key, value in point_xy.items():
                rank = value[0]+1
                if rank <= 1000:
                    canvas.create_text(key, value[1], text=f'{name} {rank}', anchor=tkinter.SW,
                                       font='times 10', fill=color)
                else:
                    canvas.create_text(key, value[1], text=f'{name} *', anchor=tkinter.SW,
                                       font='times 10', fill=color)
                if switch:
                    a = key
                    b = value[1]
                    switch = False
                else:
                    c = key
                    d = value[1]
                    canvas.create_line(a, b, c, d, width=LINE_WIDTH, fill=color)
                    a = c
                    b = d


def change_color():
    """
    to change color of line
    """
    color = COLORS.pop(0)
    COLORS.append(color)
    return color


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
