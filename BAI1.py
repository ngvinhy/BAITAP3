def ktrasonguyento(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


lst = []
while True:
    print("""1. Thêm phần tử vào list
2. Kiểm tra k xuất hiện bao nhiêu lần trong list
3. Tính tổng các số nguyên tố trong list
4. Sắp xếp
5. Xóa list
6. Thoát chương trình""")
    chucnang = int(input("Chọn chức năng muốn sử dụng: "))
    if chucnang == 1:
        a = int(input("Nhập giá trị muốn thêm: "))
        lst.append(a)
        print(f"List hiện tại: {lst}")
    elif chucnang == 2:
        k = int(input("Nhập giá trị k cần kiểm tra: "))
        dem = lst.count(k)
        print(f"Giá trị {k} xuất hiện {dem} lần trong list")
    elif chucnang == 3:
        tong = 0
        for a in lst:
            if ktrasonguyento(int(a)):
                tong += a
        print(f"Tổng các số nguyên tố trong list là: {tong}")
    elif chucnang == 4:
        if lst:
            lst.sort()
            print(f"List được sắp xếp: {lst}")
        else:
            print("List rỗng")
    elif chucnang == 5:
        lst.clear()
        print("List đã được xóa")
    elif chucnang == 6:
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại")
