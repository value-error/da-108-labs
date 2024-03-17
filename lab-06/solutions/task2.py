import numpy as np
from task1 import vector_dot_product

def matrix_vector_product(matrix, vector):
    """
    Performs matrix-vector multiplication from first principles.
    
    Arguments:
        matrix (list): A 2D list representing the matrix.
        vector (list): A 1D list representing the vector.
    
    Returns:
        list: The resulting vector after matrix-vector multiplication.

    Raises:
        ValueError: matrix row lengths are irregular.
        ValueError: count of cols in the matrix is not equal to len of the vector.
    """

    # Check if matrix is regular
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(1, rows):
        if len(matrix[i]) != columns:
            raise ValueError("matrix rows are irregular")
    
    # Check if the number of columns in the matrix is equal to the length of the vector
    if len(vector) != columns:
        raise ValueError("number of columns in matrix does not match length of vector")
    
    result = [vector_dot_product(matrix[i], vector) for i in range(rows)]
    return result

def test(matrix, vector):
    try:
        result = matrix_vector_product(matrix, vector)
        print("pp :", result)
    except ValueError as e:
        print("pp:", e)

    try:
        M = np.array(matrix)
        v = np.array(vector)
        print("np :", M.dot(v))
    except ValueError as e:
        print("np:", e)
    
    print("")

if __name__ == '__main__':
    # Example 1
    test([[1, 2], [3, 4]], [5, 6])

    # Example 2
    test([[1, 2, 3], [3, 4]], [5, 6, 7])

    # Example 3
    test([[1, 2, 3], [4, 5, 6]], [7, 8])
