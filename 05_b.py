import re

with open("05_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
s_list = (str(content).split('\''))
s = s_list[1]

def decompose(s):
  length = len(s)
  last_length = length + 1

  while length < last_length:
    for x in 'abcdefghijklmnopqrstuvwxyz':
      pair1=x+x.upper()
      pair2=x.upper()+x
      s = s.replace(pair1, "")
      s = s.replace(pair2, "")
    last_length = length
    length = len(s)
  return length

min_length = len(s) + 1
min_letter = ''
for x in 'abcdefghijklmnopqrstuvwxyz': 
  new_s = s
  new_s = new_s.replace(x, "")
  new_s = new_s.replace(x.upper(), "")
  length = decompose(new_s)
  if length < min_length:
    min_length = length
    min_letter = x

print "Min length = " + str(min_length) + " by removing letter: " + min_letter
