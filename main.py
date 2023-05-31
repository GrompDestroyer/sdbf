#Введение в пузон
#Задание на 3
#int
import sys

value = input("Введите целое число: ")
converted_value = int(value)
print(f"Тип данных: {type(converted_value)}, используется для представления целых чисел")
#bool
value = input("Введите логическое значение (True или False): ")
converted_value = bool(value)
print(f"Тип данных: {type(converted_value)}, используется для представления логических значений")
#str
value = input("Введите строку: ")
print(f"Тип данных: {type(value)}, используется для представления строковых значений")
#complex
value = input("Введите комплексное число в формате a+bj: ")
converted_value = complex(value)
print(f"Тип данных: {type(converted_value)}, используется для представления комплексных чисел")
#float
value = input("Введите число с плавающей точкой: ")
converted_value = float(value)
print(f"Тип данных: {type(converted_value)}, используется для представления чисел с плавающ")
#Задание на 4
# Максимальное значение типа данных int
max_int = sys.maxsize
print(f"Максимальное значение типа int: {max_int}")

# Максимальное значение типа данных float
max_float = sys.float_info.max
print(f"Максимальное значение типа float: {max_float}")




