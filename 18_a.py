import re
import time
import os
import sys
from copy import copy, deepcopy


with open("18_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

map = []
for line in content:
  row = []
  for c in line:
    row.append(c)
  map.append(row)

max_x = len(row)
max_y = len(map)

def display():
  for y in range(0, max_y):
    for x in range(0, max_x):
      sys.stdout.write(map[y][x])
    print ''

def adj_trees(z, x, y):
  trees = 0
  #print "Checking trees: " + str(x) + " , " + str(y)
  for i in range (y-1, y+2):
    for j in range (x-1, x+2):
      if i >= 0 and i < max_y:
        if j >= 0 and j < max_x:
          if i != y or j != x:
            #print "  Checking square: " + str(j) + " , " + str(i)
            if z[i][j] == '|':
              trees += 1
  #print trees
  return trees

def adj_lumber(z, x, y):
  lumber = 0
  #print "Checking lumber: " + str(x) + " , " + str(y)
  for i in range (y-1, y+2):
    for j in range (x-1, x+2):
      if i >= 0 and i < max_y:
        if j >= 0 and j < max_x:
          if i != y or j != x:
            #print "  Checking square: " + str(j) + " , " + str(i)
            if z[i][j] == '#':
              lumber += 1
  #print lumber
  return lumber

def do_turn(map):
  old_map = deepcopy(map)
  for y in range(0, max_y):
    for x in range(0, max_x):
      if old_map[y][x] == '.' and adj_trees(old_map, x, y) >= 3:
        map[y][x] = '|'
      if old_map[y][x] == '|' and adj_lumber(old_map, x, y) >= 3:
        map[y][x] = '#'
      if old_map[y][x] == '#':
        if  adj_lumber(old_map, x, y) >= 1 and adj_trees(old_map, x, y) >= 1:
          remain = 1
        else:
          map[y][x] = '.'
  return map

iter = 0
while iter < 10:
  iter += 1
  map = do_turn(map)

def count(z, s):
  result = 0
  for y in range(0, max_y):
    for x in range(0, max_x):
      if z[y][x] == s:
        result += 1
  return result

trees = count(map, '|')
lumber = count(map, '#')

total = trees * lumber
print "Part One: ", 
print total
