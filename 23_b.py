import re
import time
import os
import sys
from copy import copy, deepcopy


with open("23_b_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

bots = []

for line in content:
  this_bot = []
  a = line.split('>')[0]
  b = line.split('>')[0]
  d = line.split('>')[1]
  r = d.split('=')[1]
  c = a.split('<')[1]
  x = c.split(',')[0]
  y = c.split(',')[1]
  z = c.split(',')[2]

  this_bot.append(int(x))
  this_bot.append(int(y))
  this_bot.append(int(z))
  this_bot.append(int(r))
  bots.append(this_bot)

max_rad = 0
max_bot= []
min_x = 1000000
min_y = 1000000
min_z = 1000000
max_x=0
max_y=0
max_z=0
for bot in bots:
  if bot[3] > max_rad:
    max_rad = bot[3]
    max_bot = bot
  if bot[0] > max_x:
    max_x = bot[0]
  if bot[0] < min_x:
    min_x = bot[0]
  if bot[1] > max_y:
    max_y = bot[1]
  if bot[1] < min_y:
    min_y = bot[1]
  if bot[2] > max_z:
    max_z = bot[2]
  if bot[2] < min_z:
    min_z = bot[2]
print " RANGE: x = (" + str(min_x) + " to " + str(max_x) + ") ; y = " + str(min_y) + " to " + str(max_y) + " ; z = (" +  str(min_z) + " to " + str(max_z) + ")"

def manhattan(max_bot, bot):
  x_dist = abs(max_bot[0] - bot[0])
  y_dist = abs(max_bot[1] - bot[1])
  z_dist = abs(max_bot[2] - bot[2])
  return x_dist + y_dist + z_dist
  
count = 0
for bot in bots:
  dist = manhattan(max_bot, bot)
  if manhattan(max_bot, bot) <= max_bot[3]:
    count += 1


max_count = 0
rem_x = 0
rem_y = 0
rem_z = 0 

for x in range(min_x, max_x):
  print x
  for y in range(min_y, max_y):
    for z in range(min_z, max_z):
      count = 0
      for bot in bots:
        my_pos = []
        my_pos.append(x)
        my_pos.append(y)
        my_pos.append(z)

        if manhattan(bot, my_pos) <= bot[3]:
          print "in range!"
          count += 1
      if count > max_count:
        max_count = count
        rem_x = x
        rem_y = y
        rem_z = z

print max_count
print rem_x
print rem_y
print rem_z


#-----


