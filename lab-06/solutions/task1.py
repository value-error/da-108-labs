import numpy as np

def vector_dot_product(a, b):
    """
    The function computes and returns the dot product between two vectors.

    Arguments:
        a: list of values denoting elements of a vector
        b: list of values denoting elements of a vector
    
    Returns:
        y: floating-point number representing the dot product
           or None if the lengths of the vectors are unequal
    """
    
    if len(a) != len(b):
        return None
    
    y = 0

    for i in range(len(a)):
        y += a[i] * b[i]

    return y

def test(a, b):
    result = vector_dot_product(a, b)
    print("pp :", result)

    try:
        result_np = np.dot(a, b)
        print("np :", result_np)
    except ValueError:
        print("np : ValueError")

    print("")

if __name__ == '__main__':
    # Example with equal vector lengths
    test([1, 2, 3], [4, 5, 6])

    # Example with unequal vector lengths
    test([2, 4, 6, 8], [1, 3, 5])
