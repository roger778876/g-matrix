from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
YELLOW = [255, 255, 0]
matrix1 = new_matrix()
matrix2 = new_matrix()

print "testing new_matrix"
print "matrix1"
print_matrix(matrix1)
print "matrix2"
print_matrix(matrix2)

print "testing ident on matrix1"
print "new matrix1"
ident(matrix1)
print_matrix(matrix1)

print "testing del_matrix on matrix2"
print "new matrix2"
del_matrix(matrix2)
print_matrix(matrix2)

print "testing add_edge on matrix2"
print "new matrix2"
add_edge(matrix2, 1, 2, 3, 4, 5, 6)
add_edge(matrix2, 7, 8, 9, 10, 11, 12)
print_matrix(matrix2)

print "testing add_point on matrix2"
print "new matrix2"
add_point(matrix2, 13, 14, 15)
add_point(matrix2, 16, 17, 18)
print_matrix(matrix2)

print "testing matrix_mult (m1 * m2)"
print "new matrix2 after mult w/ identity m1"
matrix_mult(matrix1, matrix2)
print_matrix(matrix2)

print "new matrix2 after mult w/ 0 matrix"
matrix1 = new_matrix()
matrix_mult(matrix1, matrix2)
print_matrix(matrix2)


'''drawing!'''
del_matrix(matrix2)
for x in range(0, 15):
  for y in range(0, 15):
    x0 = x
    y0 = y
    x1 = random.randint(0, 500)
    y1 = random.randint(0, 500)
    add_edge(matrix2, x0, y0, 0, x1, y1, 0)

draw_lines(matrix2, screen, YELLOW)
display(screen)
