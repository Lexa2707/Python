#Напиши функцию safe_divide, которая принимает два аргумента: a и b. Функция должна пытаться делить a на b и возвращать результат. Если произойдет ошибка деления на ноль (ZeroDivisionError), функция должна возвращать None вместо возникновения исключения. Продемонстрируй работу функции на нескольких примерах, включая деление на ноль.

def safe_divide(a, b):

    try:
        return a / b
    except ZeroDivisionError:
        return None

# Примеры использования
print(safe_divide(10, -2))
print(safe_divide(8, 4))
print(safe_divide(9995, 0))
print(safe_divide(0, 99995))
print(safe_divide(4.588, 299))
print(safe_divide(10, 3))
print(safe_divide(7, 0))