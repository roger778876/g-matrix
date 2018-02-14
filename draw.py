from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    pass

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    pass

def add_point( matrix, x, y, z=0 ):
    pass


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
