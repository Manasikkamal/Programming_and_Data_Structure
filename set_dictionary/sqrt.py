def square_matrix_elements(matrix=[]):
    result_matrix = [[0 for _ in row] for row in matrix]
 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = square_matrix_elements(matrix)
print(new_matrix)
print(matrix)
