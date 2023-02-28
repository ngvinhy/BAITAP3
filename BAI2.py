import random


def khoitao(a):
    return [random.randint(0, 10) for _ in range(a)]


def ktralistdoixung(listt: list):
    return listt == listt[::-1]


def xoaphantu(listt, i):
    return [x for x in listt if x != i]


lst = []
print("""1. Khởi tạo list
2. Xóa phần tử k
3. Kiểm tra list đối xứng
4. Thoát chương trình""")
while True:
    try:
        chucnang = int(input("Chọn chức năng muốn sử dụng: "))
        if chucnang == 1:
            try:
                n = int(input("Nhập số giá trị ngẫu nhiên muốn thêm: "))
                if n > 0:
                    lst = khoitao(n)
                    print(f"List hiện tại: {lst}")
                else:
                    print("Số giá trị phải là số nguyên dương, vui lòng nhập lại")
            except ValueError:
                print("Số giá trị phải là số nguyên dương, vui lòng nhập lại")
        elif chucnang == 2:
            k = int(input("Nhập giá trị k cần xóa: "))
            lst = xoaphantu(lst, k)
            print(f"Các phần tử có giá trị {k} đã được xóa\nList hiện tại: {lst}")
        elif chucnang == 3:
            if ktralistdoixung(lst):
                print(f"List {lst} đối xứng")
            else:
                print(f"List {lst} không đối xứng")
        elif chucnang == 4:
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại")
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại")
