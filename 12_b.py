import re

with open("12_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

map = []
seen = []
totals = []

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

pad = '.............................................................................................'
pad_length = len(pad)

state = pad + state + '............................................................................................................................................................................................................................................................................................................................................................................................................................................................'

print ' 0 :  ',
print state

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
   

totals.append(0)
for iter in range(1, 921):
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
  if iter < 10:
    print '',
  print iter,
  print ": ",
  print '',
  #print state

  total = 0
  for i in range(0, len(state)):
    if state[i] == '#':
      total += i - pad_length
  print "Total = " + str(total) 
  totals.append(total)

# find pattern
print "Finding pattern..."
for offset in range(1, 202):
 for step in range(1, 201):
  diff = totals[offset+step] - totals[offset]
  diff2 = totals[offset+step+step] - totals[offset+step]
  diff3 = totals[offset+step+step+step] - totals[offset+step+step]

  if diff == diff2 == diff3:
    print "Offset: " + str(offset)
    print "Checking: " + str(totals[offset]) + " - " + str(totals[offset+step]) + " - " + str(totals[offset+step+step])
    print "   diffs: " + str(diff) + " - " + str(diff2) + " - " + str(diff3)

    print "Step " + str(step) + " looks like a good bet"

# Offset 86, then every 20?
for x in range(1, 20):
  print totals[86+(x*20)]

print '-------'
for x in range(0, 10):
  iter = 200 + (50*x)
  guess = totals[200] + (x) * 2750
  print str(iter) + " " + str(totals[200+(x*50)]) + ' ' + str(guess)

print '-------'

base = totals[200]
inc = ((50000000000 -200) / 50) * 2750 

result = base + inc

print '-------'
print result