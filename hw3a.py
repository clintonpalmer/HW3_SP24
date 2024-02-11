import math
import copy
from DooLittle_Method import doolittle
from Cholesky_Method import Cholesky_Method

def is_positive_definite(matrix):
  """
  This code first check to see if the matrix is symmetric.
  If it is not then it cannot be positive definite. Then it
  checks if all the eigenvalues are positive. If this is
  true then the matrix is positive definite.
  Args:
    matrix: A square matrix.
  Returns:
  True if the matrix is positive definite, False otherwise.
  Googles generative AI assisted with the dev of this function.
  """

  # Make a copy of the matrix so we don't modify the original.
  matrix_copy = copy.deepcopy(matrix)

  # Check if the matrix is symmetric.
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      if matrix_copy[i][j] != matrix_copy[j][i]:
        return False

  # Check if all of the eigenvalues of the matrix are positive.
  eigenvalues = []
  for i in range(len(matrix)):
    eigenvalues.append(math.sqrt(matrix_copy[i][i]))

  for eigenvalue in eigenvalues:
    if eigenvalue <= 0:
      return False

  # If all of the eigenvalues are positive, then the matrix is positive definite.
  return True

def forward_substitution(L, b):
    """
    This function is used to solve a set of linear equations that has
    a lower triangle matrix, The function iterates over each equation
    in the system from the first to the n-th equation. For each
    equation it calculates the solution y[i].
    :param L: lower triangular matrix
    :param b: the right hand side vector of the system of equations
    :return: "y" the solution vector for the system of equations
    chatgpt assisted with the development of this function
    """
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
    return y

def backward_substitution(U, y):
    """
    This function is used to solve a set of linear equations that has
    a upper triangle matrix, The function iterates over each equation
    in the system from the first to the n-th equation. For each
    equation it calculates the solution y[i].
    :param U:  upper triangular matrix
    :param y:  right hand side vector of the system of equations
    :return:  "x" the solution vector for the system of equations
    chatgpt assisted with the development of this function
    """
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x

def transpose_matrix(matrix):
    """
    This function transposes the matrix as part of the Cholesky
    Method solution.
    The * operator is used ot unpack the matrix,
    The zip function groups elements (into columns) from each row together based on their position.
    The map function applies the list function to each group of elements created by zip,
    converting each group (of columns) into a list (rows).
    list - converts the map object into a list of list.
    (swaps rows with columns to transpose)
    :param matrix: "A" matrix provided by the user.
    :return: transposed matrix
    chatgpt assisted with the development of this function
    """
    return list(map(list, zip(*matrix)))

def solve_matrix(augmented_matrix):
    """
    This function provides 2 different methods for solving a system
    of linear equations.  Cholesky method and Doolittle Method.
    ,
    :param augmented_matrix:
    :return:
    """
    n = len(augmented_matrix)
    matrix = [row[:-1] for row in augmented_matrix]  # Coefficient matrix
    b = [row[-1] for row in augmented_matrix]  # Right-hand side vector
    if is_positive_definite(matrix):
         # Use Cholesky decomposition
         L = Cholesky_Method(matrix)
         LT = transpose_matrix(L)
         y = forward_substitution(L, b)
         x = backward_substitution(LT, y)
         print("The Cholesky Method")
         print("Solution: ", x)
    else:
         # Use Doolittle's method
         L, U = doolittle(matrix)  # Pass the coefficient matrix, not the augmented matrix
         y = forward_substitution(L, b)
         x = backward_substitution(U, y)
         print("The Doolittle Method")
         print("Solution: ", x)

augmented_matrix = [[1, -1, 3, 2, 15],
                    [-1, 5, -5, -2, -35],
                    [3, -5, 19, 3, 94],
                    [2, -2, 3, 21, 1]]

solve_matrix(augmented_matrix)

augmented_matrix2 = [[4, 2, 4, 0, 20],
                    [2, 2, 3, 2, 36],
                    [4, 3, 6, 3, 60],
                    [0, 2, 3, 9, 122]]

solve_matrix(augmented_matrix2)