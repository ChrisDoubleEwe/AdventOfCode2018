import re

cells = []

serial = 7989

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

def get_three_square_power(x, y):
  #for i in range(0,3):
  #  for j in range(0, 3):
  #    print cells[j][i],
  #  print ''

  pow = cells[x][y]
  pow += cells[x][y+1]
  pow += cells[x][y+2]
  pow += cells[x+1][y]
  pow += cells[x+1][y+1]
  pow += cells[x+1][y+2]
  pow += cells[x+2][y]
  pow += cells[x+2][y+1]
  pow += cells[x+2][y+2]
  return pow







# Set powers
for x in range(1, 300+1):
  for y in range(1, 300+1):
    cells[x][y] = power(x, y)    



max_x = 0
max_y = 0
max_pow = -100

for x in range(1, 297+1):
  for y in range(1, 297+1):
    pow = get_three_square_power(x, y)
    if pow > max_pow:
      print "New max! pow = " + str(pow) + " ; max_pow=" + str(max_pow) + " ; x=" + str(x) + " y=" + str(y)
      max_pow = pow
      max_x = x
      max_y = y

print "Max 3x3 cell power is " + str(max_pow) + " at " + str(max_x) + "," + str(max_y)

