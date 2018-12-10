import re

with open("10_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

data = []

for line in content:
  x = line.split('<')
  pos = x[1].split('>')[0]
  vel = x[2].split('>')[0]
  pos_x = pos.split(', ')[0].strip()
  pos_y = pos.split(', ')[1].strip()
  pos = []
  pos.append(int(pos_x))
  pos.append(int(pos_y))
  vel_x = vel.split(', ')[0].strip()
  vel_y = vel.split(', ')[1].strip()
  vel = []
  vel.append(int(vel_x))
  vel.append(int(vel_y))

  row = []
  row.append(pos)
  row.append(vel)
  data.append(row)

def width():
  min_x = 10000000
  max_x = -10000000
  for x in data:
    if x[0][0] < min_x:
      min_y = x[0][0]
    if x[0][0] > max_x:
      max_y = x[0][0]
  diff = max_y - min_y
  return diff

def max_x():
  max_x = 0
  for x in data:
    print x[0][0]
    if x[0][0] > max_x:
      max_x = x[0][0]
  print max_x
  return max_x

def height():
  min_y = 10000000
  max_y = -10000000
  for x in data:
    if x[0][1] < min_y:
      min_y = x[0][1]
    if x[0][1] > max_y:
      max_y = x[0][1]
  diff = max_y - min_y
  return diff

def max_y():
  max_y = 0
  for x in data:
    if x[0][1] > max_y:
      max_y = x[0][1]
  return max_y

def finish():
  h = max_y()+5
  w = max_x()+5
  side = 0
  if h > w:
    side = h
  else:
    side = w

  print "Creating display width=" + str(w) + " height = " + str(h)
  display = []
  for i in range(0, side):
    d_row = []
    for n in range(0, side):
      d_row.append('.')
    display.append(d_row)

  print display

  for x in data:
    pos = x[0]
    pos_x = pos[0]
    pos_y = pos[1]
    print "  Plot pixel " + str(pos_x) + ", " + str(pos_y)
    display[pos_x][pos_y] = '*'

  print "rendering..."
  for x in display:
    line = ''.join(x)
    line = line[60:]
    line = line[:-30]
    print line

min_height = 10000000
rounds = 0
last_data = []
while True:
  current_height = height()
  print "Round " + str(rounds) + " ; height = " + str(current_height) + " ; min_height = " + str(min_height)
  rounds += 1
 
  if current_height > min_height:
    data = last_data
    #finish()
    exit()
  else:
    min_height = current_height 

  last_data = data
  new_data = []
  for x in data:
    pos = x[0]
    vel = x[1]
    pos_x = pos[0]
    pos_y = pos[1]
    vel_x = vel[0]
    vel_y = vel[1]
    pos_x = pos_x + vel_x
    pos_y = pos_y + vel_y
    pos = []
    pos.append(pos_x)
    pos.append(pos_y)
    row = []
    row.append(pos)
    row.append(vel)
    new_data.append(row)

  data = new_data
    
