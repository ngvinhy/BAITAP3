def ktrathutu(listt):
    for i in range(len(listt)):
        if listt[i] <= listt[i+1]:
            return True
        else:
            return False


while True:
    try:
        n = int(input("Nhập số phần tử của dãy số: "))
        if n > 1:
            lst = []
            j = 0
            while j < n:
                try:
                    k = int(input("Nhập các giá trị của dãy: "))
                    lst.append(k)
                    j += 1
                except ValueError:
                    print("Dãy số chỉ gồm số nguyên")
            if ktrathutu(lst):
                print(f"Dãy số thỏa mãn yêu cầu: {lst}")
                break
            else:
                print(f"Dãy số không thỏa mãn yêu cầu, xin vui lòng nhập lại")
        else:
            print("Dãy số phải gồm nhiều hơn 1 phần tử")
    except ValueError:
        print("Số phần tử phải là số nguyên dương")
