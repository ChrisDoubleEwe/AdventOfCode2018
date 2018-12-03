import re
import copy

with open("02_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
list1 = [x.strip() for x in content] 
list2 = copy.copy(list1)

for x in list1:
  for y in list2:
    differs = 0
    a = len(x)
    final = ''
    for i in range(0, a):
      char1 = x[i]
      char2 = y[i]
      if char1 != char2:
        differs = differs + 1
      else:
        final = final + char1
    #print x + "   " + y + "  ...differs by " + str(differs)

    if differs == 1:
      print x + "   " + y + "        " + final
      exit()
