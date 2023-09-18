#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

n_digit = int(input("Введите значение N: "))
digit = 1
while digit < n_digit:
    print(digit, end=',')
    digit = digit * 2