year = int(input("Nhap nam:"))
month = int(input("Nhap thang:"))
if (month in (1,3,5,7,8,10,12)):
    print("Thang", month, "nam", year, "co 31 ngay.")
elif (month == 2):
    if ((year % 4) == 0 and (year % 100) != 0) or (year % 400 == 0):
        print("Thang", month, "nam", year, "co 29 ngay.")
    else:
        print("Thang", month, "nam", year, "co 28 ngay.")
else:
    print("Thang", month, "nam", year, "co 30 ngay.")