import re
import time
import os
import sys

with open("17_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

min_x = 10000
min_y = 10000
max_x = 0
max_y = 0
for line in content:
  if line.startswith('x='):
    z=line.split(', ')
    x=z[0].split('=')[1]
    y=z[1].split('=')[1]
    y=y.split('..')[1]
    x = int(x)
    y = int(y)

    if x > max_x:
      max_x = x
    if x < min_x:
      min_x = x
    if y > max_y:
      max_y = y
    if y < min_y:
      min_y = y

  else:
    z=line.split(', ')
    y=z[0].split('=')[1]
    x=z[1].split('=')[1]
    x=x.split('..')[1]
    x = int(x)
    y = int(y)

    if x > max_x:
      max_x = x
    if x < min_x:
      min_x = x
    if y > max_y:
      max_y = y
    if y < min_y:
      min_y = y

print "MIN Y = " + str(min_y)
map = []
for j in range(0, max_y+2):
  row = []
  for i in range(0, max_x+2):
    row.append('.')
  map.append(row)

for line in content:
  if line.startswith('x='):
    z=line.split(', ')
    x=z[0].split('=')[1]
    y=z[1].split('=')[1]
    y1=y.split('..')[0]
    y2=y.split('..')[1]
    x = int(x)
    y1 = int(y1)
    y2 = int(y2)
    for y in range(y1, y2+1):
      map[y][x] = '#'
  else:
    z=line.split(', ')
    y=z[0].split('=')[1]
    x=z[1].split('=')[1]
    x1=x.split('..')[0]
    x2=x.split('..')[1]
    x1 = int(x1)
    x2 = int(x2)
    y = int(y)
    for x in range(x1, x2+1):
      map[y][x] = '#'


def display():
  return 

def xdisplay():
  os.system('clear')
  for j in range(0, max_y+2):
    for i in range(0, max_x+2):
      if i < min_x-1:
        continue
      sys.stdout.write(map[j][i])
    print ""
    map.append(row)
  time.sleep(0.1)  

def can_drop(x, y):
  if map[y+1][x] != '#' and map[y+1][x] != '~':
    return True
  return False

def blocked_on_both_sides(x, y):
  blocked_left = False
  blocked_right = False
  delta = 1
  while blocked_left==False or blocked_right == False:
    if blocked_left == False:
      if can_drop(x-delta, y):
        return False
      else:
        if map[y][x-delta] == '#' or map[y][x-delta] == '~':
          blocked_left = True
    if blocked_right == False:
      if can_drop(x+delta, y):
        return False
      else:
        if map[y][x+delta] == '#' or map[y][x+delta] == '~':
          blocked_right = True
    delta += 1
  if blocked_left and blocked_right:
    return True
  else:
    return False

def fill_tilde(x, y):
  start_x = x
  x = x -1
  while map[y][x] != '#' and map[y][x] != '~':
    map[y][x] = '~'
    x = x -1
  x = start_x 
  while map[y][x] != '#' and map[y][x] != '~':
    map[y][x] = '~'
    x = x + 1
  display()


def fill_pipe(x, y):
  start_x = x
  x = x -1
  while map[y][x] != '#' and map[y][x] != '~' and can_drop(x, y) == False:
    map[y][x] = '|'
    x = x -1
  if can_drop(x, y):
    map[y][x] = '|'
    drip(x, y)
  x = start_x
  while map[y][x] != '#' and map[y][x] != '~' and can_drop(x, y) == False:
    map[y][x] = '|'
    x = x + 1
  if can_drop(x, y):
    map[y][x] = '|'
    drip(x, y)
  display()


def drip(x, y):
  blocked = 0
  while y < max_y and blocked==0: 
    if can_drop(x,y):
      y = y + 1
      map[y][x] = '|'
      display()
    else:
      if blocked_on_both_sides(x, y):
        fill_tilde(x, y)
        blocked = 1
      else:
        fill_pipe(x, y)
      blocked = 1
  return 
      
old_total = -1

def count():
  total = 0
  for y in range(0, max_y+2):
    for x in range(0, max_x+2):
      if map[y][x] == '|':
        total+=1
      if map[y][x] == '~':
        total+=1
  return total

total = count()
while total != old_total:
  print total
  old_total = total
  drip(500, 0)
  total = count()



total = count()
print total

total = 0
for y in range(0, max_y+2):
  for x in range(0, max_x+2):
    if map[y][x] == '~':
      total+=1
print "PART 2"
print total
