with open("01_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
x = ''.join(content)
y=eval(x)
seen=[]

total = 0

while 1:
 for x in content:
  total = eval(str(total)+''.join(x))
  if total in seen:
    print "FREQUENCY: "+str(total)
    exit()
  seen.append(total)
  print "   "+str(total)+"    "+str(x)
  
