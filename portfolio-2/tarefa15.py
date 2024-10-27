import sys

def matrix_chain_order(dimensions):
    n = len(dimensions) - 1
    m = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        m[i][i] = 0
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m

if __name__ == "__main__":
    n = int(input("Enter the number of matrices: "))
    dimensions = []
    for i in range(n + 1):
        dimensions.append(int(input("Enter the dimension of matrix {}: ".format(i))))
    result = matrix_chain_order(dimensions)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("m[{}][{}] = {}".format(i, j, result[i][j]))