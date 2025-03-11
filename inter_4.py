# Write a Python function that takes a 2D matrix (list of lists) and returns its transpose.
def transpose_matrix(matrix):
    transposed = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[col])
        transposed.append(new_row)  
    return transposed
matrix = [
    [1, 2],
    [4, 5],
    [7, 8]
]
transposed = transpose_matrix(matrix)
print(transposed)
