from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

#variables here-----------------------------------------
cyan = (0, 255, 239)
purple = (205, 0, 255)
red = (255, 0, 0)
blank = (0, 0, 0)
slug = [[2,4], [3,4], [4,4]]
sense.set_pixel(2, 4, blank)
sense.set_pixel(3, 4, purple)
sense.set_pixel(4, 4, purple)
sense.set_pixel(5, 4, purple)
direction = "right"


#functions here-------------------------
def draw_slug():
    for segment in slug:
         sense.set_pixel(segment[0], segment[1], purple)
def move():
    
    




#main program here----------------------------------
sense.clear()

draw_slug()

while True:
    sleep(0.5)
