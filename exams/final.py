from math import *

nhap = input()
a = nhap.split()
option = int(a[0])

if option == 1:
    x = float(a[1])
    if x < 0:
        value = sin(x) * cos(5*x)
    elif x == 0:
        value = 0
    else:
        value = exp(x) * (5**x)/(x+5)
    print(value)
    
if option == 2:
    n = int(a[1])
    
    def sum(n):
        s = 0
        i = 1
        for i in range(1, n+1):
            s += (i+1) / (sqrt(i))
            i += 1
        return print(s)
        
    if n<0:
        while n<0:
            n = int(input('Nhap lai: '))
        sum(n)
    else:
        sum(n)
    
if option == 3:
    s_floor = int(a[1])
    e_floor = int(a[2])
    load = int(a[3])
    
    if load < 0:
        power = -1
    else:
        distance = e_floor - s_floor
        if load <= 1000:
            if distance <= 0:
                power = 5 * abs(distance) * load
            else:
                power = 7 * distance * load
        if 1000 <= load <= 1600:
            if distance <= 0:
                power = abs(distance)* (5 * 1000 + 7 * (load - 1000))
            else:
                power = distance * (7 * 1000 + 12 * (load - 1000))
        if 1600 <= load <= 2600:
            if distance <= 0:
                power = abs(distance) * (5 * 1000 +  7 * 600 + 5 * (load - 1600))
            else:
                power = distance * (7 * 1000 + 12 * 600 + 7 * (load - 1600))
        
    print(power)
    