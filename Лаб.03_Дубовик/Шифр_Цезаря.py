def func_to_number(tn):
    try:
        tn = int(tn)
        return tn
    except:
        print("ОШИБКА: Вы ввели не число")
        return 'False'
        
def func_to_char(txt):
    n=len(txt)
    for i in range(n):
        if 65<=ord(txt[i])<=90 or 1040<=ord(txt[i])<=1071:
            pass
        else:
            print("ОШИБКА: Вы ввели не текст", txt[i])
            return 'False'
    return txt

def func_caesar_ru(message, step): 
    result = "" 
    for i in range(len(message)): 
        char = message[i] 
        if(char.isupper()): 
            result += chr((ord(char) + step - 1040) % 32 + 1040) 
        else: 
            result += chr((ord(char) + step - 1072) % 32 + 1072) 
    return result 

def func_caesar_eu(message, step): 
    result = "" 
    for i in range(len(message)): 
        char = message[i] 
        if(char.isupper()): 
            result += chr((ord(char) + step - 65) % 26 + 65) 
        else: 
            result += chr((ord(char) + step - 97) % 26 + 97) 
    return result 
    
message = input("Сообщение: ").upper() 
while func_to_char(message) == 'False':
    message = input("Сообщение: ").upper()
message=func_to_char(message)

step = input('Шаг шифровки: ')
while func_to_number(step) == 'False':
    step=input('Шаг шифровки: ')
step=func_to_number(step)

lang = input('Выберите язык RU/EU: ').upper() 
while lang != 'RU' and  lang != 'EU' :
    lang=input('Выберите язык RU/EU: ').upper()


print("Сообщение: " + message) 
print("Шаг: " + str(step)) 
if lang == 'RU':
    print("Резултат: " + func_caesar_ru(message, step)) 
elif lang == 'EU':
   print("Резултат: " + func_caesar_eu(message, step))  
else:
    print("Неверно выбран язык") 
