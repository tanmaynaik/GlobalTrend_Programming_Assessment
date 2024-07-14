'''Write a Python function that takes a 2D list (matrix)
and returns its transpose'''

def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed.append([])
        for j in range(len(matrix)):
            transposed[i].append(matrix[j][i])
    return transposed
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))  