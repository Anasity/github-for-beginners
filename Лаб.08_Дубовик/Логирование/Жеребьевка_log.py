from loguru import logger
logger.add("Жерб.log", format="{time} {level} {message}",level="DEBUG")

import random
import keyboard


def number(tn): #функция для обрабоки ошибок ввода координат
    try:
        tn = int(tn) #преобразование в целое число
        if tn>=1:
            return tn
        else:
            print('Вы не ввели количество бочек: ')
            logger.error("проверка на число: не пройдена (error)")
            return 'False'
    except:
        print('Вы не ввели количество бочек: ')
        logger.error("проверка на число: не пройдена (error)")
        return 'False'

N = input('введите количество бочек: ')
logger.info("количество бочек введено (info)")
while number(N) == 'False': #обработка ошибок ввода N
    N = input('введите количество бочек: ')
    logger.info("количество бочек введено (info)")
logger.info("проверка на число:пройдена (info)")
N = number(N)
print('для проведения жеребьевки нажимайте пробел')
A = random.sample(range(1,N+1), N) #функция возвращает
# случайные элементы из списка без повторений

for i in A:
    print(f'случайное число - {i}')
    logger.info(f'случайное число - {i} (info)')
    while 1:
        keyboard.wait(' ')
        if keyboard.is_pressed(' '): #функция принимает символ в качестве
                                     #входных данных и возвращает True
            break
        else:
            continue
