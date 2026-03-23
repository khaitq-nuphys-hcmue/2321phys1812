from math import *

nhap = input()
arr = nhap.split()
arr[0] = int(arr[0])

if arr[0] == 1:
    x = float(arr[1])
    y = float(arr[2])
    S = ( (3*y*x**3 - 0.5*x**2 + 0.2*x*y) * 6*x*y**3 ) ** (1/3)

    print(S)

if arr[0] == 2:
    r = float(arr[1])
    h = float(arr[2])
    B = pi * r ** 2
    V = B * h
    Sxq = 2 * pi * r * h
    Stp = 2 * B + Sxq

    print(V, Sxq, Stp)

if arr[0] == 3:
    x = float(arr[1])
    if x < 0:
        f = sin(x) * cos(5*x)
    elif x == 0:
        f = 0
    else:
        f = e**x * (5**x)/(x+5)
    print(f)

if arr[0] == 4:
    qt1 = float(arr[1])
    qt2 = float(arr[2])
    gk = float(arr[3])
    ck = float(arr[4])

    gpa = round((0.1 * qt1 + 0.2 * qt2 + 0.2 * gk + 0.5 * ck), 2)
    if gpa >= 9:
        rank = 'Xuat sac'
    elif 8 <= gpa < 9:
        rank = 'Gioi'
    elif 6.5 <= gpa < 8:
        rank = 'Kha'
    elif 5 <= gpa < 6.5:
        rank = 'Trung binh'
    else:
        rank = 'Hoc lai'

    print(gpa, rank)

if arr[0] == 5:
    salary = int(arr[1])
    if salary < 0:
        print('Nhap du lieu sai')
    elif 0 <= salary <= 10000000:
        tax = 0.1 * salary
    elif 10000000 <= salary <= 15000000:
        tax = 0.15 * salary
    else:
        tax = 0.2 * salary
    actual_s = salary - tax
    print(f'Thue thu nhap: {round(tax)}, Luong rong: {round(actual_s)}')

if arr[0] == 6:
    income = int(arr[1])
    if income <= 50000000:
        fee = 0
    elif 51000000 <= income <= 100000000:
        fee = 0.03 * income
    elif 101000000 <= income <= 200000000:
        fee = 0.05 * income
    elif 201000000 <= income <= 400000000:
        fee = 0.07 * income
    else:
        fee = 0.09 * income
    print(round(fee))

if arr[0] == 7:
    def exchange(money):
        cashes = [500000, 100000, 50000, 20000, 10000]
        result = {}
        for cash in cashes:
            if money >= cash:
                result[cash] = money // cash
                money = money % cash
        return print(result)

    money = int(arr[1])
    if (money % 10000) != 0:
        print('Nhap du lieu sai')
    else:
        exchange(money)

if arr[0] == 8:
    km = float(arr[1])

    if (km < 0):
        print('Nhap du lieu sai')
    else:
        if km == 1:
            fare = 11000
        if 2 <= km <= 30:
            fare = (11000 + (km - 1) * 14500)
        if km > 30:
            fare = (11000 + 29 * 14500 + (km - 30) * 11600)
        print(round(fare))

if arr[0] == 9:
    code = str(arr[1])
    if len(code) != 8:
        print('Ma khach hang khong hop le')
    else:
        rank_n = code[4]
        if rank_n == '1':
            rank = 'Dong'
        elif rank_n == '2':
            rank = 'Bac'
        elif rank_n == '3':
            rank = 'Vang'
        else:
            rank = 'Chua xep hang'
        print('Xep hang khach hang:', rank)

if arr[0] == 10:
    serial = str(arr[1])
    if len(serial) != 7:
        print('Nhap sai')
    else:
        model = serial[1]
        if model == '3':
            model_name = 'iPhone 14'
        elif model == '4':
            model_name = 'iPhone 14 Plus'
        elif model == '5':
            model_name = 'iPhone 14 Pro'
        elif model == '6':
            model_name = 'iPhone 14 Pro Max'
        else:
            model_name = 'Dien thoai chua san xuat'
        print(model_name)

if arr[0] == 11:
    usage = float(arr[1])

    if (usage < 0):
        print('Nhap sai')
    else:
        if usage <= 4:
            price = 6000 * usage
        if 4 < usage <= 6:
            price = (6000 * 4 + (usage - 4) * 11500)
        if usage > 6:
            price = (6000 * 4 + 2 * 11500 + (usage - 6) * 12800)
        final_price = price * 1.15
        print(round(final_price))

if arr[0] == 12:
    duration = int(arr[1])
    if duration <= 2:
        price = 20000
    elif 3 <= duration <= 10:
        price = 20000 + (duration - 2) * 15000
    elif 11 <= duration <= 23:
        price = 20000 + 8 * 15000 + (duration - 10) * 10000
    else:
        sub1 = 200000 * (duration // 24)
        remain = duration % 24
        if remain <= 2:
            sub2 = 10000 * remain
        elif 3 <= remain <= 10:
            sub2 = 20000 + (remain - 2) * 15000
        elif 11 <= remain <= 23:
            sub2 = 20000 + 8 * 15000 + (remain - 10) * 10000
        price = sub1 + sub2

    print(price)

if arr[0] == 13:
    n = int(arr[1])
    i = 1
    s = 0
    while i <= n:
        s += (i+1) / sqrt(i)
        i += 1

    print(s)

if arr[0] == 14:
    n = int(arr[1])
    i = 1
    s = 0
    while i <= n:
        s += (-1)**i / i
        i += 1

    print(s)

if arr[0] == 15:
    n = int(arr[1])
    i = p = 1
    s = 0
    while i <= n:
        p *= i
        s += p / i
        i += 1

    print(s)

if arr[0] == 16:
    num = str(arr[1])
    max_digit = -1
    for c in num:
        i = int(c)
        if i > max_digit:
            max_digit = i

    print(max_digit)

if arr[0] == 17:
    pid = int(arr[1])
    qty = int(arr[2])

    if pid not in (1, 2, 3, 4):
        print('Mat hang khong giam gia')
    else:
        if pid == 1:
            unit_price = 500000
        elif pid == 2:
            unit_price = 460000
        elif pid == 3:
            unit_price = 425000
        elif pid == 4:
            unit_price = 450000
        if qty > 5:
            print('Vuot qua so luong quy dinh')
        else:
            subtotal = unit_price * qty
            print('Tien phai tra:', subtotal)

if arr[0] == 18:
    pid = int(arr[1])
    cash = int(arr[2])

    if pid not in (1, 2, 3, 4, 5, 6):
        print('Nhap sai')
    else:
        if pid == 1:
            product_name = 'Tra xanh C2'
            price = 9000
            container = 'chai'
        elif pid == 2:
            product_name = 'Sting'
            price = 11000
            container = 'chai'
        elif pid == 3:
            product_name = 'Pepsi'
            price = 10000
            container = 'chai'
        elif pid == 4:
            product_name = 'Warrior'
            price = 13000
            container = 'chai'
        elif pid == 5:
            product_name = 'Nuoc suoi'
            price = 5000
            container = 'chai'
        elif pid == 6:
            product_name = 'Sua tuoi'
            price = 8000
            container = 'hop'

        if cash < price:
            print('Thieu tien')
        else:
            qty = cash // price
            remainder = cash % price
            print(product_name, '-', qty, container, '- Tien du:', remainder)