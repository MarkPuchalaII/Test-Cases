# This is a quick example of a list comprehension in python

if __name__ == '__main__':
  x = int (input())               # This is one of the simplest versions
  p = [i+1 for i in range(x)]     # It simply prints a list, 1 through x.
  print(p)

if __name__ == '__main__':
  x = int (input())
  y = int (input())
  z = int (input())
  n = int (input())
  p = [ [ i, j, k] for i in range( x + 1 )
                   for j in range( y + 1 )
                   for k in range( z + 1 )
                      if ( ( i + 5 + k ) != n )]
  print(p)
# [[0, 5, 0], [0, 5, 1], [0, 5, 2], [1, 5, 0], [1, 5, 1], [1, 5, 2], [2, 5, 0], [2, 5, 1], [2, 5, 2]]
# Learning List Comprehensions in Python
