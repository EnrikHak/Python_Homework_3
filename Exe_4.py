#   Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#   Пример:

#   - 45 -> 101101
#   - 3 -> 11
#   - 2 -> 10


number = int(input('Введите число: '))

lastNum = []
while number != 0:
    last = number % 2
    lastNum.append(last)
    number = number // 2
print(lastNum)
reverArr = []

#   Разворот массива в обратную сторону

for i in reversed(lastNum):
    reverArr.append(i)
print(reverArr)