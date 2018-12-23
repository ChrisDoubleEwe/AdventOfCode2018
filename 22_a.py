import re
import time
import os
import sys
from copy import copy, deepcopy

depth=10689
target_x=11
target_y=722
max_x = target_x + 100
max_y = target_y + 100


#depth=510
#target_x=10
#target_y=10

map = []
for y in range(0, max_y+1):
  row = []
  for x in range(0, max_x+1):
    row.append(-1)
  map.append(row)
    

for y in range(0, max_y+1):
  for x in range(0, max_x+1):
    if x == 0 and y == 0:
      geologic = 0
    elif x == target_x and y == target_y:
      geologic = 0
    elif x == 0:
      geologic = y * 48271
    elif y == 0:
      geologic = x * 16807
    else:
      geologic = map[y][x-1] * map[y-1][x]

    erosion = (geologic + depth) % 20183

    map[y][x] = erosion

def display():
  for y in range(0, max_y+1):
    for x in range(0, max_x+1):
      if y == 0 and x == 0:
        sys.stdout.write('M')     
      elif y == target_y and x == target_x:
        sys.stdout.write('T')   
      else:
        if map[y][x] % 3 == 0:
          sys.stdout.write('.')   
        if map[y][x] % 3 == 1:
          sys.stdout.write('=')
        if map[y][x] % 3 == 2:
          sys.stdout.write('|')
    print ''

display()

def score():
  score = 0
  for y in range(0, target_y+1):
    for x in range(0, target_x+1):
      if map[y][x] % 3 == 0:
        score += 0
      if map[y][x] % 3 == 1:
        score += 1
      if map[y][x] % 3 == 2:
        score += 2
  return score 

print score()
