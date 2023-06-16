print("Введіть число:")
number = int(input())
print("Введіть місяць:")
month = (input())
print("Введіть рік:")
year = int(input())
if 21 <= number <= 31 and month == 'березень' or 1 <= number <= 20 and month == 'квітень':
    print("По гороскопу ви Овен.")
elif 21 <= number <= 30 and month == 'квітень' or 1 <= number <= 20 and month == 'травень':
    print("По гороскопу ви Телець.")
elif 21 <= number <= 31 and month == 'травень' or 1 <= number <= 20 and month == 'червень':
    print("По гороскопу ви Близнюки.")
elif 22 <= number <= 30 and month == 'червень' or 1 <= number <= 22 and month == 'липень':
    print("По гороскопу ви Рак.")
elif 23 <= number <= 31 and month == 'липень' or 1 <= number <= 23 and month == 'серпень':
    print("По гороскопу ви Лев.")
elif 24 <= number <= 31 and month == 'серпень' or 1 <= number <= 23 and month == 'вересень':
    print("По гороскопу ви Діви.")
elif 24 <= number <= 30 and month == 'вересень' or 1 <= number <= 23 and month == 'жовтень':
    print("По гороскопу ви Терези.")
elif 24 <= number <= 31 and month == 'жовтень' or 1 <= number <= 22 and month == 'листопад':
    print("По гороскопу ви Скорпіон.")
elif 23 <= number <= 30 and month == 'листопад' or 1 <= number <= 21 and month == 'грудень':
    print("По гороскопу ви Стрілець.")
elif 22 <= number <= 31 and month == 'грудень' or 1 <= number <= 20 and month == 'січень':
    print("По гороскопу ви Козеріг.")
elif 21 <= number <= 31 and month == 'січень' or 1 <= number <= 18 and month == 'лютий':
    print("По гороскопу ви Водолій.")
elif 19 <= number <= 28 and month == 'лютий' or 1 <= number <= 20 and month == 'березень':
    print("По гороскопу ви Риби.")
