#   Напишите программу, которая найдёт произведение пар чисел списка.
#   Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#   Пример:

#   - [2, 3, 4, 5, 6] => [12, 15, 16];
#   - [2, 3, 5, 6] => [12, 15]


n = int(input('Введите количество значений: '))
spisok = []
for i in range(n):
    spisok.append(int(input('Введите значение: ')))
print(spisok)

def multiply(spisok):
    spisok2 = []

#   делим список(spisok) на 2 половины
    
    for i in range((n + 1) // 2):

#   заполняем список(spisok2) произведением чисел списка(spisok)
        
        spisok2.append(spisok[i] * spisok[- i - 1])
    print(spisok2) 
multiply(spisok)