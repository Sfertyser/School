import string
import random
try:
    Task = int(input("Введіть номер завдання(1-5): "))
    if 0 < Task < 6:
        match Task:
            case 1:  # 1. Функція для перевірки, чи є рядок паліндромом
                def palindrome(a):
                    a = a.replace(" ", "").lower()  # Прибирає всі пробіли та робить текст маленьким.
                    return a == a[::-1]  # Перевіряє чи текст буде таким самим з його оберненою версією.

                input_string = input("Введіть слово яке ви хочете перевірити: ")
                if input_string.strip() == "" or "  " in input_string:
                    print("Ви ввели нічого, або ввели більше ніж 1 пробіл.")
                else:
                    if palindrome(input_string):
                        print(f"{input_string} є паліндромом.")
                    else:
                        print(f"{input_string} не є паліндромом.")
            case 2:  # 2. Функція для перевірки наявності елемента у списку
                def check_element(element, user_list):
                    return element in user_list

                user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                print(f"Лист: {user_list}")
                user_element = int(input("Введіть елемент який ви хочете найти: "))
                if check_element(user_element, user_list):
                    print(f"{user_element} знаходиться у списку.")
                else:
                    print(f"{user_element} не знаходиться у списку.")
            case 3:  # 3. Функція для перевірки входження підрядка в рядок
                def check_substring(substring, my_string):
                    return substring.lower() in my_string.lower()

                my_string = input("Введіть рядок: ")
                substring = input("Введіть підрядок: ")
                if check_substring(substring, my_string):
                    print(f"Підрядок {substring} знайдено у рядку {my_string}")
                else:
                    print(f"Підрядок {substring} не знайдено у рядку {my_string}")
            case 4:  # 4. Функція для створення випадкового пароля (import string)
                def generate_random_password(length=16):
                    characters = string.ascii_letters + string.digits  # Добавляє всі літери (Великі та малі) та числа.
                    password = "".join(random.choice(characters) for _ in range(length))  # Вибирає числа зі змінної
                    return password

                random_password = generate_random_password()
                print(f"Ваш випадковий пароль: {random_password}")
            case 5:  # 5. Функція для сортування списку слів за довжиною
                def sort_words(word_list):
                    return sorted(word_list, key=len)  # key=len означає сортування за довжиною кожного слова.


                # Приклад використання:
                words = ["Blueberry", "Banana", "Orange", "Watermelon", "Strawberry", "Apple", "Grape", "Pineapple"]
                sorted_words = sort_words(words)
                print(sorted_words)
    else:
        print("Помилка, ви ввели число не в діапазоні завдань.")
except ValueError as Error:
    print("Помилка, ви ввели текст або символи.")
except Exception as Error:
    print("Помилка, зв'яжіться з розробником програми.")
