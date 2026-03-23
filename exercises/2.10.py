print("Nhap so giay:"); t = int(input())
hour = (t // 3600) % 12
minute = (t % 3600) // 60
second = (t % 3600) % 60
if (t % 86400) > 43199:
    indicator = "PM"
else:
    indicator = "AM"
if hour == 0: hour = 12
print("Time:", hour,":", minute,":",second, indicator)