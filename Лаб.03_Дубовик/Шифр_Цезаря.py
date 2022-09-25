alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
step = int(input('Введите шаг шифровки: '))
text = input('Введите сообщение: ').upper()
n = ''
lang = input('Выберите язык RU/EU: ')
if lang == 'RU':
    for i in text:
        mesto = alfavit_RU.find(i)
        mesto_1 = mesto + step
        if i in alfavit_RU:
            n += alfavit_RU[mesto_1]
        else:
            n += i
else:
    for i in text:
        mesto = alfavit_EU.find(i)
        mesto_1 = mesto + step
        if i in alfavit_EU:
            n += alfavit_EU[mesto_1]
        else:
            n += i
print (n)
