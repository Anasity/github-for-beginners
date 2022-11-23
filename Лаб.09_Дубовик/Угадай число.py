from loguru import logger
import random
import sys
logger.add("число.log", format="{time} {level} {message}",level="DEBUG")

def evf(tn): #функция для обработки ошибок ввода числа N
    try:
        tn = int(tn) #преобразование в целое число
        if 0 < tn:
            return tn
        else:
            print("Вы ввели число меньше 1")
            logger.error("проверка на число: не пройдена (error)")
            return 'False'
    except:
        print("Вы ввели не число или не целое число")
        logger.error("проверка на число: не пройдена (error)")
        return 'False'

def pop(s): #функция для обработки ошибок ввода количества попыток
    try:
        s = int(s)
        if 0 < s:
            return s
        else:
            logger.error("проверка на число: не пройдена (error)")
            return 'False'

    except:
        logger.error("проверка на число: не пройдена (error)")
        return 'False'

def ch(f): #функция для обработки ошибок ввода в задаче Б (номера фигур)
    try:
        f = int(f)
        if 0 < f:
            return f
        else:
            logger.error("проверка на число: не пройдена (error)")
            return 'False'
    except:
        logger.error("проверка на число: не пройдена (error)")
        return 'False'

N = input('Компьютер загадает число от 1 до N. Введите N: ')
logger.info("ввод числа N (info)")
while evf(N) == 'False': #обработка ошибок ввода N
    N=input('введите N: ')
    logger.info("ввод числа N (info)")
logger.info("проверка на число:пройдена (info)")
N = evf(N)

the_numb = random.randint(1, N)

k=input('Введите количество попыток: ')
logger.info("ввод количества попыток(info)")
while pop(k) == 'False': #обработка ошибок ввода k
    k=input('Введите количество попыток: ')
    logger.info("ввод количества попыток (info)")
logger.info("проверка на число:пройдена (info)")
k = pop(k)

guess = input("Назовите число: ")
logger.info("ввод числа(info)")
while ch(guess) == 'False': #обработка ошибок ввода числа
    guess = input('Назовите число: ')
    logger.info("ввод числа (info)")
logger.info("проверка на число:пройдена (info)")
guess = ch(guess)

tries = 1
while guess != the_numb:
    if guess > the_numb:
        print("Меньше")
        logger.info("Число должно быть меньше введённого (info)")
    else:
        print("Больше")
        logger.info("Число должно быть больше введённого (info)")
    guess = int(input("Назовите число: "))
    logger.info("ввод числа (info)")
    tries += 1
    if tries>k:
        logger.info(f'Попытки закончились. Вам не удалось угадать число, на самом деле это {the_numb} (info)')
        print('Попытки закончились. Вам не удалось угадать число, на самом деле это', the_numb)
        sys.exit() #выход из программы
logger.info(f'Вам удалось угадать число, в самом деле это {the_numb} (info)')
print(f'Вам удалось угадать число, в самом деле это {the_numb}')
