from tracemalloc import stop
from bs4 import BeautifulSoup
import requests as req
    
resp = req.get("https://wordle-igra.ru/slova-iz-5-bukv")
req.encoding = 'cp1251'
soup = BeautifulSoup(resp.text, 'html.parser')
a = []



for tag in soup.find_all("td"):
    if len(tag.text)>0:
        a.append(tag.text)

def rec(out):
#создаем словарь
    dic = {}
    alfavit = 'йцукенгшщзхъфывапролджэячсмитьбю-'
    for bukva in alfavit:
        dic[bukva] = 0
    #заполняем словарь основываясь на популярности букв
    for word in out:
        for bukva in word:
            dic[bukva] += 1
    sorted_tuple = sorted(dic.items(), key=lambda x: x[1])
    sorteddic = list(dict(sorted_tuple))
    print(sorteddic[::-1])
    def find_word(in_a):
        if in_a.find(bukva) >= 0:
            return True
        else:
            return False
    for i in range(-1,-len(sorteddic),-1):
        out = list(out)
        bukva = sorteddic[i]
        if len(list(filter(find_word, out))) != 0:
            out = list(filter(find_word, out))
    print(list(out)[0])

def green(in_a):
    if in_a.find(bukva,j,j+1) == j:
        return True
    else:
        return False
def yellow(in_a):
    if (in_a.find(bukva) != j) and (in_a.find(bukva) >= 0):
        return True
    else:
        return False
def grey(in_a):
    if in_a.find(bukva) >= 0:
        return False
    else:
        return True

out = a
for i in range(6):
    rec(out)
    print('Поптыка №',i+1)
    print('Введите слово, которое вы ввели в игре')
    slovo = input()
    for j in range(5):
        out = list(out)
        bukva = slovo[j]
        print('Каким цветом загорелась буква', bukva)
        znach = input()
        if znach == 'з':
            out = list(filter(green, out))
            print(list(out))
        if znach == 'ж':
            out = list(filter(yellow, out))
            print(list(out))
        if znach == 'с':
            out = list(filter(grey, out))
            print(list(out))
        if len(out) == 1:
            exit()