import math


def Cholesky_Method(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for k in range(i + 1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            if (i == k):  # Diagonal elements
                L[i][k] = math.sqrt(matrix[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (matrix[i][k] - tmp_sum))

    return L