from display import *
from matrix import *


# reads point pairs from matrix and draws lines
# ignores z axis for now
def draw_lines( matrix, screen, color ):
  matrix_len = len(matrix)
  point_pair = 0
  while (point_pair < matrix_len):
    x0 = matrix[point_pair][0]
    y0 = matrix[point_pair][1]
    x1 = matrix[point_pair + 1][0]
    y1 = matrix[point_pair + 1][1]
    draw_line(x0, y0, x1, y1, screen, color)
    point_pair += 2
    

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
  point1 = [x0, y0, z0, 1]
  point2 = [x1, y1, z1, 1]
  matrix.append(point1)
  matrix.append(point2)
  

def add_point( matrix, x, y, z=0 ):
  point = [x, y, z, 1]
  matrix.append(point)


'''DRAW LINE FUNCTIONS'''
# returns the octant number
def octant(x0, y0, x1, y1):
  try:
    m = (float(y1) - y0) / (x1 - x0)
  except: # vertical line
    return 0

  if ((m >= 0) & (m <= 1)):
    return 1
  elif (m > 1):
    return 2
  elif ((m < 0) * (m >= -1)):
    return 8
  elif (m < -1):
    return 7

def draw_line(x0, y0, x1, y1, screen, color):
  if (x0 > x1): # drawing from right to left -> switch points
    xstor = x0
    ystor = y0
    x0 = x1
    y0 = y1
    x1 = xstor
    y1 = ystor

  A = y1 - y0
  B = -1 * (x1 - x0)
  x = x0
  y = y0
  m = octant(x0, y0, x1, y1)

  # vertical line
  if (m == 0):
    while (y <= y1):
      plot (screen, color, x, y)
      y += 1

  # octant 1
  elif (m == 1):
    d = 2 * A + B
    while (x <= x1):
      plot(screen, color, x, y)
      if (d > 0):
        y += 1
        d += 2 * B
      x += 1
      d += 2 * A

  # octant 2
  elif (m == 2):
    d = A + 2 * B
    while (y <= y1):
      plot(screen, color, x, y)
      if (d < 0):
        x += 1
        d += 2 * A
      y += 1
      d += 2 * B

  # octant 8
  elif (m == 8):
    d = 2 * A - B
    while (x <= x1):
      plot(screen, color, x, y)
      if (d < 0):
        y -= 1
        d -= 2 * B
      x += 1
      d += 2 * A

  # octant 7
  elif (m == 7):
    d = A - 2 * B
    while (y >= y1):
      plot(screen, color, x, y)
      if (d > 0):
        x += 1
        d += 2 * A
      y -= 1
      d -= 2 * B
