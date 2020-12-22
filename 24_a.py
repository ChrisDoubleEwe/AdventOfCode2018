import re
import time
import os
import sys
from copy import copy, deepcopy


with open("24_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

immune = []
infect = []
idx = 1
immune_switch = -1
for line in content:
  print line
  if line == '':
    continue
  if line == 'Immune System:':
    immune_switch = 1
    idx = 1
    continue
  if line == 'Infection:':
    immune_switch = 0
    idx = 1
    continue
  unit = []
  num = line.split(' ')[0]
  hp = line.split(' ')[4]
  if '(' in line:
    print line.split('(')[1]
    w1 = line.split('(')[1].split(')')[0]
    if ';' in w1:
      imm=w1.split('; ')[0]
      weak=w1.split('; ')[1]
    else:
      imm = ''
      weak = w1
    weak = weak.replace('weak to ', '')
    weak = weak.split(', ')
    imm = imm.replace('immune to ', '')
    imm = imm.split(', ')
  else:
    weak = ''
    imm = ''
  if '(' in line:
    damage = line.split(')')[1].split(' ')[6]
    damage_type = line.split(')')[1].split(' ')[7]
    initiative = line.split(')')[1].split(' ')[11]
  else:
    damage = line.split(' ')[12]
    damage_type = line.split(' ')[13]
    initiative = line.split(' ')[17]


  unit.append(int(num))
  unit.append(int(hp))
  unit.append(imm)
  unit.append(weak)
  unit.append(int(damage))
  unit.append(damage_type)
  unit.append(int(initiative))
  unit.append(int(idx))
  idx += 1


  if immune_switch == 1:
    immune.append(unit)
  else:
    infect.append(unit)


def get_unit_by_index(type, idx):
  if type == 'infect':
    for u in infect:
      if u[7] == idx:
        return u
  else:
    for u in immune:
      if u[7] == idx:
        return u

def order_my_pairs(list_of_pairs):
  print "Unordered..."
  print list_of_pairs

  new_list = []
  if len(list_of_pairs) == 1:
    new_list = deepcopy(list_of_pairs)
    return new_list
  while len(list_of_pairs) > 0:
    old_new_list = deepcopy(new_list)
    high_init = -1
    high_pair = []
    for pair in list_of_pairs:
      if pair[1] > -1 and pair[3] > -1:
        this_init = get_unit_by_index(pair[0], pair[1])[6]
        if this_init > high_init:
          high_init = this_init
          high_pair = pair
    if high_pair:
      print "Dealing with highest pair..."
      print high_pair
      print list_of_pairs
      new_list.append(high_pair)
      list_of_pairs.remove(high_pair) 
    if old_new_list == new_list:
      return new_list
  print "Ordered..."
  print new_list
  return new_list


def calc_damage(a, d):
  dam = a[0] * a[4]
  if a[5] in d[2]:
    dam = 0
  if a[5] in d[3]:
    dam = dam * 2
  return dam

def unit_compare(x, y):
  x_eff = x[0] * x[4]
  y_eff = y[0] * y[4]
  return x_eff - y_eff




round = 0

while True:
  round += 1
  # Process in order of effective
  seen = []
  done = 0
  all = len(infect) + len(immune)
  remaining_infect = deepcopy(infect)
  remaining_immune = deepcopy(immune)

  attack_pairs = []

  print "===================================="
  print "Round " + str(round)
  print "Immune System:"
  for u in immune:
    print "Group " + str(u[7]) + " contains " + str(u[0]) + " units"

  print "Infection System:"
  for u in infect:
    print "Group " + str(u[7]) + " contains " + str(u[0]) + " units"
 
  while done < all:
    highest_eff = 0
    highest_init = 0
    highest_type = ''
  
    for attack_unit in infect:
      if attack_unit in seen:
        continue
      if attack_unit[0] * attack_unit[4] >= highest_eff:
        if attack_unit[0] * attack_unit[4] == highest_eff and attack_unit[6] < highest_init:
          continue
        highest_eff = attack_unit[0] * attack_unit[4]
        highest_init = attack_unit[6]
        highest_unit = attack_unit
        highest_type = 'infect'
    for attack_unit in immune:
      if attack_unit in seen:
        continue
      if attack_unit[0] * attack_unit[4] >= highest_eff:
        if attack_unit[0] * attack_unit[4] == highest_eff and attack_unit[6] < highest_init:
          continue
        highest_init = attack_unit[6]
        highest_eff = attack_unit[0] * attack_unit[4]
        highest_unit = attack_unit
        highest_type = 'immune'
  
    seen.append(highest_unit)
    done += 1
    # Choose target for this group

    selected_target = []
    if highest_type == 'infect':
      high_dam = -1
      # Get highest damage
      for target in remaining_immune:
        dam = calc_damage(highest_unit, target)
        if dam > high_dam:
          high_dam = dam
      # Get highest effective power
      high_eff = 0
      for target in remaining_immune:
        dam = calc_damage(highest_unit, target)
        if dam == high_dam:
          if target[0] * target[4] > high_eff:
            high_eff = target[0] * target[4]
      # Get high initiative
      high_init = 0
      for target in remaining_immune:
        dam = calc_damage(highest_unit, target)
        if dam == high_dam and ((target[0] * target[4]) == high_eff):
          if target[3] > high_init:
            high_init = target[3]
            selected_target = target
      pair = []
      pair.append('infect')
      pair.append(highest_unit[7])
      pair.append('immune')
      if selected_target:
        pair.append(selected_target[7])
      else:
        pair.append(-1)
      pair.append(high_dam)

      attack_pairs.append(pair)
  
  
      if len(selected_target) > 0:
        remaining_immune.remove(selected_target)


    if highest_type == 'immune':
      high_dam = -1
      # Get highest damage
      for target in remaining_infect:
        dam = calc_damage(highest_unit, target)
        if dam > high_dam:
          high_dam = dam
      # Get highest effective power
      high_eff = 0
      for target in remaining_infect:
        dam = calc_damage(highest_unit, target)
        if dam == high_dam:
          if target[0] * target[4] > high_eff:
            high_eff = target[0] * target[4]
      # Get high initiative
      high_init = 0
      for target in remaining_infect:
        dam = calc_damage(highest_unit, target)
        if dam == high_dam and ((target[0] * target[4]) == high_eff):
          if target[3] > high_init:
            high_init = target[3]
            selected_target = target
      if len(selected_target) > 0:
        remaining_infect.remove(selected_target)
      pair = []
      pair.append('immune')
      pair.append(highest_unit[7])
      pair.append('infect')
      if selected_target:
        pair.append(selected_target[7])
      else:
        pair.append(-1)
      pair.append(high_dam)
      attack_pairs.append(pair)
  
  # ATTACK PHASE
  print "ATTACK PHASE...."
  ordered_pairs = []
  ordered_pairs = order_my_pairs(attack_pairs)
  
  # get 
  for pair in ordered_pairs:
    attack_pair = get_unit_by_index(pair[0], pair[1])
    defend_pair = get_unit_by_index(pair[2], pair[3])
    damage = calc_damage(attack_pair, defend_pair)
    print pair
    #damage = pair[4]
    print "Calc:"
    print damage
    print defend_pair[1]
    kill_unitsf = damage / defend_pair[1]
    print kill_unitsf
    kill_units = int (damage / defend_pair[1])
    
    defend_pair[0] = defend_pair[0] - kill_units 
    print str(pair[0]) + " group " + str(pair[1]) + " attacks defending group " + str(pair[3]) + ", killing " + str(kill_units) + "units  -- or float " + str(kill_unitsf) + " (damage = " + str(damage) + ")"
  
  
 
  for unit in immune:
    if unit[0] < 1:
      immune.remove(unit)
  
  for unit in infect:
    if unit[0] < 1:
      infect.remove(unit) 
  
  if len(immune) <= 0:
    print "INFECT WIN"
    total = 0
    print infect
    for u in infect:
      total+= u[0]
      print u[0]
    print "TOTAL"
    print total
    exit()
  if len(infect) <= 0:
    print "IMMUNE WIN"
    total = 0
    for u in immune:
      total+= u[0]
    print total 
    exit()
