import re

text = input('Введите текст:')
sentences = re.split(r'(?<=[.?!])\s+', text)
i = 0
while i < len (sentences):
    print(sentences[i])
    i = i + 1
print(f'предложений в тексте: {len(sentences)}')