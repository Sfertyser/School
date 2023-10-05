# Wrong program
# def calculate_expression(expression):
#     stack = []
#     operators = {"+", "-", "*", "/"}
#     current_number = ""
#
#     def perform_operation(operator, operand1, operand2):
#         if operator == "+":
#             return operand1 + operand2
#         elif operator == "-":
#             return operand1 - operand2
#         elif operator == "*":
#             return operand1 * operand2
#         elif operator == "/":
#             if operand2 == 0:
#                 raise ValueError("Дiлення на 0!")
#             return operand1 / operand2
#
#     for char in expression:
#         if char.isdigit() or char == "-":
#             current_number += char
#         elif char in operators or char.isspace():
#             if current_number:
#                 stack.append(int(current_number))
#                 current_number = ""
#             if char in operators:
#                 stack.append(char)
#
#     if current_number:
#         stack.append(int(current_number))
#
#     while len(stack) > 1:
#         operand2 = stack.pop()
#         operator = stack.pop()
#         operand1 = stack.pop()
#         result = perform_operation(operand1, operator, operand2)
#         stack.append(result)
#
#     return stack[0] if stack else "Некорректний вираз!"
#
#
# # Приклади використання функції
# expression1 = "3 + 5 * 2"
# result1 = calculate_expression(expression1)
# print("Result 1:", result1)
#
# expression2 = "8 / 0"
# result2 = calculate_expression(expression2)
# print("Result 2:", result2)


# Right program
def calculate_expression(expression):
    stack = []
    operators = {"+", "-", "*", "/"}
    current_number = ""

    def perform_operation(operator, operand1, operand2):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            if operand2 == 0:
                print("Дiлення на 0!")  # Проблема була в raise ZeroDivision
                exit()
            return operand1 / operand2

    def precedence(operator):
        if operator in ("+", "-"):
            return 1
        elif operator in ("*", "/"):
            return 2
        return 0

    for char in expression:
        if (char.isdigit() or char == "." or
        (char == "-" and (not current_number or (stack and stack[-1] in operators)))):
            current_number += char
        elif char in operators or char.isspace():
            if current_number:
                stack.append(int(current_number))
                current_number = ""
            if char in operators:
                while (stack and stack[-1] in operators and
                       precedence(stack[-1]) >= precedence(char)):
                    operand2 = stack.pop()
                    operator = stack.pop()
                    operand1 = stack.pop()
                    result = perform_operation(operator, operand1, operand2)
                    stack.append(result)
                stack.append(char)

    if current_number:
        stack.append(int(current_number))

    while len(stack) > 1:
        operand2 = stack.pop()
        operator = stack.pop()
        operand1 = stack.pop()
        result = perform_operation(operator, operand1, operand2)
        stack.append(result)

    return stack[0] if stack else "Некорректний вираз!"


expression1 = "3 + 5 * 2"
result1 = calculate_expression(expression1)
print(f"{expression1} буде: {result1}")

expression2 = "8 / 0"
result2 = calculate_expression(expression2)
print(f"{expression2} буде: {result2}")
