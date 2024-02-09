# Напишіть програму, яка приймає матрицю та номер рядка або стовпця і знаходить
# суму всіх елементів у цьому рядку або стовпці.
# matrix = [
#           [1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]
#          ]


# row_index = 1
# column_index = 2
# sum_of_row = sum(matrix[row_index])
# print(f"Сума елементів у рядку: {sum_of_row}")
# sum_of_column = sum(row[column_index] for row in matrix)
# print(f"Сума елементів у стовбці: {sum_of_column}")


# def sum_matrix(matrix, index, axis="row"):
#     if axis == "row":
#         return sum(matrix[row_index])
#     elif axis == "column":
#         return sum(row[column_index] for row in matrix)
#
#
# print(f"Сума елементів у рядку: {sum_matrix(matrix, row_index)}")
# print(f"Сума елементів у стовбці: "
#       f"{sum_matrix(matrix, column_index, axis="column")}")


"""Реалізуйте функцію, яка приймає матрицю і повертає її транспоновану версію,
тобто матрицю, в якій рядки стають стовпцями і навпаки."""


def function():
    return [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(
        matrix1[0]))]


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transported_matrix = function()
for row in transported_matrix:
    print(row)

# Напишіть програму, яка приймає дві матриці і виконує їх множення за правилом
# матричного множення, якщо це можливо, або повертає помилку в іншому випадку.
