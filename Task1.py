# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

d = int(input('Введите цифру от 1 до 7: '))
if d <= 5:
    print('Будний день')
else:
    print('Выходной')