def dayso(n):
    lst = []
    i = 0
    while i < n:
        try:
            k = float(input("Nhập các giá trị của list: "))
            lst.append(k)
            i += 1
        except ValueError:
            print("List chỉ gồm số thực")
    lst.sort(reverse=True)
    return lst


while True:
    try:
        N = int(input("Nhập số phần tử của list: "))
        if N > 0:
            print(f"Dãy số theo thứ tự giảm dần: {dayso(N)}")
            break
        else:
            print("Số phần tử phải là số nguyên dương")
    except ValueError:
        print("Số phần tử phải là số nguyên dương")
