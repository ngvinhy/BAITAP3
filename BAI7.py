def nhapmatrix():
    m, n = map(int, input("Nhập số hàng và số cột của ma trận: ").split())
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i][j] = int(input(f"Nhập giá trị phần tử ({i+1}, {j+1}): "))
    return matrix


# Test
matran1 = nhapmatrix()
matran2 = nhapmatrix()


def congmatrix(matrix1, matrix2):
    m1, n1 = len(matrix1), len(matrix1[0])
    m2, n2 = len(matrix2), len(matrix2[0])
    if m1 != m2 or n1 != n2:
        return "Không thể cộng hai ma trận không cùng kích thước"
    matrix = [[0 for _ in range(n1)] for _ in range(m1)]
    for i in range(m1):
        for j in range(n1):
            matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix


print(congmatrix(matran1, matran2))


def hoanvimatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    kq = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            kq[i][j] = matrix[j][i]
    return kq


print(hoanvimatrix(matran1))
