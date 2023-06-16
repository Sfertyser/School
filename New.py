number = 10
text = ""
# if number % 2 == 0:
#     text = "парним"
# else:
#     text = "не парним"
text = "парним" if number % 2 == 0 else "не парним"   # Тарнарний оператор
print(f"{number} є {text}")
