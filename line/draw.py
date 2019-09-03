from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 - x1 > 0:
        x0,y0,x1,y1 = x1,y1,x0,y0
        
    dx = x1 - x0
    dy = y1 - y0

    a = dy
    b = -1 * dx

    x = x0
    y = y0
    
    #OCT1
    if dy >= 0 and dx > dy:
        d = 2 * a + b
        while x <= x1:
            plot(screen,color,x,y)
            if d > 0:
                y += 1
                d += 2 * b
            x += 1
            d += 2 * a
    #OCT2
    elif dy > 0 and dy >= dx:
        d = 2 * b + a
        while y <= y1:
            plot(screen,color,x,y)
            if d < 0:
                x += 1
                d += a * 2
            y += 1
            d += b * 2

    #OCT7
    elif dy < 0 and -1 * dy > dx:
        d = -2 * b + a
        while y >= y1:
            plot(screen,color,x,y)
            if d >= 0:
                x += 1
                d += a * 2
            y -= 1
            d += b * -2

    #OCT8
    elif dy < 0 and dx >= dy * -1:
        d = 2 * a - b
        while x <= x1:
            plot(screen,color,x,y)
            if d <= 0:
                y -= 1
                d += -2 * b
            x += 1
            d += 2 * a
    
