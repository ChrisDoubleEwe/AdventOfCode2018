import re

with open("12_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

map = []

line_no = 0
first = ''

for line in content:
  if line_no == 0:
    first = line
  if line_no == 1:
    discard = 1
  if line_no > 1:
    map.append(line)
  line_no += 1

state = first.split(' ')[2]  

pad = '.........'
pad_length = len(pad)

state = pad + state + '......................'
print ' 0 :  ' + state

new_map = []
for item in map:
  new_item = []
  s1 = item.split(' ')[0]
  s2 = item.split(' ')[2]
  #s2 = s1[0]+s1[1]+s2+s1[3]+s1[4]
  new_item.append(s1)
  new_item.append(s2)
  new_map.append(new_item)

map = new_map

def do_replace(resul, s, m, r):
  result = ''
  for i in range(0, len(s)):
    if i < 2:
      result += resul[i]
      continue
    if i > len(s)-3:
      result += resul[i]
      continue
    test = s[i-2] + s[i-1] + s[i] + s[i+1] + s[i+2]
    if test == m:
      result += r
    else:
      result += resul[i]
  return result
   

for iter in range(1, 21):
  final_state = state
  for item in map:
    result = do_replace(final_state, state, item[0], item[1])
    #print "Replacing " + item[0] + " with " + item[1]
    #print "   before: " + state
    #result = state.replace(item[0],item[1])
    #result = state
    #starts = [match.start() for match in re.finditer(re.escape(item[0]), state)]
    #for i in starts:
    #  result = result[0:i+2] + item[1] + result[i+3:]
    #print "   after:  " + result 
    # copy differences between state and result to final_state
    #copy = ''
    #for i in range(0, len(final_state)):
    #  result_c = result[i]
    #  state_c = state[i]
    #  final_c = final_state[i]
    #  if result_c == state_c:
    #    copy += final_c
    #  else:
    #    copy += result_c
    final_state = result
  state = final_state
  if iter % 500000000 == 0:
    print iter / 500000000
  #if iter < 10:
  #  print '',
  #print iter,
  #print ": ",
  #print state

total = 0
for i in range(0, len(state)):
  if state[i] == '#':
    total += i - pad_length
print "Total = " + str(total) 
