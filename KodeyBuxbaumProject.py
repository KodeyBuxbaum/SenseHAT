from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

#variables here-----------------------------------------
cyan = (0, 255, 239)
purple = (205, 0, 255)
red = (255, 0, 0)
blank = (0, 0, 0)
slug = [[3,4], [4,4], [5, 4]]
sense.set_pixel(2, 4, blank)
sense.set_pixel(3, 4, red)
sense.set_pixel(4, 4, purple)
direction = "right"


#functions here-------------------------
def draw_slug():
    for segment in slug:
         sense.set_pixel(segment[0], segment[1], purple)

def move():
    last = slug[-1]
    first = slug[0]
    next = list(last)
    if direction == "right":
        next[0] = last[0] + 1
        sense.set_pixel(next[0], next[1], purple)
        sense.set_pixel(last[0], last[1], blank)
        slug.remove(first)
        if last[0] + 1 == 7:
            next[0] = 0
        else:
            next[0] = last[0] + 1






#main program here----------------------------------
sense.clear()
while True:
    draw_slug()
    move()
