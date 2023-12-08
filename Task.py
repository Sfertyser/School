from collections import defaultdict
import random
import math
# Дано звіт продаж за тиждень працівників компанії у такому форматі
# Може бути таке що якись працівник робив декілька продаж на тиждень як на приклад "Alisa"
# Задача:
# створити множину робітників що зазначено у звіті продаж - вивести на єкран створити словник ключем якого буде ім'я
# працівника, а значенням сума виторгу ним за тиждень що зазначена  ключем "price" у звіті. Словник  надрукувати.
# data = [
#  {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
#  {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
#  {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
#  {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
#  {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
#  {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
# ]
# workers = set(entry["name"] for entry in data)
# sales_sum = {}
# for entry in data:
#  name = entry["name"]
#  price = entry["price"]
#  if name in sales_sum:
#   sales_sum[name] += price
#  else:
#   sales_sum[name] = price
#
# print(f"Множина робітників: {workers}")
# print("Сума виторгу за тиждень за кожного працівника: ")
# for worker, sales in sales_sum.items():
#  print(f"{worker}: {sales}")

# v2
# data = [
#  {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
#  {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
#  {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
#  {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
#  {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
#  {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
# ]
# workers = set(entry["name"] for entry in data)
# sales_sum = default dict(int)
# for entry in data:
#  sales_sum[entry["name"]] += entry["price"]
# print(f"Множина робітників: {workers}")
# print("Сума виторгу за тиждень за кожного працівника: ")
# for worker, sales in sales_sum.items():
#  print(f"{worker}: {sales}")

# Задача: Розподіл точок на площині
# Створіть програму, яка генерує список точок на площині. Кожна точка представлена словником з ключами "x" та "y",
# що вказують координати точки. Кількість точок та їхні координати визначаються випадковим чином.
# Виведіть:
# 1. Кількість унікальних значень x та y у згенерованому списку точок.
# 2. Всі точки, які знаходяться в першій чверті (x та y обидва додатні).
# 3. Відстань між першою та останньою точкою у списку.
# Приклад виводу:
# Кількість унікальних значень x: 8
# Кількість унікальних значень y: 7
# Точки в першій чверті:
# {"x": 3, "y": 5}
# {"x": 2, "y": 4}
# {"x": 4, "y": 3}
# Відстань між першою та останньою точкою: 5.0
# У цій задачі вам слід розглянути генерацію списку точок та виконання різних операцій над ним.
# dots = [{"x": random.randint(-10, 10), "y": random.randint(-10, 10)} for _ in range(10)]
# unique_x_value = len(set(dot["x"] for dot in dots))
# unique_y_value = len(set(dot["y"] for dot in dots))
# points_in_first_quadrant = [dot for dot in dots if dot["x"] > 0 and dot["y"] > 0]
# print("Точки в першій чверті: ")
# for dot in points_in_first_quadrant:
#     print(dot)
# distance = math.sqrt((dots[0]["x"] - dots[-1]["x"])**2 + (dots[0]["y"] - dots[-1]["y"])**2)
# print(f"\n Відстань між першою та останію точкою: {distance:.4f}")
