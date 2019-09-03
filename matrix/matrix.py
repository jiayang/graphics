"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ''
    for i in range(4):
        line = ''
        for j in range(len(matrix)):
            line += str(matrix[j][i]) + ' '
        s += line + '\n'
    print(s)
    
#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m3 = []
    for i in range(4):
        row = [m1[j][i] for j in range(4)]
        final_row = [dot_product(row,col) for col in m2]
        m3.append(final_row)
    for i in range(len(m3)):
        for j in range(len(m3[i])):
            m2[j][i] = m3[i][j]
    

#Assume v1,v2 same size vectors
def dot_product(v1,v2):
    x = 0
    for i in range(len(v1)):
        x += v1[i] * v2[i]
    return x

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
