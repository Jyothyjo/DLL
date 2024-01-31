// matrix_operations.h

#ifndef MATRIX_OPERATIONS_H
#define MATRIX_OPERATIONS_H

#ifdef _MSC_VER
#ifdef MATRIX_EXPORTS
#define MATRIX_API __declspec(dllexport)
#else
#define MATRIX_API __declspec(dllimport)
#endif
#else
#define MATRIX_API extern
#endif

#ifdef __cplusplus
extern "C" {
#endif

    MATRIX_API void matrix_addition(int* a, int* b, int* result, int rows, int cols);
    MATRIX_API void matrix_subtraction(int* a, int* b, int* result, int rows, int cols);
    MATRIX_API void matrix_multiplication(int* a, int* b, int* result, int rows_a, int cols_a,int rows_b,int cols_b);
    MATRIX_API void matrix_transpose(int* a, int* result, int rows, int cols);

#ifdef __cplusplus
}
#endif

#endif // MATRIX_OPERATIONS_H

