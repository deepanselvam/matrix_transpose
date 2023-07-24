def matrix(A, n, m):
    for i in range(n):
        for j in range(m):
            if i < j:
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp
    return A

n = int(input("enter the number of rows: "))
m = int(input("enter the number of columns: "))
A = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input("enter a value: ")))
    A.append(row)

value = matrix(A, n, m)
for values in value:
    print(values)
