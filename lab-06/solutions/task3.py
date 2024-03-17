import numpy as np
from task1 import vector_dot_product

def is_matrix_regular(matrix):
    """
    Checks if all rows in a matrix are of the same length

    Arguments:
        matrix (list): A 2D list representing the matrix.
    
    Returns:
        bool: True if matrix is regular
    """

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(1, rows):
        if len(matrix[i]) != columns:
            return False
        
    return True
            
def matrix_multiply(matrix1, matrix2):
    """
    Performs matrix-matrix multiplication from first principles.

    Arguments:
        matrix1 (list): A 2D list representing the first matrix.
        matrix2 (list): A 2D list representing the second matrix.
    
    Returns:
        list: The resulting matrix after matrix-matrix multiplication.
    
    Raises:
        ValueError: If the number of columns in the first matrix is not equal
                    to the number of rows in the second matrix.
    """

    if not is_matrix_regular(matrix1):
        raise ValueError("matrix1 is irregular")
    
    if not is_matrix_regular(matrix2):
        raise ValueError("matrix2 is irregular")
    
    # Check if the dimensions are compatible for matrix multiplication
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("matrices cannot be multiplied")
    
    rows = len(matrix1)
    columns = len(matrix2[0])
    n = len(matrix2)

    # Initialize the resulting matrix with zeros    
    result = [[0 for _ in range(columns)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(columns):
            result[r][c] = sum(matrix1[r][i] * matrix2[i][c] for i in range(n))

    return result

def test(matrix1, matrix2):
    try:
        result = matrix_multiply(matrix1, matrix2)
        print("pp:", result)
    except ValueError as e:
        print("pp:", e)

    try:
        A = np.array(matrix1)
        B = np.array(matrix2)
        result_np = A.dot(B)
        print("np:", result_np)
    except ValueError as e:
        print("np:", e)

    print("")

if __name__ == '__main__':
    # Example 1
    test([[1, 2], [3, 4]], [[5, 6], [7, 8]])

    # Example 2
    test([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    
    # Example 3
    test([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]])
