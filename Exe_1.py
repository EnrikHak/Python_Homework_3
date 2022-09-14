#   Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#   стоящих на нечётной позиции.

#   Пример:

#   - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


n = int(input('Введите кол-во чисел: '))
spisok = []
for i in range(n):
    spisok.append(int(input('Введите числа: ')))
print(spisok)

def summ(spisok):
    summa = 0
    for i in range(len(spisok)):
        if i % 2 == 1:
            summa += spisok[i]
    print(f'Сумма чисел нечетных позиций = {summa}')
summ(spisok)