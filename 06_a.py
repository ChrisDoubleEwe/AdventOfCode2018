import re

with open("06_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# Parse input string into pairs of x-y integer coordinates
coords = []
for a in content:
  b = a.split(', ')
  x = int(b[0])
  y = int(b[1])
  coord = []
  coord.append(x)
  coord.append(y)
  coords.append(coord)

# Find max X and Y to discover the bounds of the area
max_x = 0
max_y = 0

for coord in coords:
  if coord[0] > max_x:
    max_x = coord[0]
  if coord[1] > max_y:
    max_y = coord[1]

max_manhatten = max_x + max_y + 10


# Initialize field
empty_cell= []
empty_cell.append(0)
empty_cell.append(max_manhatten)
empty_row = []
for i in range(0, max_y+10):
  empty_row.append(empty_cell)
empty_field = []
for i in range(0, max_x+10):
  empty_field.append(empty_row)

def output_field(field):
  for row in field:
    for elem in row:
      char = '-'
      if elem[0]==0:
        char = '.'
      else:
        s = '.abcdefghijklmnopqrs'
        char = s[elem[0]]
        if elem[1]==0:
          char=char.upper()
      print char,
    print ''

field = empty_field

# Go through pairs of coordinates 1 by 1
coord_number = 0

for coord in coords:
  new_field = []
  coord_number += 1
  for y in range(0, max_y+1):
    new_row = []
    for x in range(0, max_x+1):
      new_cell = []
      this_man_dist = abs(coord[0]-x)+abs(coord[1]-y)

      this_pair = field[y][x]
      if this_man_dist < this_pair[1]:
        new_cell.append(coord_number)
        new_cell.append(this_man_dist)
      elif this_man_dist == this_pair[1]:
        new_cell.append(0)
        new_cell.append(this_man_dist)
      else:
        new_cell = this_pair
      new_row.append(new_cell)
    new_field.append(new_row)
  field = new_field


# Work out largest area
# We can ignore all the groups adjacent to sides (because they are infinite)

ignore_list = []
max_id = 0
for y in range(0, max_y+1):
  for x in range(0, max_x+1):
    this_cell = field[y][x]
    this_id = this_cell[0]
    if this_id > max_id:
      max_id = this_id
    if y == 0:
      ignore_list.append(this_id)
    if y == max_y:
      ignore_list.append(this_id)
    if x == 0:
      ignore_list.append(this_id)
    if x == max_x:
      ignore_list.append(this_id)

ignore_list = list(set(ignore_list)) 

max_area = 0
dummy = 0
for id in range(1, max_id+1):
  this_area = 0
  for y in range(0, max_y+1):
    for x in range(0, max_x+1):
      this_cell = field[y][x]
      this_id = this_cell[0]
      if this_id in ignore_list:
        dummy += 1
      else:
        if this_id == id:
          this_area += 1
  if this_area > max_area:
    max_area = this_area

print "Max area = " + str(max_area)
 
