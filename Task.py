try:
    Task = int(input("Введіть номер завдання(1-9): "))
    if 0 < Task < 10:
        match Task:
            case 1:
                words = ["apple", "banana", "grape", "pear", "kiwi", "orange"]
                grouped_by_length = {}
                for word in words:
                    lenth = len(word)
                    if lenth in grouped_by_length:
                        grouped_by_length[lenth].append(word)
                    else:
                        grouped_by_length[lenth] = [word]
                print(grouped_by_length)
            case 2:
                text_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
                text = "three"
                number = text_numbers.get(text, "unknown")
                print(number)
            case 3:
                elements = [1, 2, 3, 2, 1, 3, 1, 2, 4, 5, 1]
                count_dict = {}
                for el in elements:
                    if el in count_dict:
                        count_dict[el] += 1
                    else:
                        count_dict[el] = 1
                print(count_dict)
            case 4:
                synonyms = {
                    "happy": ["joyful", "content", "pleased"],
                    "sad": ["unhappy", "miserable", "gloomy"],
                    "angry": ["irate", "furious", "enraged"]
                }
                word = "happy"
                end = synonyms.get(word, [])
                print(end)
            case 5:
                text = "hello world"
                char_count = {}
                for t in text:
                    if t in char_count:
                        char_count[t] += 1
                    else:
                        char_count[t] = 1
                print(char_count)
            case 6:
                # 1 варіант
                student_info = {
                    "Аліса": {"age": 20, "grades": [85, 90, 78]},
                    "Боб": {"age": 22, "grades": [92, 88, 95]}
                }
                print("Варіанти: Аліса, Боб")
                student_name = str(input("Введіть ім'я студента: "))
                correct_name = student_name.capitalize()
                if correct_name in student_info:
                    student = student_info[correct_name]
                    age = student["age"]
                    grades = student["grades"]
                    average_grade = sum(grades) / len(grades)
                    print(f"Ім'я: {correct_name}")
                    print(f"Вік: {age}")
                    print(f"Оцінки: {grades}")
                else:
                    print(f"Студента з ім'ям {student_name} не знайдено.")
                # 2 варіант
                student_info = {
                    "Аліса": {"age": 20, "grades": [85, 90, 78]},
                    "Боб": {"age": 22, "grades": [92, 88, 95]}
                }
                student_info_alice = {
                    "Аліса": student_info["Аліса"]
                }
                student_info_bob = {
                    "Боб": student_info["Боб"]
                }
                print()
                print(student_info_alice)
                print(student_info_bob)
            case 7:
                grades = {"math": 90, "history": 85, "biology": 78}
                total = sum(grades.values())
                average = int(total / len(grades))
                print(f"Оцінки: {grades}")
                print(f"Сума: {total}")
                print(f"Середнє значення: {average}")
            case 8:
                menu = {
                    "burger": 8.99,
                    "pizza": 12.99,
                    "salad": 6.49,
                    "pasta": 10.49
                }
                order = ["pizza", "salad"]
                total_price = 0
                for item in order:
                    if item in menu:
                        total_price += menu[item]
                print(f"Меню: {menu}")
                print(f"Ваш заказ: {order}")
                print(f"Сума заказу: {total_price}")
            case 9:
                translations = {
                    "hello": "привіт",
                    "world": "світ",
                    "python": "пітон"
                }
                print("Варіанти: hello, world, python")
                word = input("Введіть слово яке потрібно перекласти: ")
                correct_word = word.lower()
                if correct_word in translations:
                    translation = translations[correct_word]
                    print(f"Переклад слова {correct_word} - {translation}")
                else:
                    print(f"Слово {correct_word} не знайдено у словнику перекладів.")
    else:
        print("Помилка, ви ввели число не в діапазоні завдань.")
except ValueError as Error:
    print("Помилка, ви ввели текст або символи.")
except Exception as Error:
    print("Помилка, зв'яжіться з розробником програми.")
