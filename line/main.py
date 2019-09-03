from display import *
from draw import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]

for i in range(360):    
    draw_line(250,250,int(round(math.cos(math.radians(i)) * 200) + 250), int(round(math.sin(math.radians(i)) * 200) + 250),screen,[100,0,(i * 2) % 256])

x = 250
y = 250
theta = 0
for i in range(350):
    newtheta = theta + 10
    newx = x + int(round(math.cos(math.radians(theta)) * i / 10))
    newy = y + int(round(math.sin(math.radians(theta)) * i / 10))
    draw_line(x,y,newx,newy,screen,[(i*2) % 256,255 - (i%256),i%256])
    x,y,theta = newx,newy,newtheta
    
draw_line(250,450,63,168,screen,[255,255,0])
draw_line(250,450,437,168,screen,[255,255,0])
draw_line(437,168,63,168,screen,[255,255,0])


    
display(screen)
save_extension(screen, 'img.png')
