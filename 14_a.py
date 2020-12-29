import re

recipes = []
recipes.append(3)
recipes.append(7)

#recipes.append(3)
#recipes.append(8)
#recipes.append(0)
#recipes.append(6)
#recipes.append(2)
#recipes.append(1)

elves = []
elves.append(0)
elves.append(1)

def elfAdd():
  for i in range(0, len(elves)):
    add = recipes[elves[i]]
    new_pos = (elves[i] + add +1) % len(recipes)
    print "  Elf " + str(i)+ ": Adding " + str(add) + " to " + str(elves[i]) + " to give " + str(new_pos) 
    elves[i] = new_pos
    

def display():
  for i in range(0, len(recipes)):
    if i == elves[0]:
      print "(" + str(recipes[i]) + ") ",
    elif i == elves[1]:
      print "[" + str(recipes[i]) + "] ",
    else:
      print str(recipes[i]) + " ",
  print " "

def score():
  total = ''
  for i in range(max, max+10):
    print i
    print recipes[i]
    total = total + str(recipes[i])
  print "TOTAL = " + total
 
max = 430971

iter = 0
while True:
  print iter
  iter += 1
  if iter > max+20:
    score()
    exit()


  new_recipe = recipes[elves[0]] + recipes[elves[1]]
  new_recipe_str = str(new_recipe)
  for c in new_recipe_str:
    recipes.append(int(c))

  elfAdd()

  #display()
