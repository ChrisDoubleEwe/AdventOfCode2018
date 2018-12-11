import re

cells = []

serial = 4151

# Initialize

for y in range(1, 300+2):
  row = []
  for x in range(1, 300+2):
    row.append(0)
  cells.append(row)

def power(x,y):
  rack = x + 10
  pow = rack * y
  pow += serial
  pow = pow * rack
  pow_str = '0000' + str(pow)
  hundreds = pow_str[len(pow_str)-3]
  hun = int(hundreds)
  pow = hun -5
  return pow

def get_three_square_power(x, y, size):
  if x + size > 300:
    return 0
  if y + size > 300:
    return 0

  pow = 0
  for i in range(0,size):
    pow += sum(cells[x+i][y:y+size])

  return pow







# Set powers
for x in range(1, 300+1):
  for y in range(1, 300+1):
    cells[x][y] = power(x, y)    



max_x = 0
max_y = 0
max_size = 0
max_pow = -100

for size in range(0,300):
 print "Doing size=" + str(size)
 for x in range(230, 232):
  for y in range(63, 67):
    pow = get_three_square_power(x, y, size)
    if pow > max_pow:
      max_pow = pow
      max_x = x
      max_y = y
      max_size = size

print "Max cell power is " + str(max_pow) + " at " + str(max_x) + "," + str(max_y) + "," + str(max_size)

