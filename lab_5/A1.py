import re

def shorten_text (txt):
    while True:
        if txt.find('(') == -1: break
        if txt.find(')') == -1: break
        txt = txt.replace(txt[txt.find('('):txt.find(')')+1], '')
    return txt

stroka = input("Введите текст:")
print(shorten_text(stroka))