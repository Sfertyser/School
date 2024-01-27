"""Сума елементiв матрицi (построково)"""

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in matrix:
#     row_sum = sum(row)
#     print(f"Сума елементiв строки {row}: {row_sum}")

"""Множення на число"""
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# factor = 2
#
# result_matrix = [[element * factor for element in row] for row in matrix]
#
# print("Помножена матриця:", result_matrix)

"""Пошук min елементу у кожному стовбцi"""

# matrix = [
#     [11, -2, 34],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for j in range(len(matrix[0])):
#     column = [matrix[i][j] for i in range(len(matrix))]
#     min_element = min(column)
#     print(f"Мiнiмальний елемент у стовпцi {j + 1}: {min_element}")

"""Пошук середнього значення ел-тiв у матрицi"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# flat_row = [element for row in matrix for element in row]
# average = sum(flat_row) / len(flat_row)
#
# print(average)

"""Пошук додатнiх елементiв у матрицi"""

# matrix = [
#     [-1, 2, 3],
#     [4, -5, 6],
#     [-7, -8, 9]
# ]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] > 0:
#             print(f"Додатнiй елемент {matrix[i][j]}, позицiя ({i + 1}, "
#                   f"{j + 1})")

"""Транспонування матриці"""
"""Створіть матрицю та транспонуйте її, помінявши місцями рядки і стовпці,
 створюючи нову матрицю."""

# V1
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix2 = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]
# for i in range(3):
#     for j in range(3):
#         matrix2[i][j] = matrix1[j][i]
#
# for row in matrix2:
#     print(row)

# V2
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix2 = [[matrix1[j][i] for j in range(len(matrix1))]
#            for i in range(len(matrix1[0]))]
#
# for row in matrix2:
#     print(row)
