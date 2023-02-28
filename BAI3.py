import random


def khoitao(a, b):
    return [[random.randint(0, 10) for _ in range(b)] for _ in range(a)]


def dong(matrx, i):
    return matrx[i-1]


def cot(matrx, j):
    return [hang[j-1] for hang in matrx]


def lonnhat(matrx):
    return max([max(i) for i in matrx])


matrix = []
while True:
    print("""1. Khởi tạo ma trận
2. Truy xuất dòng
3. Truy xuất cột
4. Giá trị MAX trong ma trận
5. Thoát chương trình""")
    try:
        chucnang = int(input("Chọn chức năng muốn sử dụng: "))
        if chucnang == 1:
            try:
                M, N = map(int, input("Nhập số hàng và số cột của ma trận, cách nhau bởi dấu cách: ").split())
                matrix = khoitao(M, N) if M and N > 0 else "Số hàng và số cột phải là số nguyên dương, vui lòng nhập lại"
                print(f"Ma trận ngẫu nhiên {M}x{N}: {matrix}")
            except ValueError:
                print("Số hàng và số cột phải là số nguyên dương, vui lòng nhập lại")
        elif chucnang == 2:
            m = int(input("Nhập dòng cần tìm: "))
            if matrix:
                try:
                    print(f"Dòng thứ {m} của ma trận: {dong(matrix, m)}" if m > 0 else f"Dòng {m} không tồn tại trong ma trận")
                except IndexError:
                    print(f"Dòng {m} không tồn tại trong ma trận")
            else:
                print("Ma trận chưa được khởi tạo")
        elif chucnang == 3:
            n = int(input("Nhập cột cần tìm: "))
            if matrix:
                try:
                    print(f"Cột thứ {n} của ma trận: {cot(matrix, n)}" if n > 0 else f"Cột {n} không tồn tại trong ma trận")
                except IndexError:
                    print(f"Cột {n} không tồn tại trong ma trận")
            else:
                print("Ma trận chưa được khởi tạo")
        elif chucnang == 4:
            print(f"Giá trị lớn nhất trong ma trận là: {lonnhat(matrix)}" if matrix else "Ma trận chưa được khởi tạo")
        elif chucnang == 5:
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại")
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại")
