import time
import numpy as np
from task2 import matrix_vector_product

# Generate a random matrix and vector
matrix_size = 1000
vector_size = 1000

# create a matrix with elements chosen randomly from 1-9
matrix = [[np.random.randint(1, 10) for _ in range(vector_size)] for _ in range(matrix_size)]

# create a vector with elements chosen randomly from 1-9
vector = [np.random.randint(1, 10) for _ in range(vector_size)]

# matrix vector multiplication using List implementation
start_time = time.time()
i = 0
while time.time() - start_time < 5:
    result_list = matrix_vector_product(matrix, vector)    
    i += 1
end_time = time.time()    
list_time = (end_time - start_time) / i
print(f"List implementation time: {list_time:.6f} seconds")

# NumPy implementation
start_time = time.time()
matrix_np = np.array(matrix)
vector_np = np.array(vector)
i = 0
while time.time() - start_time < 5:
    result_np = matrix_np.dot(vector_np)
    i += 1
end_time = time.time()
numpy_time = (end_time - start_time) / i
print(f"NumPy implementation time: {numpy_time:.6f} seconds")

# Check if the results are the same
assert np.array_equal(result_list, result_np)
print("Results are the same")

print("numpy implementation is %.1f times faster than the list implementation" % (list_time/numpy_time))