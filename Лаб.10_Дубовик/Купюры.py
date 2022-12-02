def Wkk(tn): #функция для обработки ошибок ввода числа N
    try:
        tn = int(tn) #преобразование в целое число
        if 0 < tn:
            return tn
        else:
            return 'False'
    except:
        return 'False'
#ввод суммы 
N = input('Введите сумму:\n')
while Wkk(N) == 'False': #обработка ошибок ввода N
    N=input('Введите натуральное число:\n')
N = Wkk(N)

k=[64,32,16,8,4,2,1] #создание массива купюр
print('Для выдачи суммы используются следующие купюры:\n')
#расчёт купюр и их количества 
for i in k:
    num=N//i
    N=N-(num*i)
    if num!=0:
        print(f'Количество: {num}, номинал: {i} ', end='\n')
    
