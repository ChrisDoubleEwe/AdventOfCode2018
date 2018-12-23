import re
import time
import os
import sys
from copy import copy, deepcopy

#depth=10689
#target_x=11
#target_y=722
max_x = target_x + 15
max_y = target_y + 15


depth=510
target_x=10
target_y=10
max_x = target_x + 15
max_y = target_y + 15

math_map = []
map = []
for y in range(0, max_y+1):
  row = []
  new_row = []
  for x in range(0, max_x+1):
    row.append(-1)
    new_row.append('-')
  math_map.append(row)
  map.append(new_row)
    

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
      geologic = math_map[y][x-1] * math_map[y-1][x]

    erosion = (geologic + depth) % 20183

    math_map[y][x] = erosion

def display():
  for y in range(0, max_y+1):
    for x in range(0, max_x+1):
      if y == 0 and x == 0:
        sys.stdout.write('M')     
        map[y][x] = 'M'
      elif y == target_y and x == target_x:
        sys.stdout.write('T')   
        map[y][x] = 'T'

      else:
        if math_map[y][x] % 3 == 0:
          sys.stdout.write('.')   
          map[y][x] = '.'
        if math_map[y][x] % 3 == 1:
          sys.stdout.write('=')
          map[y][x] = '='
        if math_map[y][x] % 3 == 2:
          sys.stdout.write('|')
          map[y][x] = '|'
    print ''

display()

def score():
  score = 0
  for y in range(0, target_y+1):
    for x in range(0, target_x+1):
      if math_map[y][x] % 3 == 0:
        score += 0
      if math_map[y][x] % 3 == 1:
        score += 1
      if math_map[y][x] % 3 == 2:
        score += 2
  return score 

print score()

routes = []
this_route = []
my_x = 0
my_y = 0

def moves(my_x, my_y, routes, this_route):
  step = []
  step.append(my_x)
  step.append(my_y)
  # If we've been here before, stop (can't be the shortest route)
  if step in this_route:
    return
  
  this_route.append(step)

  # If we're at the target, we're done
  if map[my_y][my_x] == 'T':
    routes.append(this_route)
    return

  # If this is the first move, we've got a torch equipped and can go to rocky or narrow regions E or S
  if map[my_y][my_x] == 'M':
    if map[my_y+1][my_x] == '.' or map[my_y+1][my_x] == '|':
      move(my_y+1, my_x, routes, this_route,)
    if map[my_y][my_x+1] == '.' or map[my_y][my_x+1] == '|':
      move(my_y, my_x+1, routes, this_route) 
    return

  # If we're in rock, 
  if map[my_y][my_x] == 'M'
#From starting position
#Can I move N?
#Add to potential route
#Am I at target?

moves(my_x, my_y, routes, this_route)

