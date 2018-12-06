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
max_distance = 10000

def output_field(field, max):
  safe = 0
  for row in field:
    for elem in row:
      if elem<max:
        char = '#'
        safe += 1
      else:
        char = '.'
      #print char,
    #print ''

  print "Safe area = " + str(safe)

#Go through entire field, cell by cell
field = []
for y in range(0, max_y+1):
  row = []
  for x in range(0, max_x+1):
    this_man_dist = 0
    for coord in coords:
      coord_man_dist = abs(coord[0]-x)+abs(coord[1]-y)
      this_man_dist += coord_man_dist
    row.append(this_man_dist)
  field.append(row)

output_field(field, max_distance)


