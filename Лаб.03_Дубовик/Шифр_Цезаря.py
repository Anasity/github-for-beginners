def func_to_number(tn): #объявление функции, проверяющей ввод только цифр
    try: #если в данном блоке возникает ошибка, то вызывается блок except
        tn = int(tn) #преобразование в целое число
        return tn #функция, возвращающая значение tn
    except: #обработка ошибки
        print("ОШИБКА: Вы ввели не число")
        return 'False' #функция возвращает False


def func_to_char(txt):  #объявление функции, проверяющей ввод только букв
    n = len(txt) #функция возвращает длину текста
    for i in range(n): #цикл генерирует числа в диапазоне от i=0 до n
        if 65 <= ord(txt[i]) <= 90 or 1040 <= ord(txt[i]) <= 1071: #функция возвращает число символа Unicode,
            # проверяет, что символ в пределах русского и английского алфавитов
            pass #пропуск хода
        else: #обработка ошибки
            print("ОШИБКА: Вы ввели не текст", txt[i])
            return 'False' #функция возвращает False
    return txt #функция возвращает текст


def func_caesar_ru(message, step): #объявление функции для русского алфавита
    result = "" #объявление строки
    for i in range(len(message)): #цикл генерирует числа в диапазоне от i=0 до длины строки
        char = message[i]
        if (char.isupper()):
            result += chr((ord(char) + step - 1040) % 32 + 1040) #Функция возвращает строку,
            # представляющую символ Unicode русского алфавита
        else:
            result += chr((ord(char) + step - 1072) % 32 + 1072)
    return result


def func_caesar_eu(message, step): ##объявление функции для английского алфавита
    result = ""
    for i in range(len(message)): #цикл генерирует числа в диапазоне от i=0 до длины строки
        char = message[i]
        if (char.isupper()):
            result += chr((ord(char) + step - 65) % 26 + 65) #Функция возвращает строку,
            # представляющую символ Unicode английского алфавита
        else:
            result += chr((ord(char) + step - 97) % 26 + 97)
    return result


message = input("Сообщение: ").upper() #функция преобразовывает строку massage в верхний регистр
while func_to_char(message) == 'False': #пока возникает ошибка, выводится "Сообщение: "
    message = input("Сообщение: ").upper()
message = func_to_char(message)

step = input('Шаг шифровки: ')
while func_to_number(step) == 'False': #пока возникает ошибка, выводится "Шаг шифровки: "
    step = input('Шаг шифровки: ')
step = func_to_number(step)

lang = input('Выберите язык RU/EU: ').upper() #функция преобразовывает строку lang в верхний регистр
while lang != 'RU' and lang != 'EU':
    lang = input('Выберите язык RU/EU: ').upper()

print("Сообщение: " + message)
print("Шаг: " + str(step))
if lang == 'RU':
    print("Резултат: " + func_caesar_ru(message, step))
elif lang == 'EU':
    print("Резултат: " + func_caesar_eu(message, step))
else:
    print("Неверно выбран язык")
    
