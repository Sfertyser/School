try:
    choice = int(input("Введіть номер завдання(1-5): "))
    if 0 < choice < 6:
        match choice:
            case 1:  # Операції над множинами:
                set1 = {1, 2, 3, 4, 5}
                set2 = {4, 5, 6, 7, 8}
                print("Об'єднання множин:", set1.union(set2))
                print("Перетин чисел у множинах:", set1.intersection(set2))
                print("Різниця чисел у першій множині від другої:", set1.difference(set2))
                print("Різниця чисел у другої множини від першої:", set2.difference(set1))
            case 2:  # Перевірка включеності:
                set3 = {1, 2, 3, 4}
                set4 = {1, 2, 3, 4, 5, 6, 7, 8}
                if set3.issubset(set4):
                    print("Так, одна множина є підмножиною іншої.")
                else:
                    print("Ні, одна множина не є підмножиною іншої.")
            case 3:  # Видалення дублікатів:
                list_wd = [1, 1, 2, 3, 4, 4, 5, 5]
                print(f"Список з дублікатами: {list_wd}")
                print("Множина:", set(list_wd))
            case 4:  # Математичні операції:
                math_students = {"Abby", "Bob", "Max", "Michael"}
                physics_students = {"Bob", "James", "Michael", "Grace"}
                print("Студенти, які вивчають лише математику:", math_students.difference(physics_students))
                print("Студенти, які вивчають лише фізику:", physics_students.difference(math_students))
                print("Студенти, які вивчають обидва предмети:", math_students.intersection(physics_students))
            case 5:  # Конвертація типів:
                mixed_set = {1, 4, 7, "hello"}
                print("Множина: ", mixed_set)
                converted_list = list(mixed_set)
                print("Конвертована множина у список:", converted_list)
    else:
        print("Помилка, ви ввели число не в діапазоні завдань.")
except Exception as Error:
    print("Помилка, зв'яжіться з розробником програми.")
