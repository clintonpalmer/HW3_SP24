
def doolittle(matrix):
    """
    Performs Doolittle's method for LU decomposition on a given square matrix.
    The function decomposes a given square matrix into the product of a lower triangular matrix (L) and an upper triangular matrix (U).
    Parameters:
    matrix (list of list of float): The square matrix to be decomposed.
    Returns:
    L (list of list of float): The lower triangular matrix resulting from the LU decomposition.
    U (list of list of float): The upper triangular matrix resulting from the LU decomposition.
    chatgpt assisted in developing this function
    """
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