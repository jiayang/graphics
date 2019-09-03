from display import *
from draw import *
from matrix import *
import math

screen = new_screen()
color = [ 168, 80, 255 ]
matrix = new_matrix()


m1 = [
    [1,2,3,4],
    [2,4,8,6],
    [1,0,0,1],
    [3,4,5,6]
    ]

m2 = [[1,2,3,4],[6,5,22,1]]
print('Matrix 1')
print_matrix(m1)
print('Matrix 2')
print_matrix(m2)
matrix_mult(m1,m2)
print('Matrix 2 AFTER M1*M2')
print_matrix(m2)
print('Matrix 1 Turned into identity')
ident(m1)
print_matrix(m1)
print('M1*M2')
matrix_mult(m1,m2)
print_matrix(m2)

##DRAWING THE IMAGE
add_edge(matrix, 200,400,0, 300, 450,0)
add_edge(matrix, 0, 0, 0, 250,425,0)
add_edge(matrix, 250,425, 0, 400,250,0)
add_edge(matrix, 400, 250,0,450,0,0)
add_edge(matrix,0,475,0,10,480,0)
add_edge(matrix,10,480,0,15,495,0)
add_edge(matrix,15,495,0,25,500,0)
add_edge(matrix,250,250,0,300,275,0)
add_edge(matrix,300,275,0,300,225,0)
add_edge(matrix,300,225,0,250,200,0)
add_edge(matrix,250,250,0,250,200,0)
add_edge(matrix,250,250,0,225,275,0)
add_edge(matrix,300,275,0,275,300,0)
add_edge(matrix,250,250,0,200,200,0)
add_edge(matrix,200,200,0,200,150,0)
add_edge(matrix,200,150,0,250,200,0)
add_edge(matrix,200,200,0,178,213,0)

draw_lines( matrix, screen, color )
display(screen)
