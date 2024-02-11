
def doolittle(matrix):
    n = len(matrix)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    for i in range(n):
        for k in range(i, n):
            sum = 0.0
            for j in range(i):
                sum += (L[i][j] * U[j][k])
            U[i][k] = matrix[i][k] - sum

        for k in range(i, n):
            if (i == k):
                L[i][i] = 1.0
            else:
                sum = 0.0
                for j in range(i):
                    sum += (L[k][j] * U[j][i])
                L[k][i] = (matrix[k][i] - sum) / U[i][i]
    return L, U