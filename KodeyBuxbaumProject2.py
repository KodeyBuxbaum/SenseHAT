from sense_hat import SenseHat
from time import *
from random import *
sense = SenseHat()

#variables here-----------------------------------------
direction = "right"
purple = (205, 0, 255)
1 = randint(0, 255)
2 = randint(0, 255)
3 = randint(0, 255)
blank = (0, 0, 0)
slug = [[3,4], [4,4], [5, 4]]
sense.set_pixel(2, 4, blank)
sense.set_pixel(3, 4, purple)
sense.set_pixel(4, 4, purple)
white = (255, 255, 255)
vegetables = []
score = 0
pause = 0.5
dead = False
colors = (1, 2, 3, purple)
#functions here-------------------------
def draw_slug():
    for segment in slug:
        while True:
            sense.set_pixel(segment[0], segment[1], colors)
            sleep(0.5)

def move():
    global pause
    global score
    global dead
    last = slug[-1]
    first = slug[0]
    next = list(last)
    remove = True
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
    if next in vegetables:
        vegetables.remove(next)
        score = score + 1
        if score % 5 == 0 and score > 0:
            remove = False
            pause = pause * 0.8
        if score % 5 == 0 and score > 0:
             remove = False
    
    if remove == True:
        sense.set_pixel(first[0], first[1], blank)
        slug.remove(first)
    if next in slug:
        dead = True
    slug.append(next)
    sense.set_pixel(next[0], next[1], purple)
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



#main program here----------------------------------
sense.clear()
while True:
    if dead == False:
        sleep(pause)
        draw_slug()
        move()
        sense.stick.direction_any = joystick_moved
        if len(vegetables) < 3:
            make_veg()
    else:
        sense.show_message("Your score was: " + str(score) + " Congrats!")































    

    
