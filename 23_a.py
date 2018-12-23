import re
import time
import os
import sys
from copy import copy, deepcopy


with open("23_a_input.txt") as f:
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

  print "x=" + str(x) + " ; y=" + str(y) + " ; z=" + str(z) + " [r=" + str(r) + "]"
  this_bot.append(int(x))
  this_bot.append(int(y))
  this_bot.append(int(z))
  this_bot.append(int(r))
  bots.append(this_bot)

max_rad = 0
max_bot= []
for bot in bots:
  if bot[3] > max_rad:
    max_rad = bot[3]
    max_bot = bot

print max_rad
print max_bot

def manhattan(max_bot, bot):
  x_dist = abs(max_bot[0] - bot[0])
  y_dist = abs(max_bot[1] - bot[1])
  z_dist = abs(max_bot[2] - bot[2])
  return x_dist + y_dist + z_dist
  
count = 0
for bot in bots:
  dist = manhattan(max_bot, bot)
  if manhattan(max_bot, bot) <= max_bot[3]:
    print bot
    print "IN RANGE: " + str(dist) + " <= " + str(max_bot[3])
    count += 1

  else:
    print bot
    print "not in range: " + str(dist) + " > " + str(max_bot[3])


print count
