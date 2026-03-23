print("Nhap vao so nam:"); year = int(input())
if ((year % 4) == 0 and (year % 100) != 0) or (year % 400 == 0):
    print("Nam", year, "la nam nhuan")
else: print("Nam", year, "khong la nam nhuan")