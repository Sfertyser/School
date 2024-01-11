""" Base for programs """
# try:
#     choice = int(input("Введіть номер завдання(1-5): "))
#     while choice <= 0 or choice >= 6:
#         choice = int(input("Помилка, введіть номер завдання(1-5): "))
#     match choice:
#         case 1:
#             pass
#         case 2:
#             pass
#         case 3:
#             pass
#         case 4:
#             pass
#         case 5:
#             pass
# except MemoryError as e:
#     print(f"{str(e)}, у вас недостатньо оперативної пам'яті щоб запустити цю "
#           "програму.")
# except FileNotFoundError as e:
#     print(f"{str(e)}, програма не може отримати доступ до файлу.")
# except OverflowError as e:
#     print(f"{str(e)}, межу допустимих значень було перевищено.")
# except PermissionError as e:
#     print(f"{str(e)}, у вас немає необхідних прав доступу для виконання "
#           f"певної операції")
# except TypeError as e:
#     print(f"{str(e)}, перевірте правильність типів даних.")
# except ValueError as e:
#     print(f"{str(e)}, перевірте правильність введених даних.")
# except Exception as e:
#     print(f"Виникла помилка: {str(e)}")
