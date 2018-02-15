from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print_matrix(matrix)
ident(matrix)
add_edge( matrix, 300, 40, 500, 6, 700, 80 )
print_matrix(matrix)
ident(matrix)
print_matrix(matrix)

draw_lines(matrix, screen, color)


# draw_lines( matrix, screen, color )
# display(screen)
