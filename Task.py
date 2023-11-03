# Поліморфізм
# class Animal:
#     def speak(self):
#         return ""
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Мяу"
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Гав"
#
#
# cat = Cat()
# dog = Dog()
#
# print(cat.speak())
# print(dog.speak())


# def animal_sound(animal):
#     return animal.speak()


# cat = Cat()
# dog = Dog()
# print(animal_sound(cat))
# print(animal_sound(dog))


# class My_number:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         if isinstance(other, My_number):
#             return My_number(self.value + other.value)
#         else:
#             return My_number(self.value + other)
#
#     def __str__(self):
#         return str(self.value)
#
#
# num1 = My_number(25)
# num2 = My_number(35)
# result = num1 + num2
# print(result)

"""Створіть функцію get_area, яка приймає об'єкт фігури (як екземпляр класу Shape)
та повертає площу цієї фігури, використовуючи поліморфізм."""


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


def get_area(Shape):
    return Shape.area()
#
#
# rectangle = Rectangle(10, 8)
# circle = Circle(30)
# print(get_area(rectangle))
# print(get_area(circle))


shapes = [Rectangle(4, 5), Circle(30)]
for shape in shapes:
    print(shape.area())
