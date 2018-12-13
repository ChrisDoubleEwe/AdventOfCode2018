import re

with open("13_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line

map = []
carts = []

y = -1
for row in content:
  y += 1
  new_row = []
  x = -1
  for c in str(row):
    x += 1
    if c == '^':
      cart = []
      cart.append(c)
      cart.append(x)
      cart.append(y)
      cart.append(0)
      carts.append(cart)
      c = "|"
    if c == 'v':
      cart = []
      cart.append(c)
      cart.append(x)
      cart.append(y)
      cart.append(0)
      carts.append(cart)
      c = "|"
    if c == '>':
      cart = []
      cart.append(c)
      cart.append(x)
      cart.append(y)
      cart.append(0)
      carts.append(cart)
      c = "-"
    if c == '<':
      cart = []
      cart.append(c)
      cart.append(x)
      cart.append(y)
      cart.append(0)
      carts.append(cart)
      c = "-"
    new_row.append(c)
  map.append(new_row)
print carts

#for r in map:
  #print r
#print carts

def move_carts():
  for cart in carts:
    dir = cart[0]
    cart_x = cart[1]
    cart_y = cart[2]
    turn = cart[3]

    #print " x= " + str(cart_x) + " y= " + str(cart_y)
    track = map[cart_y][cart_x]
    if track == '-':
      if dir == '<':
        cart_x = cart_x - 1
      elif dir == '>':
        cart_x = cart_x + 1
    if track == '|':
      if dir == '^':
        cart_y = cart_y - 1
      elif dir == 'v':
        cart_y = cart_y + 1
    if track == '/':
      if dir == '^':
        cart_x = cart_x - 1
        dir = '>'
      elif dir == 'v':
        cart_x = cart_x - 1
        dir = '<'
      elif dir == '>':
        cart_y = cart_y - 1
        dir = '^'
      elif dir == '<':
        cart_y = cart_y + 1
        dir = 'v'
    if track == '\\':
      if dir == '<':
        cart_y = cart_y - 1
        dir = '^'
      elif dir == '>':
        cart_y = cart_y + 1
        dir = 'v'
      elif dir == '^':
        cart_x = cart_x - 1
        dir = '<'
      elif dir == 'v':
        cart_x = cart_x + 1
        dir = '>'
    if track == "+":
      new_dir = ''
      if turn == 0: # LEFT
        if dir == 'v':
          cart_x = cart_x + 1
          new_dir = '>'
        if dir == '^':
          cart_x = cart_x - 1
          new_dir = '<'
        if dir == '<':
          cart_y = cart_y + 1
          new_dir = 'v'
        if dir == '>':
          cart_y = cart_y - 1
          new_dir = '^'
      if turn == 1: # STRAIGHT
        if dir == 'v':
          cart_y = cart_y + 1
        if dir == '^':
          cart_y = cart_y - 1
        if dir == '<':
          cart_x = cart_x - 1
        if dir == '>':
          cart_y = cart_y + 1
      if turn == 2: # RIGHT
        if dir == 'v':
          cart_x = cart_x - 1
          new_dir = '<'
        if dir == '^':
          cart_x = cart_x + 1
          new_dir = '>'
        if dir == '<':
          cart_y = cart_y - 1
          new_dir = '^'
        if dir == '>':
          cart_y = cart_y + 1
          new_dir = 'v'
      dir = new_dir
      turn += 1
      if turn > 2:
        turn = 0
    cart[0] = dir
    cart[1] = cart_x
    cart[2] = cart_y
    cart[3] = turn

def check_crash():
  for i in range(0, len(carts)):
    for j in range(0, len(carts)):
      cart1 = carts[i]
      cart2 = carts[j]
      if cart1[1] == cart2[1]:
        if cart1[2] == cart2[2]:
          if i != j:
            print "CRASH!   " + str(cart1[1]) + "," + str(cart2[2])
            exit()

iter = 0
while True:
  iter += 1
  #print "Move " + str(iter)
  move_carts()
  #print carts
  check_crash()
