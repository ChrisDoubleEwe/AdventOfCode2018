import re
import time
import os
import sys
from copy import copy, deepcopy


with open("25_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

min_dimension = 10000
max_dimension = -1

points = []

uniq = 0
for line in content:
  uniq += 1
  a = line.split(',')
  point = []
  for ds in a:
    d = int(ds)
    point.append(d)
  point.append(uniq)
  points.append(point)


def get_num_constellations():
  seen_constellations = []
  for point in points:
    if point[4] in seen_constellations:
      dummy = 1
    else:
      seen_constellations.append(point[4])
  return len(seen_constellations)

def check_distance(a, b):
  distance = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) + abs(a[3] - b[3])
  return distance

def merge_constellations(a, b):
  a_cons = a[4]
  b_cons = b[4]
  if a_cons > b_cons:
    for point in points:
      if point[4] == a_cons:
        point[4] = b_cons
  else:
    for point in points:
      if point[4] == b_cons:
        point[4] = a_cons

last_num_constellations = uniq+100
num_constellations = get_num_constellations()
while num_constellations < last_num_constellations:
  last_num_constellations = num_constellations
  for pointa in points:
    for pointb in points:
      if pointa != pointb:
        if check_distance(pointa, pointb) <= 3:
          merge_constellations(pointa, pointb)
  num_constellations = get_num_constellations()

print "Final number of constellations:" 
num_constellations = get_num_constellations()
print num_constellations

