import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    mag = sum([i * i for i in vector])
    mag = math.pow(mag,.5)
    for i in range(len(vector)):
        vector[i] = vector[i]/mag
        
#Return the dot porduct of a . b
def dot_product(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p0,p1,p2 = polygons[i:i+3]
    v0 = [p1[i] - p0[i] for i in range(3)]
    v1 = [p2[i] - p0[i] for i in range(3)]
    return cross(v0,v1)

def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
    
