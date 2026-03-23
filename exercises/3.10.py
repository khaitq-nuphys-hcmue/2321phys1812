import math

a = float(input("Nhap he so a:"))
b = float(input("Nhap he so b:"))
c = float(input("Nhap he so c:"))
det = b**2 - 4*a*c
if det < 0:
    print("Phuong trinh", a, "x^2 +", b,"x +",c,"= 0 vo nghiem")
elif det > 0:
    x1 = (- b - math.sqrt(det)) / (2 * a)
    x2 = (- b + math.sqrt(det)) / (2 * a)
    print("Phuong trinh", a, "x^2 +", b,"x +",c,"= 0 co hai nghiem la x_1 =", round(x1,4), "va x_2=", round(x2,4))
else:
    x = -b / (2 * a)
    print("Phuong trinh", a, "x^2 +", b,"x +",c,"= 0 co nghiem kep x =", round(x, 4))