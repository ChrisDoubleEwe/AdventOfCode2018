d = 0
s = set()
part1 = True
while True:
    e = d | 0x10000
    d = 5557974
    while True:
        c = e & 0xFF
        d += c
        d &= 0xFFFFFF
        d *= 65899
        d &= 0xFFFFFF
        if (256 > e):
            if part1:
                print(d)
                exit(0)
            else:
                if d not in s:
                    print(d)
                s.add(d)
                break      
        c = 0
        # the following code was the optimised part
        e = e // 256
