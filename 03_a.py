import re

with open("03_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

squares=[]
for x in content:
  print x
  x1=(x.split(' @ ')) 
  id=x1[0]
  x2=(x1[1].split(': '))
  x3=(x2[0].split(','))
  left=x3[0]
  top=x3[1]
  x4=(x2[1].split('x'))
  width=x4[0]
  height=x4[1]

  square = []
  square.append(id)
  square.append(int(left))
  square.append(int(top))
  square.append(int(width))
  square.append(int(height))
  print square
  squares.append(square)

# Work out limits of fabric
max_width = 0
max_height = 0
for square in squares:
  w = square[1]+square[3]
  h = square[2]+square[4]

  if w > max_width:
    max_width = w
  if h > max_height:
    max_height = h

max_width = max_width+1
max_height = max_height + 1
if max_height > max_width:
  max_width=max_height
else:
  max_height = max_width

print max_width
print max_height

fabric=[]
for x in range(0, max_width):
  fabric_row=[]
  for y in range(0, max_height):
    fabric_row.append('.')
  fabric.append(fabric_row)

#print fabric

for square in squares:
  for x in range(0, square[3]):
    for y in range(0, square[4]):
      current = fabric[square[1]+x][square[2]+y]
      if current == '.':
        fabric[square[1]+x][square[2]+y] = square[0]
      else:
        fabric[square[1]+x][square[2]+y] = 'X'
#print fabric

overlaps = 0
for x in range(0, max_width):
  for y in range(0, max_height):
    if fabric[x][y] == 'X':
      overlaps = overlaps + 1

print str(overlaps)

for square in squares:
  intact = 1
  for x in range(0, square[3]):
    for y in range(0, square[4]):
      current = fabric[square[1]+x][square[2]+y]
      if current == 'X':
        intact = 0
  if intact == 1:
    print 'Square ' + square[0] + ' is intact'
