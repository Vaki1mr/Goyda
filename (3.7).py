import numpy as np

def solve_linear_system(n, m, matrix):
    matrix = np.array(matrix, dtype=float)
    if matrix.shape != (n, m):
      raise ValueError("Matrix dimensions do not match N and M")
    for i in range(n):
        pivot = matrix[i, i]
        if pivot == 0:
            for k in range(i + 1, n):
                if matrix[k, i] != 0:
                    matrix[[i, k]] = matrix[[k, i]]
                    pivot = matrix[i, i]
                    break
            else:
                if np.any(matrix[i, i+1:]):
                  return None, "no solution"
                else:
                  return None, "infinite"
        matrix[i] /= pivot
        for j in range(n):
            if i != j:
                factor = matrix[j, i]
                matrix[j] -= factor * matrix[i]
    solution = matrix[:, m - 1]
    is_unique = True
    for i in range(n):
        if np.all(matrix[i, :m-1] == 0) and matrix[i, m-1] != 0:
            is_unique = False
            break
    if is_unique:
      return solution, "unique"
    else:
        return None, "unique"
if __name__ == "__main__":
    n = int(input("Enter the number of rows (N): "))
    m = int(input("Enter the number of columns (M): "))
    matrix = []
    print("Enter the augmented matrix (row by row, separated by spaces):")
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    solution, solution_type = solve_linear_system(n, m, matrix)
    if solution is not None:
        print("Solution:", solution)
        print("Solution type:", solution_type)
    else:
        print("Solution type:", solution_type)