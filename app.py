import numpy as np

# #Create 1D null numpy array
# my_zero_arr = np.zeros(10)
# print(my_zero_arr)

# #Get totally memory array occuped 
# my_zero_arr_memory = my_zero_arr.size * my_zero_arr.itemsize
# print(my_zero_arr_memory)

# #Get numpy.zeros documentation
# get_numpy_zeros_info = np.info(np.zeros)
# print(get_numpy_zeros_info)

# #Change fifth element to 1
# my_zero_arr_two = np.zeros(10)
# my_zero_arr_two[4] = 1
# print(my_zero_arr_two)

# #Create an array with values from 10 to 49
# my_arange_arr = np.arange(10, 50)
# print(my_arange_arr)

# #Create an array from 0 to 9 and reverse.
# my_arange_arr_two = np.arange(0, 10)
# print(my_arange_arr_two[::-1])

# #Create a vector from 0 to 8 and reshape it to a 3x3 matrix
# my_vector_to_matrix = np.arange(0, 9)
# my_vector_to_matrix = my_vector_to_matrix.reshape(3,3)
# print(my_vector_to_matrix)

# #Find indices of the non zero elements
# my_non_arr = [1,2,0,0,4,0]
# my_non_arr_wo0 = np.nonzero(my_non_arr)
# print(my_non_arr_wo0)

# #Create identity matrix 3x3
# identity_matrix = np.eye(3)
# print(identity_matrix)

# #Create an array with three random numbers
# arr = np.random.random(3)
# print(arr)

# #Find the maximum value
# arr = np.random.random(10)
# print(np.max(arr))

# #Find the mean value
# arr = np.random.random(10)
# print(np.mean(arr))

# #Matrix of one with zeros in the center
# arr = np.ones((5, 5))
# arr[1:-1,1:-1] = 0
# print(arr)

# #Change border one's to zeros
# arr = np.ones((5, 5))
# print(np.pad(arr, 1))

# #Check expresions
# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(np.nan in set([np.nan]))
# print(0.3 == 3 * 0.1)

# #Create a vector from 0 to 8 and reshape it to a 3x3 matrix and print diagonal.
# my_vector_to_matrix = np.arange(0, 9)
# my_vector_to_matrix = my_vector_to_matrix.reshape(3,3)
# print(np.diag(my_vector_to_matrix))

# #Create 8x8 matrix and fill with a checkerboard
# matrix = np.zeros((8, 8))
# matrix[1::2, ::2] = 1
# matrix[::2, 1::2] = 1
# print(matrix)