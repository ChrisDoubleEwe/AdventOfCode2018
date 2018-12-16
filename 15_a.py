import re
import sys
from copy import copy, deepcopy

with open("15_a_input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


class Unit:
  def __init__(self, type, x, y):
    self.type = type
    self.x = x
    self.y = y
    self.ap = 3
    self.hp = 200

map = []
units = []
map_x = -1
map_y = -1
for row in content:
  map_y += 1
  map_x = -1
  new_row = []
  for c in row:
    map_x += 1
    if c == 'E':
      new_unit = Unit('E', map_x, map_y)
      units.append(new_unit)
    if c == 'G':
      new_unit = Unit('G', map_x, map_y)
      units.append(new_unit)
    new_row.append(c)
  map.append(new_row)

def show_units(my_units):
  for u in reading_order(my_units):
    attrs = vars(u)
    print u.type + '(' + str(u.hp) + ')'

def show_unit(u):
  attrs = vars(u)
  print ', '.join("%s: %s" % item for item in sorted(attrs.items()))


def show_map(m):
  for y in range(0, map_y+1):
    for x in range(0, map_x+1):
      sys.stdout.write(str(m[y][x]))
    print ''

def in_range(unit):
  for u in units:
    if abs(abs(unit.x - u.x) + abs(unit.y - u.y)) == 1:
      if unit.type != u.type:
        return True
  return False 

def get_targets(unit):
  if unit.type == 'E':
    target_type = 'G'
  else:
    target_type = 'E'

  targets=[]
  for u in units:
    if u.type == target_type:
      targets.append(u)
  return targets

def get_in_range(targets):
  squares = []
  for u in targets:
    if map[u.y][u.x+1] == '.':
      square = []
      square.append(u.x+1)
      square.append(u.y)
      squares.append(square)
    if map[u.y][u.x-1] == '.':
      square = []
      square.append(u.x-1)
      square.append(u.y)
      squares.append(square)
    if map[u.y+1][u.x] == '.':
      square = []
      square.append(u.x)
      square.append(u.y+1)
      squares.append(square)
    if map[u.y-1][u.x] == '.':
      square = []
      square.append(u.x)
      square.append(u.y-1)
      squares.append(square)
  return squares 
    
def get_reachable(unit, coords):
  result = []
  for square in coords:
    my_map = deepcopy(map)
    step = 0
    found_path = True
    my_map[square[1]][square[0]] = 0
    while found_path:
      found_path = False
      last_step = step
      step += 1
      for x in range(0, map_x+1):
        for y in range(0, map_y+1):
          if my_map[y][x] == last_step:
            if my_map[y][x+1] == '.':
              my_map[y][x+1] = step
              found_path = True
            if my_map[y][x-1] == '.':
              my_map[y][x-1] = step
              found_path = True
            if my_map[y+1][x] == '.':
              my_map[y+1][x] = step
              found_path = True
            if my_map[y-1][x] == '.':
              my_map[y-1][x] = step
              found_path = True
    reachable = 0
    distance = 10000
    direction = '-'
    if type(my_map[unit.y-1][unit.x]) == int:  
      reachable = 1
      if my_map[unit.y-1][unit.x] < distance:
        distance = my_map[unit.y-1][unit.x]
        direction = 'up'
    if type(my_map[unit.y][unit.x-1]) == int:
      reachable = 1
      if my_map[unit.y][unit.x-1] < distance:
        distance = my_map[unit.y][unit.x-1]
        direction = 'left'
    if type(my_map[unit.y][unit.x+1]) == int:
      reachable = 1
      if my_map[unit.y][unit.x+1] < distance:
        distance = my_map[unit.y][unit.x+1]
        direction = 'right'
    if type(my_map[unit.y+1][unit.x]) == int:
      reachable = 1
      if my_map[unit.y+1][unit.x] < distance:
        distance = my_map[unit.y+1][unit.x]
        direction = 'down'
    if reachable == 1:
      r = []
      r.append(square)
      r.append(distance)
      r.append(direction)
      result.append(r)

  nearest_result = []
  min_dist = 100000000
  for r in result:
    if r[1] < min_dist:
      min_dist = r[1]
  for r in result:
    if r[1] == min_dist:
      nearest_result.append(r)
  return nearest_result

def reading_order(units):
  result = []
  for y in range(0, map_y+1):
    for x in range(0, map_x+1):
      for u in units:
        if u.x == x and u.y == y:
          result.append(u)
  return result

def get_first_reading_order(coords):
  result = []
  for y in range(0, map_y+1):
    for x in range(0, map_x+1):
      for i in coords:
        if i[0][0] == x and i[0][1] == y:
          return i
  return [[-1, -1], -1, '-']

def move(unit):
  targets = get_targets(unit)
  if len(targets) == 0:
    print "No targets"
    exit()
  moves_in_range = get_in_range(targets)
  nearest = get_reachable(unit, moves_in_range)
  chosen = get_first_reading_order(nearest)
  
  # Clear current pos in map
  map[unit.y][unit.x] = '.'

  # Update position
  if chosen[2] == 'up':
    unit.y += -1
  if chosen[2] == 'down':
    unit.y += 1
  if chosen[2] == 'left':
    unit.x += -1
  if chosen[2] == 'right':
    unit.x += 1

  # Update map
  map[unit.y][unit.x] = unit.type


def hit(target):
  if target.hp <= 3:
    map[target.y][target.x] = '.'
    units.remove(target)
  else:
    target.hp += -3
  return

def attack(unit):
  target_unit = unit
  target_hp = 201
  for target in get_targets(unit):
     if target.x == unit.x and target.y == unit.y-1 and target.hp < target_hp:
       target_unit = target
       target_hp = target.hp
     if target.x == unit.x-1 and target.y == unit.y and target.hp < target_hp:
       target_unit = target
       target_hp = target.hp
     if target.x == unit.x+1 and target.y == unit.y and target.hp < target_hp:
       target_unit = target
       target_hp = target.hp
     if target.x == unit.x and target.y == unit.y+1 and target.hp < target_hp:
       target_unit = target
       target_hp = target.hp
  if target_hp < 201:
    hit(target_unit)
  return
        
def sum_hp():
  total = 0
  for u in units:
    total += u.hp

  print "TOTAL HIT POINTS = ",
  print total

  outcome = full_iter * total
  print "OUTCOME = ",
  print outcome


def check_game_over():
  found_e = 0
  found_g = 0
  for u in units:
    if u.type == 'E':
      found_e = 1
    if u.type == 'G':
      found_g = 1
  if (found_e + found_g) < 2:
    print "GAME OVER!"
    show_map(map)
    show_units(units)
    sum_hp()
    exit()
  return

print "Round: 0"

show_map(map)
show_units(units)
print " "
print " "
print " "
 
iter = 0
full_iter = 0
while True:
  iter += 1


  for unit in reading_order(units):
    check_game_over()
    if unit:
      if not in_range(unit):
        move(unit)
      if in_range(unit):
        attack(unit)

  full_iter = iter
  print "Round: " + str(iter)
  show_map(map)
  show_units(units)
  print " "
  print " "
  print " "
  
