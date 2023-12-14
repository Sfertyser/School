import random
"""Задача: Спортивний турнір
Напишіть програму для генерації розкладу спортивного турніру.
Кількість команд та результати матчів визначаються випадковим чином.
Кожен матч представлений словником з ключами:
"команда1", "команда2" та "результат".
Результат може бути виграшем однієї з команд або нічиєю."""
try:
    def generate_tournament_schedule(num_teams):
        teams = [f"Команда {i}" for i in range(1, num_teams + 1)]
        random.shuffle(teams)
        schedule = []  # Потрібний для зберігання розкладу матчів.
        while len(teams) > 1:
            matches = []
            for i in range(0, len(teams), 2):  # Формує пари команд для матчів.
                match = {
                    "команда1": teams[i],
                    "команда2": teams[i + 1],
                    "результат": None
                }
                while (match["результат"] is None  # Для переграння після нічиї.
                       or match["результат"] == "Нічия"):
                    match["результат"] = random.choice([teams[i], teams[i + 1],
                                                        "Нічия"])
                    if match["результат"] == "Нічия":
                        print(f"Нічия між {match["команда1"]}"
                              f" та {match["команда2"]}"
                              f". Матч було переграно.")
                        match["результат"] = random.choice([teams[i],
                                                            teams[i + 1]])
                matches.append(match)  # Додає для зміни щоб вивести можна було.
            schedule.append(matches)  # Додає список matches до schedule.
            winners = [match["результат"] for match in matches
                       if match["результат"]
                       != "Нічия"]  # Зберігає переможців.
            teams = winners
        return schedule


    num_teams = random.choice([4, 8, 16])
    print(f"Розклад спортивного турніру з {num_teams} команд:\n")
    tournament_schedule = generate_tournament_schedule(num_teams)
    round_num = 1
    for matches in tournament_schedule:
        print(f"\nЕтап {round_num}:")
        for match in matches:
            if match["результат"] == "Нічия":
                print(f"Нічия між {match["команда1"]} та {match["команда2"]}"
                      f". Матч було переграно.")
            print(f"{match["команда1"]} проти {match["команда2"]}:"
                  f" Переможець - {match["результат"]}")
            winner_team = match["результат"]
        round_num += 1
    print(f"\nВ цьому спортивному турнірі перемогла: {winner_team}")
except MemoryError as Error:
    print("Помилка, у вас нехватає пам'яті для запуску програми.")
except Exception as Error:
    print("Помилка, зв'яжіться з розробником програми.")
