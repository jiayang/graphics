from display import *
from draw import *
from parser import parse_file
from matrix import *

screen = new_screen()
color = [ 0, 222, 255 ]
edges = []
transform = new_matrix()

parse_file('script', edges, transform, screen, color)
