import random
select = int(input("Введіть номер завдання: "))
if 0 < select < 5:
    match select:
        case 1:
            """Створіть матрицю чисел. Знайдіть максимальний елемент
            в кожному рядку та виведіть результат."""
            rows = int(input("Введіть кількість рядків: "))
            cols = int(input("Введіть кількість стовпців: "))
            min_value = int(input("Введіть мінімальне значення: "))
            max_value = int(input("Введіть максимальне значення: "))
            while min_value == max_value:
                max_value = int(input("Введіть максимальне значення: "))
            matrix = []
            for _ in range(rows):
                row = [random.randint(min_value, max_value)
                       for _ in range(cols)]
                matrix.append(row)
            print("Згенерована матриця:")
            for row in matrix:
                print(row)
            print("\nМаксимальні елементи в кожному рядку:")
            for i, row in enumerate(matrix, 1):
                max_in_row = max(row)
                print(f"Рядок {i}: {max_in_row}")

        case 2:
            """Створіть дві матриці однакового розміру та додайте їх,
            створюючи нову матрицю із результатом."""
            rows = int(input("Введіть кількість рядків: "))
            cols = int(input("Введіть кількість стовпців: "))
            min_value = int(input("Введіть мінімальне значення: "))
            max_value = int(input("Введіть максимальне значення: "))
            matrix1 = []
            for _ in range(rows):
                row = [random.randint(min_value, max_value)
                       for _ in range(cols)]
                matrix1.append(row)
            print("Перша матриця:")
            for row in matrix1:
                print(row)
            matrix2 = []
            for _ in range(rows):
                row = [random.randint(min_value, max_value)
                       for _ in range(cols)]
                matrix2.append(row)
            print("\nДруга матриця:")
            for row in matrix2:
                print(row)

            result_matrix = []
            for i in range(rows):
                result_row = [matrix1[i][j] + matrix2[i][j]
                              for j in range(cols)]
                result_matrix.append(result_row)
            print("\nРезультат додавання матриць:")
            for row in result_matrix:
                print(row)

        case 3:
            """Створіть дві матриці із відповідними розмірами та перемножте їх,
            створюючи нову матрицю із результатом"""
            rows1 = int(input("Введіть кількість рядків для обох матриць: "))
            cols1 = int(input("Введіть кількість стовпців для обох матриць: "))
            rows2 = rows1
            cols2 = cols1

            matrix1 = [[0] * cols1 for _ in range(rows1)]
            matrix2 = [[0] * cols2 for _ in range(rows2)]

            print("Введіть елементи першої матриці:")
            for i in range(rows1):
                for j in range(cols1):
                    matrix1[i][j] = int(input(f"Елемент [{i + 1},{j + 1}]: "))

            print("Введіть елементи другої матриці:")
            for i in range(rows2):
                for j in range(cols2):
                    matrix2[i][j] = int(input(f"Елемент [{i + 1},{j + 1}]: "))

            result_matrix = [[0] * cols2 for _ in range(rows1)]

            for i in range(rows1):
                for j in range(cols2):
                    for k in range(cols1):
                        result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

            print("\nРезультат множення матриць:")
            for row in result_matrix:
                print(row)

        case 4:
            """Створіть квадратну матрицю та визначте,
            чи вона є симетричною(рівною своєму транспонованому варіанту)."""
            n = int(input("Введіть розмір квадратної матриці: "))
            matrix = [[random.randint(1, 10) for _ in range(n)]
                      for _ in range(n)]
            print("Квадратна матриця:")
            for row in matrix:
                print(row)
            transposed_matrix = [[matrix[j][i] for j in range(n)]
                                 for i in range(n)]
            is_symmetric = True
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] != transposed_matrix[i][j]:
                        is_symmetric = False
                        break
            if is_symmetric:
                print("\nМатриця є симетричною.")
            else:
                print("\nМатриця не є симетричною.")

else:
    print("Помилка, ви ввели неправильний номер завдання")
