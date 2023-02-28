import random


def khoitao(a):
    listt = []
    for i in range(a):
        while True:
            x = random.randint(0, 10)
            if x not in listt:
                listt.append(x)
                break
    return listt


try:
    n = int(input("Nhập số phần tử ngẫu nhiên muốn thêm vào list: "))
    if n > 0:
        print(f"List gồm {n} phần tử ngẫu nhiên không trùng nhau: {khoitao(n)}")
    else:
        print("Số phần tử phải là số nguyên dương")
except ValueError:
    print("Số phần tử phải là số nguyên dương")
