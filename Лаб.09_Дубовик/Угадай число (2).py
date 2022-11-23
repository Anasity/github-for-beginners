import random
import sys

def evf(tn): #функция для обработки ошибок ввода числа N
    try:
        tn = int(tn) #преобразование в целое число
        if 0 < tn:
            return tn
        else:
            print("Вы ввели число меньше 1")
            return 'False'
    except:
        print("Вы ввели не число или не целое число")
        return 'False'

def pop(s): #функция для обработки ошибок ввода количества попыток
    try:
        s = int(s)
        if 0 < s:
            return s
        else:
            return 'False'
    except:
        return 'False'

def ch(f): #функция для обработки ошибок ввода в задаче Б (номера фигур)
    try:
        f = int(f)
        if 0 < f:
            return f
        else:
            return 'False'
    except:
        return 'False'

N = input('Компьютер загадает число от 1 до N. Введите N: ')
while evf(N) == 'False': #обработка ошибок ввода N
    N=input('введите N: ')
N = evf(N)

the_numb = random.randint(1, N)

k=input('Введите количество попыток: ')
while pop(k) == 'False': #обработка ошибок ввода k
    k=input('Введите количество попыток: ')
k = pop(k)

guess = input("Назовите число: ")
while ch(guess) == 'False': #обработка ошибок ввода числа
    guess = input('Назовите число: ')
guess = ch(guess)

tries = 1
while guess != the_numb:
    if guess > the_numb:
        print("Меньше")
    else:
        print("Больше")
    guess = int(input("Назовите число: "))
    tries += 1
    if tries>k:
        print ('Попытки закончились. Вам не удалось угадать число, на самом деле это', the_numb)
        sys.exit() #выход из программы

print("Вам удалось отгадать число, это в самом деле", the_numb)
