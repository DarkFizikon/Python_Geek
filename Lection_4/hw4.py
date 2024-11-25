def count_unique_characters(s: str) -> int:
    # Преобразуем все символы в нижний регистр
    lower_s = map(lambda x: x.lower(), s)

    # Создаём множество уникальных символов
    unique_chars = set(lower_s)

    # Возвращаем количество уникальных символов
    return len(unique_chars)

# Пример использования
message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
