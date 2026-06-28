def matrix_addition(matrix1, matrix2):
    # Check if matrices are the same size
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Error: Matrices must have the same dimensions to add."
    #1. start with empty matrix
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    #2. # Loop through rows and columns to add matching elements
    for r in range(len(A)):
        for c in range(len(A[0])):
            result[r][c] = A[r][c] + B[r][c]
    return result