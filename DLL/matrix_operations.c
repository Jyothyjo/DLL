// matrix_operations.c
#include "matrix_operations.h"

void matrix_addition(int* a, int* b, int* result, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i * cols + j] = a[i * cols + j] + b[i * cols + j];
        }
    }
}

void matrix_subtraction(int* a, int* b, int* result, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i * cols + j] = a[i * cols + j] - b[i * cols + j];
        }
    }
}

void matrix_multiplication(int* a, int* b, int* result, int rows_a, int cols_a,int rows_b, int cols_b) {
   // if (cols_a == rows_b) {
        for (int i = 0; i < rows_a; i++) {
            for (int j = 0; j < cols_b; j++) {
                result[i * cols_b + j] = 0;
                for (int k = 0; k < cols_a; k++) {
                    result[i * cols_b + j] += a[i * cols_a + k] * b[k * cols_b + j];
                }
            }
       // }
    }
    //else
      //  return 0;
}

void matrix_transpose(int* a, int* result, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[j * rows + i] = a[i * cols + j];
        }
    }
}
