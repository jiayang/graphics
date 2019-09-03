import math
from display import *

  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 2

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    a = calculate_ambient(ambient,areflect)
    d = calculate_diffuse(light,dreflect,normal)
    s = calculate_specular(light,sreflect,view,normal)
    #a = [0,0,0]
    #s = [0,0,0]
    #d = [0,0,0]
    color = sum(a,d,s)
    limit_color(color)
    return color

def calculate_ambient(alight, areflect):
    return [alight[i] * areflect[i] for i in range(len(alight))]

def calculate_diffuse(light, dreflect, normal):
    l,col = light
    normalize(l)
    normalize(normal)
    c = dot_product(l,normal)
    return [dreflect[i] * col[i] * c for i in range(len(dreflect))]
def calculate_specular(light, sreflect, view, normal):
    l,col = light
    normalize(l)
    normalize(normal)
    normalize(view)
    c = dot_product(subtract(distribute(2*dot_product(l,normal),normal),l),view)
    c = ( abs(c) ** SPECULAR_EXP) * c / abs(c) 
    return [sreflect[i] * col[i] * c for i in range(len(sreflect))]

def limit_color(color):
    for i in range(len(color)):
        a = color[i]
        color[i] = a if a <= 255 and a > 0 else 255 if a > 255 else 0
    return color
#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude
def subtract(a,b):
    return [a[i] - b[i] for i in range(len(a))]
def distribute(c,a):
    return [c * e for e in a]
def sum(*args):
    lst = []
    for i in range(len(args[0])):
        x = 0
        for j in range(len(args)):
            x += args[j][i]
        lst.append(x)
    return lst
#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
