import math
n = int(input('Nhap n: '))

if n<2:
    print(n,'khong la so nguyen to')
elif n>2:
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            print(n, 'khong la so nguyen to')
            break
    else:
            print(n,'la so nguyen to')
else:
    print(n, 'la so nguyen to')