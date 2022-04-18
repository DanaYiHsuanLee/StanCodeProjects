"""
File: my_drawing.py
Name:Dana
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GArc, GLine, GPolygon, GLabel
from campy.graphics.gwindow import GWindow
import random
from campy.gui.events.timer import pause

window = GWindow(width=800, height=400)
def main():
    """
    Title: my favorite Totoro.
    I still believe there is a totoro somewhere on Earth until now.
    """
    # body
    arc0 = GArc(400, 600, 0, 90)
    window.add(arc0, x=400, y=200)
    arc1 = GArc(400, 600, 90, 45)
    window.add(arc1, x=400, y=200)
    # the animals on its head
    line0 = GLine(510, 180, 500, 200)
    window.add(line0)
    line1 = GLine(480, 180, 470, 200)
    window.add(line1)
    line2 = GLine(480, 180, 470, 170)
    window.add(line2)
    line3 = GLine(510, 180, 520, 180)
    window.add(line3)
    line4 = GLine(510, 150, 520, 180)
    window.add(line4)
    line5 = GLine(510, 150, 470, 170)
    window.add(line5)
    line0 = GLine(460, 180, 455, 200)
    window.add(line0)
    line1 = GLine(450, 180, 445, 205)
    window.add(line1)
    line2 = GLine(450, 180, 440, 170)
    window.add(line2)
    line3 = GLine(460, 180, 470, 180)
    window.add(line3)
    line4 = GLine(470, 150, 470, 180)
    window.add(line4)
    line5 = GLine(470, 150, 440, 170)
    window.add(line5)
    eye = GOval(7, 7, x=420, y=192)
    window.add(eye)
    eye = GOval(3, 3, x=420, y=195)
    eye.filled = True
    eye.color = 'black'
    window.add(eye)
    eye = GOval(6, 6, x=413, y=196)
    window.add(eye)
    eye = GOval(2.5, 2.5, x=413, y=198)
    eye.filled = True
    eye.color = 'black'
    window.add(eye)
    # its hair
    hair = GLine(504, 190, 512, 190)
    window.add(hair)
    hair1 = GLine(504, 192, 512, 192)
    window.add(hair1)
    hair2 = GLine(504, 194, 512, 194)
    window.add(hair2)
    hair3 = GLine(504, 196, 512, 196)
    window.add(hair3)
    hair1 = GLine(447, 192, 441, 192)
    window.add(hair1)
    hair2 = GLine(447, 190, 441, 190)
    window.add(hair2)
    hair3 = GLine(447, 194, 441, 194)
    window.add(hair3)
    hair1 = GLine(462, 192, 456, 192)
    window.add(hair1)
    hair2 = GLine(462, 194, 456, 194)
    window.add(hair2)
    hair3 = GLine(462, 196, 456, 196)
    window.add(hair3)
    hair1 = GLine(477, 192, 471, 192)
    window.add(hair1)
    hair2 = GLine(477, 194, 471, 194)
    window.add(hair2)
    hair3 = GLine(477, 196, 471, 196)
    window.add(hair3)
    # its body
    arc = GArc(20, 100, 180, 90)
    window.add(arc, x=412, y=165)
    arc = GArc(20, 40, 280, 110)
    window.add(arc, x=408, y=165)
    arc = GArc(20, 40, 0, 90)
    window.add(arc, x=410, y=175)
    line = GLine(420, 190, 425, 165)
    window.add(line)
    line = GLine(425, 165, 430, 185)
    window.add(line)
    arc = GArc(30, 80, 360, 120)
    window.add(arc, x=420, y=185)
    arc = GArc(80, 70, 100, 115)
    window.add(arc, x=400, y=213)
    line = GLine(400, 255, 385, 260)
    window.add(line)
    hair1 = GLine(388, 257, 398, 257)
    window.add(hair1)
    hair2 = GLine(388, 260, 398, 260)
    window.add(hair2)
    arc = GArc(15, 15, 100, 115)
    window.add(arc, x=382, y=260)
    arc = GArc(30, 30, 100, 160)
    window.add(arc, x=378, y=268)
    hair1 = GLine(368, 280, 378, 285)
    window.add(hair1)
    hair2 = GLine(358, 287, 378, 287)
    window.add(hair2)
    hair2 = GLine(368, 289, 378, 289)
    window.add(hair2)
    hair3 = GLine(368, 299, 380, 296)
    window.add(hair3)
    line = GLine(368, 299, 338, 350)
    window.add(line)
    arc = GArc(350, 350, 0, 90)
    window.add(arc, x=280, y=299)
    # the marks on its body
    tri = GPolygon()
    tri.add_vertex((365, 325))
    tri.add_vertex((375, 330))
    tri.add_vertex((370, 310))
    tri.filled = True
    tri.fill_color = 'gray'
    window.add(tri)
    tri = GPolygon()
    tri.add_vertex((380, 335))
    tri.add_vertex((400, 345))
    tri.add_vertex((390, 313))
    tri.filled = True
    tri.fill_color = 'gray'
    window.add(tri)
    tri = GPolygon()
    tri.add_vertex((400, 350))
    tri.add_vertex((420, 360))
    tri.add_vertex((410, 328))
    tri.filled = True
    tri.fill_color = 'gray'
    window.add(tri)
    eye = GOval(20, 20, x=413, y=255)
    window.add(eye)
    eye = GOval(8, 8, x=415, y=260)
    eye.filled = True
    eye.fill_color = 'black'
    window.add(eye)
    # its umbrella
    line = GLine(420, 310, 460, 315)
    window.add(line)
    line = GLine(420, 310, 440, 315)
    window.add(line)
    line = GLine(420, 290, 450, 285)
    window.add(line)
    line = GLine(420, 290, 440, 285)
    window.add(line)
    line = GLine(420, 297, 455, 295)
    window.add(line)
    line = GLine(420, 297, 450, 295)
    window.add(line)
    line = GLine(361, 310, 361, 130)
    line.color = 'seagreen'
    window.add(line)
    arc = GArc(100, 100, 0, 180)
    arc.filled = True
    arc.fill_color = 'limegreen'
    arc.color = 'limegreen'
    window.add(arc, x=360, y=110)
    # title
    title = GLabel('ダナ・リー作品')
    title.font = "SansSerif-20"
    window.add(title, x=550, y=300)
    title = GLabel('StanCode')
    title.font = "Courteous-20"
    window.add(title, x=550, y=320)

    while True:   # rain
        x = random.randint(200, window.width)
        y = random.randint(100, window.height)
        rain1 = GLine(x, y, x, y+15)
        rain1.color = 'deepskyblue'
        window.add(rain1)
        x1 = random.randint(200, window.width)
        y1 = random.randint(0, window.height)
        rain2 = GLine(x1, y1, x1, y1 + 15)
        rain2.color = 'deepskyblue'
        window.add(rain2)
        window.remove(rain1)
        x3 = random.randint(200, window.width)
        y3 = random.randint(100, window.height)
        rain3 = GLine(x3, y3, x3, y3 + 15)
        rain3.color = 'steelblue'
        window.add(rain3)
        pause(200)
        window.remove(rain2)
        window.remove(rain3)

if __name__ == '__main__':
    main()
