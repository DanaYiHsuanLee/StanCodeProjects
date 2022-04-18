"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage

BLUR=5
def blur(img):
    """
    :param img:img,the original smiley-face
    :return: image, after blurred
    """
    new = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x,y)
            new_pixel = new.get_pixel(x,y)
            r = 0
            g = 0
            b = 0
            n = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    new_x = x+i
                    new_y = y+j
                    if img.width>new_x>-1 and img.height>new_y>-1:
                        newxy = img.get_pixel(new_x,new_y)
                        r += newxy.red
                        g += newxy.green
                        b += newxy.blue
                        n += 1
            new_r = r/n
            new_g = g/n
            new_b = b/n
            new_pixel.red = new_r
            new_pixel.green = new_g
            new_pixel.blue = new_b
    return new

def main():
    """
    TODO:
    """
    img = SimpleImage("images/smiley-face.png")
    img.show()
    blurred_img = blur(img)
    blurred_img.show()
    for i in range(BLUR):
        blurred_img = blur(blurred_img)
    blurred_img.show()





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
