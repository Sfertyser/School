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


# def function():
#     return [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(
#         matrix1[0]))]
#
#
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transported_matrix = function()
# for row in transported_matrix:
#     print(row)

# Напишіть програму, яка приймає дві матриці і виконує їх множення за правилом
# матричного множення, якщо це можливо, або повертає помилку в іншому випадку.

"""Напишіть програму, яка приймає дві матриці і виконує їх множення за правилом
матричного множення, якщо це можливо, або повертає помилку в іншому випадку."""

matrix1 = [
          [1, 2, 3],
          [4, 5, 6],
          ]
matrix2 = [
          [7, 8],
          [9, 10],
          [11, 12]
          ]

rows1 = len(matrix1)
cols1 = len(matrix1[0])
rows2 = len(matrix2)
cols2 = len(matrix2[0])

print(f"Перша матриця: {matrix1}")
print(f"Друга матриця: {matrix2}")

if cols1 != rows2:
    print("Помилка, неможливо виконати множення, розміри матриць не "
          "відповідають умовам матричного множення")
else:
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]  # Створює
    # нову матрицю
    for i in range(rows1):  # проходить по кожному рядку першої матриці
        for j in range(cols2):  # проходить по кожному стовпцю другої матриці
            for k in range(cols1):  # проходить по минулим
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    print("Результат множення матриць: ")
    for row in result:
        print(row)
