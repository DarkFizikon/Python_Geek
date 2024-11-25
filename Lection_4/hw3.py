from collections import Counter

def can_be_poly(s: str) -> bool:
    # Подсчитываем частоту каждого символа в строке
    char_count = Counter(s)

    # Подсчитываем количество символов с нечётной частотой
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    # Если количество символов с нечётной частотой не превышает одного, то можно получить палиндром
    return odd_count <= 1

# Примеры использования
print(can_be_poly('abcba'))  # True
print(can_be_poly('abbbc'))   # False
