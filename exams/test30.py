nhap = input()
a = nhap.split()

if a[0] == '1':
    level = float(a[1])
    if level < 0:
        print('-1')
    else:
        angle = 36 * level
        print(round(angle))

if a[0] == '2':
    usr = int(a[1])
    m_current = int(a[2])
    m_old = int(a[3])
    diff = m_current - m_old

    if (usr < 0) or (m_current < 0) or (m_old < 0) or (diff < 0):
        print('-1')
    else:
        mpu = diff / usr
        if mpu < 4:
            price = mpu * usr * 8509
        if 4 <= mpu < 6:
            price = usr * (4 * 8509 + (mpu - 4) * 16383)
        if mpu >= 6:
            price = usr * (4 * 8509 + 2 * 16383 + (mpu - 6) * 18288)
        print(round(price))

if a[0] == '3':
    fl_start = int(a[1])
    fl_end = int(a[2])
    load = int(a[3])
    d = (fl_end - fl_start)

    if load < 0:
        print('-1')
    else:
        if load <= 1000:
            if d < 0:
                power = 5 * load * abs(d)
            else:
                power = 7 * load * d
        if 1000 < load <= 1600:
            if d < 0:
                power = (5 * 1000 + 7 * (load - 1000)) * abs(d)
            else:
                power = (7 * 1000 + 12 * (load - 1000)) * d
        if 1600 < load <= 2600:
            if d < 0:
                power = (9200 + (load - 1600) * 5) * abs(d)
            else:
                power = (14200 + (load - 1600) * 7) * d

    print(power)

if a[0] == '4':
    battery_level = int(a[1])
    kmode = int(a[2])

    if kmode == 1:
        distance = battery_level / 3 * 5

    if kmode == 2:
        if battery_level >= 50:
            distance = 5 * ((battery_level - 50) / 3.6 + 30 / 4.9 + 20 / 7)
        if 20 <= battery_level < 50:
            distance = 5 * ((battery_level - 20) / 4.9  + 20 / 7)
        if battery_level < 20:
            distance = battery_level / 7 * 5

    if kmode == 3:
        if battery_level >= 50:
            distance = 5 * ((battery_level - 50) / 8 + 30 / 10.5)
        if 20 <= battery_level < 50:
            distance = 5 * ((battery_level - 20) / 10.5)
        if battery_level < 20:
            distance = 0

    if kmode == 4:
        if battery_level >= 50:
            distance = 5 * ((battery_level - 50) / 4.4 + 30 / 5.3)
        if 20 <= battery_level < 50:
            distance = 5 * ((battery_level - 20) / 5.3)
        if battery_level < 20:
            distance = 0

    print(round(distance, 2))

if a[0] == '5':
    def calculate_distance(trip):
        current_battery = 100  # dung lượng pin ban đầu là 100%
        total_distance = 0  # tổng quãng đường đã đi được

        for segment in trip:
            if segment > 0:  # Xe đang lên dốc
                distance_possible = min(segment, current_battery * 2.15)  # Xác định quãng đường có thể đi được, không vượt quá dung lượng pin
                total_distance += distance_possible  # Cập nhật tổng quãng đường
                current_battery -= distance_possible / 2.15  # Giảm dung lượng pin tương ứng
                current_battery = round(current_battery)
            elif segment == 0:  # Xe dừng sạc pin
                current_battery += 25  # Sạc pin thêm 25%
                if current_battery > 100:  # Nếu pin đầy
                    current_battery = 100
            else:  # Xe xuống dốc
                charging_state = abs(segment) // 10  # Tính phần pin được sạc lại từ việc xuống dốc
                current_battery += charging_state
                if current_battery > 100:  # Nếu pin đầy
                    current_battery = 100

                total_distance += abs(segment)  # Cộng vào tổng quãng đường đã đi được

        return print(round(total_distance, 1))  # Trả về tổng quãng đường đã đi được, làm tròn 1 chữ số thập phân

    # Đọc chuỗi số nguyên input sau số 5
    trip = list(map(int, a[1:]))

    # Tính toán và in kết quả
    result = calculate_distance(trip)





