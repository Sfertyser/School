"""Оптимізація словника для зберігання даних:
Розглянемо ситуацію, коли у вас є словник з великим обсягом даних, які надають інформацію про студентів в університеті.
Кожен студент має унікальний ідентифікатор,
а атрибути включають оцінки різних предметів, дату народження, список курсів і т.д.
Зіткніться із завданням оптимізації цього словника, щоб забезпечити ефективний доступ та модифікацію даних."""

# from collections import namedtuple, default-dict
# Student = namedtuple("Student", ["Name", "DOB", "Grades"])
# grades = defaultsect(int)
# grades["Math"] = 0
# grades["Ecology"] = 0
# student_data = {
#     "ID1": Student("Петро", "01-01-2000", {"Language": 75, "Chemistry": 86, "Math": 72}),
#     "ID2": Student("Оксана", "25-08-2003", {"Biology": 93, "Ecology": 82, "History": 79}),
#     "ID3": Student("Дмитро", "12-11-1998", {"Information Technology": 96, "Physics": 88, "Geography": 91})
# }
# for studentID, student_info in student_data.items():
#     print(f"studentID: {studentID}")
#     print(f"Name:{student_info.Name}")
#     print(f"DOB:{student_info.DOB}")
#     print("Grades:")
#     for subject, grade in student_info.Grades.items():
#         print(f"    {subject}: {grade}")
#
# student_test = Student("Оксана", "25-08-2003", {"Biology": 93, "Ecology": 82, "History": 79})
# print(student_test[0])
# print(student_test.Name)
# print(grades["Law"])

"""Спростіть представлення точок у двовимірному просторі та обчисліть відстань між двома точками."""
# from collections import namedtuple
# import math
#
# Point = namedtuple("Point", ["x", "y"])
# point1 = Point(3, 4)
# point2 = Point(-3, 4)
#
#
# def calculate(p1, p2):
#     return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
#
#
# distance = calculate(point1, point2)
# print(distance)
