import re

with open("02_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
two = 0
three = 0
for x in content:
  y = ''.join(sorted(x))
  y = ' ' + y + ' ' 

  print x+'   '+y
  matchFour = re.match( r'.*(\w)\1\1\1', y)
  if matchFour:
    print y
    print "match four"
    y=re.sub(r'(\w)\1\1\1','-',y)

  matchThree = re.match( r'.*(\w)\1\1[^\1]', y)
  if matchThree:
    three=three+1
    print "  match three: " + str(three)
    y=re.sub(r'(\w)\1\1','-',y)
    print '      ' + y

  matchTwo =   re.match( r'.*(\w)\1[^\1]', y)


  if matchTwo:
    two=two+1
    print "  match two: " + str(two)

print str(two)
print str(three)
total = two * three

print str(total)
