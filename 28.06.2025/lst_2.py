def word_count(text):
    # Приводим текст к нижнему регистру
    text = text.lower()
    
    # Разбиваем строку на слова
    words = text.split()
    
    # Инициализируем словарь для подсчета
    word_counts = {}
    
    # Подсчитываем количество вхождений каждого слова
    for word in words:
        if word in word_counts:
            word_counts[word] += 1  # Увеличиваем счетчик слова
        else:
            word_counts[word] = 1  # Добавляем новое слово в словарь
            
    return word_counts

text = "Привет мир привет"
result = word_count(text)
print(result)  # Вывод: {'привет': 2, 'мир': 1}