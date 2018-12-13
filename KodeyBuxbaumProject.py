from sense_hat import SenseHat
from time import *
from random import *
sense = SenseHat()

#variables here-----------------------------------------
direction = "right"
purple = (205, 0, 255)
blank = (0, 0, 0)
slug = [[3,4], [4,4], [5, 4]]
sense.set_pixel(2, 4, blank)
sense.set_pixel(3, 4, purple)
sense.set_pixel(4, 4, purple)
veggie_color = (255, 255, 255)
vegetables =[]

#functions here-------------------------
def draw_slug():
    for segment in slug:
         sense.set_pixel(segment[0], segment[1], purple)

def move():
    last = slug[-1]
    first = slug[0]
    next = list(last)
    if direction == "right":
        if last[0] + 1 == 8:
            next[0] = 0
        else:
            next[0] = last[0] + 1
    elif direction == "left":
        if last[0] - 1 == -1:
            next[0] = 7
        else:
            next[0] = last[0] - 1
    elif direction == "down":
        if last[1] + 1 == 8:
            next[1] = 0
        else:
            next[1] = last[1] + 1
    elif direction == "up":
        if last[1] - 1 == -1:
            next[1] = 7
        else:
            next[1] = last[1] - 1

        
    sense.set_pixel(next[0], next[1], purple)
    sense.set_pixel(first[0], first[1], blank)
    slug.append(next)
    slug.remove(first)



def joystick_moved(event):
    global direction
    direction = event.direction


def make_veg():
    x = randint(0, 7)
    y = randint(0, 7)
    new = [x, y]
    while new in slug:
        x = randint(0, 7)
        y = randint(0, 7)
        new = [x, y, veggie_color]
        if len(vegetables) < 3:
            make_veg()
        vegetables.append(new)
#main program here----------------------------------
sense.clear()

while True:
    sleep(0.5)
    draw_slug()
    move()
    sense.stick.direction_any = joystick_moved
    make_veg()
    sense.set_pixel































    

    
