from tkinter import *
import random
import math

root = Tk()

width=400
height=400

canvas = Canvas(root, width=width, height=height)

ranpoint = [(random.choice(list(range(width))[::2]), random.choice(list(range(height))[::2])) for i in range(150)]

canvas.pack()

def p5map(n, start1, stop1, start2, stop2):
  return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

for x in list(range(height))[::2]:
    for y in list(range(width))[::2]:
        distance = []
        for i, j in ranpoint:
            dist = math.sqrt((x-i)**2 + (y-j)**2)
            distance.append(dist)
        n = 0
        distance.sort()
        noise = int(p5map(distance[n], 0, 50, 0, 255))
        if noise > 255:
            noise = 255
        
        canvas.create_rectangle(x, y, x+1, y+1, fill=rgb_to_hex((noise, noise, noise)), outline = rgb_to_hex((noise, noise, noise)))
        #root.update()
        


root.mainloop()
