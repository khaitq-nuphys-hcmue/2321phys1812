x = int(input('Nhap x: '))
n = int(input('Nhap n: '))
i=p=1
s=0
while i<=n:
    p*=i
    s+= pow(x, i) / p
    i+=1
print('Tong:', s)