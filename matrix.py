import math


def print_matrix( matrix ):
  output = ""
  for xyz in range(0, 4):
    output += "|  "
    for point in matrix: # beautifies print output to have even columns
      max_len = len(str(max(point)))
      num = str(point[xyz])
      while (len(num) < max_len):
        num = " " + num
      output += num + "  "
    output += "|\n"
  print output

# creates identity matrix
def ident( matrix ):
  i = 0
  for point in matrix:
    for xyz in range(0, 4):
      if (xyz == i):
        point[xyz] = 1
      else:
        point[xyz] = 0
    i += 1

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
