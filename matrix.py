import ctypes
import numpy as np

# Load the DLL
matrix_dll = ctypes.cdll.LoadLibrary("C:/Users/Jyothi/source/repos/DLL/x64/Debug/DLL.dll")

# Define the function prototypes
matrix_addition = matrix_dll.matrix_addition
matrix_addition.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
matrix_addition.restype = None

matrix_subtraction = matrix_dll.matrix_subtraction
matrix_subtraction.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
matrix_subtraction.restype = None

matrix_multiplication = matrix_dll.matrix_multiplication
matrix_multiplication.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int]
matrix_multiplication.restype = None

matrix_transpose = matrix_dll.matrix_transpose
matrix_transpose.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
matrix_transpose.restype = None

# Read matrix dimensions from the user
rows_a = int(input("Enter the number of rows for matrix A: "))
cols_a = int(input("Enter the number of columns for matrix A: "))
rows_b = int(input("Enter the number of rows for matrix B: "))
cols_b = int(input("Enter the number of columns for matrix B: "))

# Read matrix A from the user
print("Enter matrix A (row-wise):")
a = np.zeros((rows_a, cols_a), dtype=np.int32)
for i in range(rows_a):
    row = input().split()
    a[i] = [int(num) for num in row]

# Read matrix B from the user
print("Enter matrix B (row-wise):")
b = np.zeros((rows_b, cols_b), dtype=np.int32)
for i in range(rows_b):
    row = input().split()
    b[i] = [int(num) for num in row]

# Create output matrices
result = np.zeros((rows_a, cols_a), dtype=np.int32)

# Get operation choice from the user
print("Select matrix operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")
choice = int(input("Enter your choice (1-4): "))

# Perform the selected operation
if choice == 1:
    matrix_addition(a.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                    b.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                    result.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                    ctypes.c_int(rows_a),
                    ctypes.c_int(cols_a))
    print("Matrix Addition:")
elif choice == 2:
    matrix_subtraction(a.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                       b.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                       result.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                       ctypes.c_int(rows_a),
                       ctypes.c_int(cols_a))
    print("Matrix Subtraction:")
elif choice == 3:
    if cols_a != rows_b:
        print("Error: Invalid matrix dimensions for multiplication")
    else:
        result = np.zeros((rows_a, cols_b), dtype=np.int32)
        matrix_multiplication(a.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                              b.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                              result.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                              ctypes.c_int(rows_a),
                              ctypes.c_int(rows_b),
                              ctypes.c_int(cols_a),
                              ctypes.c_int(cols_b))
        print("Matrix Multiplication:")
elif choice == 4:
    result = np.zeros((cols_a, rows_a), dtype=np.int32)
    matrix_transpose(a.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                     result.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                     ctypes.c_int(rows_a),
                     ctypes.c_int(cols_a))
    print("Matrix Transpose:")
else:
    print("Invalid choice")
print(result)