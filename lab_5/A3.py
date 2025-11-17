def create_abbreviation(text):
    words = text.split()
    abbreviation = ''.join(word[0].upper() for word in words if len(word) >= 3)
    return abbreviation

text = input("Введите текст: ")
print(create_abbreviation(text))