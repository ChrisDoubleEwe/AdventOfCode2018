import re
import time
import os
import sys
from copy import copy, deepcopy


with open("20_a_test.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

content = str(content[0])
content = list(content)

print content 

all_possible_paths = []

# ^ENWWW(NEEE|SSE(EE|N))$

def process_paths(remainder, start):
   print "\n\nPROCESS PATHS"
   print remainder
   print start

   while remainder[0] != '$' and remainder[0] != '(':
     c = remainder.pop(0)
     print "Adding " + str(c) + " to START "
     start += c
     print start
   c = remainder.pop(0)
   if c == '$':
     start.append('$')
     print "Possible path = "
     all_possible_paths.append(start)
     print start
     return
   if c == '(':
     options = []
     brackets = 0
     this_path = []
     mybreak = 0
     while mybreak == 0:
       c = remainder.pop(0)
       if c == '(':
         brackets += 1
         this_path.append(c)
       if c == "|":
         if brackets == 0:
           options.append(this_path)
           this_path = []
         else:
           this_path.append(c)
       if c == ')':
         if brackets > 0:
           brackets += -1
           this_path.append(c)
         else:
           options.append(this_path)
           this_path = []
           mybreak = 1
       if c in 'NSEW':
         this_path.append(c)
   print "   OPTIONS"
   print options
   my_start = deepcopy(start)
   for opt in options:
     this_start = deepcopy(start)
     print "---------Processing Option"
     print opt
     print this_start
     print "--------------------------"
     this_path = opt
     this_path.extend(remainder)
     process_paths(this_path, this_start)

     
process_paths(content, [])
print "\n\n\nALL POSSIBLE PATHS"
print all_possible_paths
