import math


def print_matrix( matrix ): # as it turns out, I made my own \t
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

# changes matrix to identity matrix
def ident( matrix ):
  del matrix[:]
  i = 0
  for point in range(4):
    matrix.append([])
    for xyz in range(4):
      if (xyz == i):
        matrix[point].append(1)
      else:
        matrix[point].append(0)
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
