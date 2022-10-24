def conver_to_int(n): #объяление функции для определения целочисленности
    try: #если в данном блоке возникает ошибка, то вызывается блок except
        n = int(n) #преобразование в целое число
    except Exception:
        return -1
    return n
def conver_to_float(n): #объяление функции для определения целочисленности
    try: #если в данном блоке возникает ошибка, то вызывается блок except
        n = float(n) #преобразование в целое число
    except Exception:
        return -1
    return n
def input_table(table, n): #объявление функции для ввода отношений критериев в матрицу
    #ввод отношений для верхней половины матрицы, считая от главной диагонали
    for i in range(n):
        for j in range(n):
            if (i == j):
                table[i][j] = 1 #элементы главной диагонали равны единице
            if (i < j):
                while table[i][j] == 0: #для выхода из цикла ввода элемента ожидается верный ввод
                    ratio = input("Введите отношение критерия {0} к критерию {1} ".format(i+1, j+1))
                    ratio = conver_to_float(ratio)
                    if (ratio == -1) or (ratio in (0.5,0.33,0.25,0.2,0.14,0.125,0.11) == False and (1 <= ratio <= 9) == False): #проверка введённых значений на соответствие условиям
                        print('Отношение должно быть целым числом от 1 до 9 ')
                    else:
                        table[i][j] = ratio
    for i in range(n):
        for j in range(n):
            if (i > j):
                table[i][j] = 1/table[j][i]
    return table
#вывод матрицы попарных сравнений
def output_table(table, n):
    for i in range(n):
        for j in range(n):
            print("{0:.4f}".format(table[i][j]), end=" ")
        print()
def table_sum(table, n):#объявление функции для суммирования всех элементов
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += table[i][j]
    return sum
def count_wq (table,n,sum): #объявление функции для расчёта весовых коэффициентов
    array_wq  = list()
    #расчёт суммы отношений для каждого критерия
    for j in range(n):
        column_sum = 0
        for i in range(n):
            column_sum += table[j][i]
        array_wq.append(column_sum/sum)
    return array_wq

n = 0
#ввод количества критериев
while n == 0: #пока количество не будет положительным целым числом, цикл запрашивает ввод
    n = input("Введите количество критериев: ")
    n = conver_to_int(n)
    if (n == -1) or (n < 1): #обработка ошибок ввода польозователя
        print("Количество критериев должно быть положительным целым числом")
        n = 0
a = [[0] * n for i in range(n)] #создание двумерного массива n*n
a = input_table(a,n)
print("\nМатрица попарного сравнения: ")
output_table(a,n)
a_sum = table_sum(a,n)
print("\nСумма элементов матрицы: {0:.4f}".format(a_sum))
wq = count_wq(a,n,a_sum) #создание массива, хранящего весовые коэффициенты
print("Весовые коэффициенты:", end=" ")
for elem in wq:
    print(round(elem,2), end=" ") #форматирование вывода
