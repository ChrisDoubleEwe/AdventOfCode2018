import re

with open("04_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

shifts=[]
for x in content:
  shift=[]
  x1=(x.split('] ')) 
  datetime=x1[0]
  message=x1[1]

  x2=(datetime.split(' '))
  x4=(x2[0].split('['))
  date=x4[1]
  time=x2[1] 

  x3 = (time.split(':'))
  hour=x3[0]
  min=x3[1]

  if message.find('Guard ') != -1:
    x6=(message.split(' '))
    guard_num=x6[1]
  else:
    guard_num="-"

  shift.append(guard_num)
  shift.append(date)
  shift.append(hour)
  shift.append(min)
  shift.append(message)
  shifts.append(shift)

first_row = 1
current_min = 0
asleep = 0

rows = []
timerow = ['.'] * 60


def fill(list, start, stop):
  print "  Filling from " + str(start) + " to " + str(stop)
  for i in range(start, stop):
    list[i]='#'

guard_number = ''
this_date = ''

for shift in shifts:
  # Have we got a new guard starting duty?
  if shift[0] != '-':
    print "New guard"
    # Yes, it's a new guard.
    if asleep == 1:
      fill(timerow, current_min, 60)
      print timerow
      newrow = []
      newrow.append(this_date)
      newrow.append(guard_number)
      newrow.append(timerow)
      rows.append(newrow)
      timerow = ['.'] * 60
    else:
      print timerow
      newrow = []
      newrow.append(this_date)
      newrow.append(guard_number)
      newrow.append(timerow)
      rows.append(newrow)
      timerow = ['.'] * 60

    guard_number = shift[0]
    this_date = shift[1]


    
    asleep = 0
    if int(shift[2])>0:
      current_min=0
    else:
      current_min=int(shift[3])

  # Has the guard fallen asleep?
  if shift[4] == 'falls asleep':
    print "  Guard falls asleep"
    asleep = 1
    if int(shift[2])>0:
      current_min=0
    else:
      current_min=int(shift[3])

  # Has the guard woken up?
  if shift[4] == 'wakes up':
    print "  Guard wakes up"
    asleep = 0
    fill(timerow, current_min, int(shift[3]))
    if shift[2]>0:
      current_min=0
    else:
      current_min=int(shift[3])

# Print output
rows.pop(0)
for row in rows:
  print row[0] + ' ' + row[1] + '  ' + ''.join(row[2])

# Find which guard spent the most time asleep
guards = []
for row in rows:
  guards.append(row[1])

guards = sorted(set(guards))
print guards

results = []
for guard in guards:
  asleep_time = 0
  for row in rows:
    if row[1] == guard:
      asleep_time = asleep_time + row[2].count('#') 
  pair = []
  pair.append(guard)
  pair.append(asleep_time)
  results.append(pair)

print results

max_guard = ''
max_time = 0
for r in results:
  if r[1] > max_time:
    max_time = r[1]
    max_guard = r[0]

print "Max time asleep = " + max_guard + " with " + str(max_time) + " minutes"

# Find minute for that guard when they are asleep most
asleep = [0] * 60
for row in rows:
  if row[1] == max_guard:
    for i in range(0,60):
      if row[2][i] == '#':
        asleep[i] = asleep[i]+1

print asleep
max_asleep = 0
max_min = 0
for i in range(0,60):
  if asleep[i] > max_asleep:
    max_asleep = asleep[i]
    max_min = i

print "Guard " + max_guard + " is most likely to be asleep in minute " + str(max_min) + " (" + str(max_asleep) + " mins)"

guard_parts = max_guard.split('#')
guard_num = guard_parts[1]

out = int(guard_num) * max_min

print "RESULT = " + str(out)

