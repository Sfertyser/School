import random
try:
    choice = int(input("Введіть номер завдання(1-4): "))
    while choice <= 0 or choice >= 5:
        choice = int(input("Помилка, введіть номер завдання(1-4): "))
    match choice:
        case 1:
            """Створіть матрицю чисел. Знайдіть максимальний елемент
            в кожному рядку та виведіть результат."""
            rows = int(input("Введіть кількість рядків: "))
            cols = int(input("Введіть кількість стовпців: "))
            min_value = int(input("Введіть мінімальне значення: "))
            max_value = int(input("Введіть максимальне значення: "))
            matrix = []
            while min_value == max_value:
                max_value = int(input("Помилка, мінімальне число дорівнювало "
                                      "максимальному. Введіть максимальне "
                                      "значення: "))

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
            matrix2 = []
            result_matrix = []

            for _ in range(rows):
                row = [random.randint(min_value, max_value)
                       for _ in range(cols)]
                matrix1.append(row)
            print("Перша матриця:")

            for row in matrix1:
                print(row)

            for _ in range(rows):
                row = [random.randint(min_value, max_value)
                       for _ in range(cols)]
                matrix2.append(row)
            print("\nДруга матриця:")
            for row in matrix2:
                print(row)

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
            matrix1 = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            print(f"Перша матриця:")
            for row in matrix1:
                print(row)
            matrix2 = [
                [9, 8, 7],
                [6, 5, 4],
                [3, 2, 1]
            ]
            print(f"Друга матриця:")
            for row in matrix2:
                print(row)
            result_matrix = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]

            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

            print("Результуюча матриця:")
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


except MemoryError as e:
    print(f"{str(e)}, у вас недостатньо оперативної пам'яті щоб запустити цю "
          "програму.")
except FileNotFoundError as e:
    print(f"{str(e)}, програма не може отримати доступ до файлу.")
except OverflowError as e:
    print(f"{str(e)}, межу допустимих значень було перевищено.")
except PermissionError as e:
    print(f"{str(e)}, у вас немає необхідних прав доступу для виконання "
          f"певної операції")
except TypeError as e:
    print(f"{str(e)}, перевірте правильність типів даних.")
except ValueError as e:
    print(f"{str(e)}, перевірте правильність введених даних.")
except Exception as e:
    print(f"Виникла помилка: {str(e)}")
