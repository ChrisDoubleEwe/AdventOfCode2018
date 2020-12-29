idx = '430971'
r = [3,7]
a = 0
b = 1

def doit():
    global a,b
    s = r[a] + r[b]
    r.extend(list(map(int,str(s))))
    a = (a + r[a] + 1) % len(r)
    b = (b + r[b] + 1) % len(r)

while idx not in ''.join(map(str,r[-10:])):
    doit()
print(''.join(map(str,r)).index(idx))
