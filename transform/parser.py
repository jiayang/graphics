from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open(fname)
    lines = [line.strip() for line in f]
    i = 0
    while True:
        if lines[i] == 'line':
            c = lines[i+1].split()
            x0,y0,z0,x1,y1,z1 = [int(v) for v in c]
            add_edge(points,x0,y0,z0,x1,y1,z1)
            i += 2
            continue
        if lines[i] == 'ident':
            transform = new_matrix()
            ident(transform)
            i += 1
            continue
        if lines[i] == 'scale':
            sf = [int(v) for v in lines[i+1].split()]
            matrix_mult(make_scale(sf[0],sf[1],sf[2]),transform)
            i += 2
            continue
        if lines[i] == 'translate' or lines[i] == 'move':
            tm = [int(v) for v in lines[i+1].split()]
            matrix_mult(make_translate(tm[0],tm[1],tm[2]),transform)
            i += 2
            continue
        if lines[i] == 'rotate':
            r = {
                'x' : make_rotX,
                'y' : make_rotY,
                'z' : make_rotZ
                }
            next_row = lines[i+1].split()
            matrix_mult(r[next_row[0]](int(next_row[1])),transform)
            i += 2
            continue
        if lines[i] == 'apply':
            matrix_mult(transform,points)
            points = [[int(val) for val in row] for row in points]
            i += 1
            continue
        if lines[i] == 'display':
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
            i += 1
            continue
        if lines[i] == 'save':
            fout = lines[i+1]
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
            i += 2
            continue
        if lines[i] == 'quit':
            return
