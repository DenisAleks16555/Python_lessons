def remove_vowels(s): # функция удаления из строки всех гласных букв
    vowels = 'аеёиоуыэюя'
    return ''.join([char for char in s if char not in vowels])
print(remove_vowels("программирование"))