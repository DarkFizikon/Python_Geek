array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

#Количество элементов, которые есть в каждом списке
#Решение без ипользования множеств
all_elements = array_1 + array_2 + array_3
new_array_elements = []

for element in all_elements:
    if element not in new_array_elements and all(element in array for array in [array_1, array_2, array_3]):
        new_array_elements.append(element)

print(f"Solution without plenty's: {new_array_elements}")
#Решение с использованием множеств
new_array_elements_set = set(array_1) & set(array_2) & set(array_3)
print(f"solution with plenty's: {new_array_elements_set}")

#Количество элементов из первого списка, которые отстутвуют во втором и третьем
#Решение без ипользования множеств
new_array_elements_2 = []
for element in array_1:
    if element not in array_2 and element not in array_3:
        new_array_elements_2.append(element)
print(f"Solution without plenty's: {new_array_elements_2}")

#Решение с использованием множеств
new_array_elements_set_2 = set(array_1) - set(array_2) - set(array_3)
print(f"solution with plenty's: {new_array_elements_set_2}")

