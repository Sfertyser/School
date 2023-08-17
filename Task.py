import random
try:
    Task = int(input("Введіть номер завдання(1-6): "))
    if 0 < Task < 7:
        match Task:
            case 1:  # Порахувати кiлькiсть чисел зI знаком "-"
                List = [random.randint(-100, 100) for _ in range(10)]
                print(f"Згенерований лист: {List}")
                negative_count = sum(1 for num in List if num < 0)
                if negative_count == 0:
                    print("Негативних чисел немає.")
                else:
                    print(f"Кількість негативних чисел: {negative_count}")
            case 2:  # Видалити всi елементи списку, що дiляться на 3 без залишку
                List = [random.randint(-100, 100) for _ in range(10)]
                print(f"Згенерований лист: {List}")
                final_list = [num for num in List if num % 3 != 0]
                if final_list == 0:
                    print("В листі немає елементів які дiляться на 3 без залишку.")
                else:
                    print(f"Лист без елементів які дiляться на 3 без залишку: {final_list}")
            case 3:  # Зробити сортування списку без метода sort
                List = [random.randint(-100, 100) for _ in range(10)]
                print(f"Згенерований лист: {List}")
                e = len(List)  # Змінна для довжини списка.
                for i in range(e):  # Потрібно для створення циклу.
                    for j in range(0, e - i - 1):  # (0, n - i - 1) Робить щоб через кожний цикл він переходив на 2 ел.
                        if List[j] > List[j + 1]:  # Якщо минулий елемент більший за наступний.
                            List[j], List[j + 1] = List[j + 1], List[j]  # Змінює їх місцями.
                print(f"Посортований список: {List}")
            case 4:  # Написати список задом наперед
                List = [random.randint(-100, 100) for _ in range(10)]
                print(f"Згенерований лист: {List}")
                reversed_list = List[::-1]
                print(f"Список задом наперед: {reversed_list}")
            case 5:  # Створити новий список, у якому кожен елемент - конкатенація рядка
                words = ["apple", "banana", "cherry"]
                print(f"Данні слова: {words}")
                suffix = " pie"
                print(f"Суфікс: {suffix}")
                new_list = [word + suffix for word in words]
                print(f"Новий список: {new_list}")
            case 6:  # Знайти спільні елементи у двох списках.
                List1 = [random.randint(-30, 30) for _ in range(10)]
                List2 = [random.randint(-30, 30) for _ in range(10)]
                print(f"Перший згенерований лист: {List1}")
                print(f"Другий згенерований лист: {List2}")
                same_elements = []
                for e in List1:
                    if e in List2:
                        same_elements.append(e)
                if not same_elements:
                    print(f"Спільних елементів немає.")
                else:
                    print(f"Спільні елементи: {same_elements}")
    else:
        print("Помилка, ви ввели число не в діапазоні завдань.")
except ValueError as Error:
    print("Помилка, ви ввели текст або символи.")
except Exception as Error:
    print("Помилка, зв'яжіться з розробником програми.")
