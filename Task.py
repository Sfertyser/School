import math
try:
    choice = int(input("Введіть номер завдання(1-5): "))
    while choice <= 0 or choice >= 6:
        choice = int(input("Помилка, введіть номер завдання(1-5): "))
    match choice:

        case 1:  # Задача про об'єм кулі.
            """ Обчисліть об'єм кулі з радіусом 34. """
            radius = 34
            volume = (4 * math.pi * radius ** 3) / 3
            print(f"Об'єм кулі з радіусом {radius} дорівнює: {volume}")

        case 2:  # Задача з геометричною прогресією.
            """ Знайдіть суму перших 5 членів геометричної прогресії
             з першим членом 3 і знаменником 2. """
            first_term = 3
            common_ratio = 2
            num_terms = 5
            sum_gp = (first_term * (1 - common_ratio ** num_terms)
                      / (1 - common_ratio))
            print(f"Сума перших {num_terms}"
                  f" членів геометричної прогресії: {int(sum_gp)}")

        case 3:  # Задача про об'єм циліндра.
            """ Обчисліть об'єм циліндра з радіусом основи 5 і висотою 15. """
            radius = 5
            height = 15
            base_area = math.pi * radius ** 2
            volume = base_area * height
            print(f"Об'єм циліндра з радіусом основи: {radius}, і висотою: "
                  f"{height}, дорівнює: {volume}")

        case 4:  # Задача про використання константи π.
            """ Знайдіть довжину кола, якщо радіус дорівнює 7. """
            radius = 7
            circumference = 2 * math.pi * radius
            print(f"Довжина кола з радіусом: {radius},"
                  f" дорівнює: {circumference}")

        case 5:  # Задача з трикутником і сінусом.
            """ Знайдіть довжину сторони прямокутного трикутника,
             якщо вам відомі кут 30 градусів і гіпотенуза рівна 5. """
            angle = 30
            hypotenuse = 5
            angle_rad = math.radians(angle)
            side = hypotenuse * math.sin(angle_rad)
            print(f"Довжина сторони прямокутного трикутника"
                  f" при куті {angle} градусів та гіпотенузі {hypotenuse} "
                  f"градусів, дорівнює {round(side, 1)}")

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
