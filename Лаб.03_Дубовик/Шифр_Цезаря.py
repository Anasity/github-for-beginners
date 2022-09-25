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
    
message = input("Сообщение для ДЕшифровки: ").upper() 
step = int(input('Шаг шифровки: '))  
lang = input('Выберите язык RU/EU: ')

print("Сообщение: " + message) 
print("Шаг: " + str(step)) 
if lang == 'RU':
    print("Резултат: " + func_caesar_ru(message, step)) 
elif lang == 'EU':
   print("Резултат: " + func_caesar_eu(message, step))  
else:
    print("Неверно выбран язык") 
