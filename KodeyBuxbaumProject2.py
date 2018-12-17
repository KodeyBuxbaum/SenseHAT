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
white = (255, 255, 255)
vegetables = []
score = 0
#functions here-------------------------
def draw_slug():
    for segment in slug:
         sense.set_pixel(segment[0], segment[1], purple)

def move():
    global score
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
    else:
        pass

        
    
    slug.append(next)
    sense.set_pixel(next[0], next[1], purple)
    sense.set_pixel(first[0], first[1], blank)
    slug.remove(first)
    """
    if next in vegetables:
        vegetables.remove(next)
        score = score + 1
    #remove = True
    if remove == True:
        if score % 5 == 0:
            sense.set_pixel(first[0], first[1], blank)
    



def joystick_moved(event):
    global direction
    direction = event.direction


def make_veg():
    new = slug[0]
    while new in slug:
        x = randint(0, 7)
        y = randint(0, 7)
        new = [x, y]
        vegetables.append(new)
        sense.set_pixel(x,y, white)
        """
#main program here----------------------------------
sense.clear()

while True:
    sleep(0.5)
    draw_slug()
    move()
    































    

    
