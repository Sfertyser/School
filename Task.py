import random
"""Задача: Комерційна нерухомість
Напишіть програму для генерації списку комерційних приміщень
на земельній ділянці. Кожне приміщення представлено словником з ключами: 
"площа", "тип" та "ціна". Тип приміщення може бути, наприклад: "офіс", 
"магазин", "ресторан". Площа та ціна генеруються випадковим чином.
Кількість приміщень, їхні характеристики також визначаються випадковим чином."""


def buildings_function(num_properties):
    property_types = ["офіс", "магазин", "ресторан"]
    buildings = [
        {
            "площа": random.randint(100, 1000),
            "тип": random.choice(property_types),
            "ціна": random.randint(1000, 99999)
        }
        for _ in range(num_properties)
    ]
    return buildings


def buildings_info(properties):
    for i, prop in enumerate(properties, 1):
        print(f"{i}. Інформація про комерційні приміщеня: Тип - "
              f"{prop["тип"]}, Площа - {prop["площа"]}, Ціна - ${prop["ціна"]}")


def square(properties):
    return sum(prop["площа"] for prop in properties)


def value(properties):
    return sum(prop["ціна"] for prop in properties)


# Генеруємо список комерційних приміщень
# Виводимо інформацію про приміщення
# Обчислюємо та виводимо загальну площу та вартість
num_properties = 5
comercial_buildings = buildings_function(num_properties)
buildings_info(comercial_buildings)
square_all = square(comercial_buildings)
value_all = value(comercial_buildings)
print(f"Загальна площа: {square_all}, загальна ціна: {value_all}")
