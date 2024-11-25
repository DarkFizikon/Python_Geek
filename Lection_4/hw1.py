from typing import List

# Исходные списки
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

# Новый список для чисел, возведённых в третью степень и округлённых до трёх знаков после запятой
cubed_floats = [round(x ** 3, 3) for x in floats]

# Новый список для имён, содержащих минимум пять букв
long_names = [name for name in names if len(name) >= 5]

# Новый список для произведения всех чисел
product_of_numbers = [numbers[0]]
for number in numbers[1:]:
    product_of_numbers[0] *= number

# Вывод результатов
print("Cubed and rounded floats:", cubed_floats)
print("Names with at least 5 letters:", long_names)
print("Product of all numbers:", product_of_numbers[0])
