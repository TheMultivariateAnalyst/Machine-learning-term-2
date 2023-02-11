import numpy as np

# function to perform Gaussian elimination on a matrix
def gaussian_elimination(matrix):
    n = len(matrix)
    # loop through each column
    pivot_cols = 0
    free_cols = 0
    for i in range(n):
        # pivot element is the element in the current column with the largest absolute value
        pivot = max(matrix[i:,i], key=abs)
        # if pivot element is zero, matrix is singular and cannot be inverted
        if pivot == 0:
            free_cols += 1
        else:
            pivot_cols += 1
            # swap the current row with the row containing the pivot element
            pivot_index = np.where(matrix[:,i] == pivot)[0][0]
            matrix[[i, pivot_index], :] = matrix[[pivot_index, i], :]
            # normalize the pivot row
            pivot = matrix[i,i]
            matrix[i] = matrix[i]/pivot
            # eliminate the elements in the current column in all other rows
            for j in range(n):
                if j != i:
                    factor = matrix[j,i]
                    matrix[j] = matrix[j] - factor*matrix[i]
    print("Number of pivot columns:", pivot_cols)
    print("Number of free columns:", free_cols)
    return matrix

# generate a randomly generated matrix
matrix = np.random.rand(5,6)
print("Original Matrix:")
print(matrix)

result = gaussian_elimination(matrix)
print("Matrix after Gaussian elimination:")
print(result)

# calculate the complete solution (particular solution + null space solution)
n = len(matrix)
particular_solution = result[:,:n]
null_space = result[:,n:]
print("Particular solution:")
print(particular_solution)
print("Null space solution:")
print(null_space)
