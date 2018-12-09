import re

with open("08_a_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print content

data_string = content[0].split(' ')
data = []
for d in data_string:
  data.append(int(d))


print data
total_metadata = 0
total_node_values = 0

def process_node():
  node_value = 0
  global total_metadata
  children = data.pop(0)
  metadata = data.pop(0)
  child_values = []
  for child in range(0, children):
    child_values.append(process_node())
  print "NODE:"
  print "  children = " + str(children)
  print "  metadata = " 
  for meta in range(0, metadata):
    m = data.pop(0)
    total_metadata += m
    m = m - 1
    if children > 0:
      if len(child_values) > m:
        print "len = " + str(len(child_values)) + " ; m = " + str(m)
        node_value += child_values[m]
    else:
      node_value += m + 1
    print "    " + str(m)
  print "NODE VALUE = " + str(node_value)
  return node_value

while data != []:
  process_node()

print "total_metadata = " + str(total_metadata)

