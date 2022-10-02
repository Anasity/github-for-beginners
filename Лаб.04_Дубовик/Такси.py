def Sort_Tax(A):
    j = len(A) - 1
    flag = True
    while flag:
        flag = False
        for i in range(0, j):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                flag = True
        j -= 1

def Sort_Dist(A):
    j = len(A) - 1
    flag = True
    while flag:
        flag = False
        for i in range(0, j):
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                flag = True
        j -= 1

n=int(input("Введите число сотруднииков (от 1 до 1000): "))
dist=list(map(int, input("Введите расстояния в км от работы до домов сотрудников : ").split()))
tax=list(map(int, input("Введите тарифы в рублях за проезд одного км в такси: ").split()))
for i in range(n):
    tax[i]= (tax[i], i)
for i in range(n):
    dist[i]= (dist[i], i)
 
Sort_Tax(tax)
Sort_Dist(dist)

sum_itog=0
for line in range(n):
    sum=tax[line][0]*dist[line][0]
    sum_itog=sum_itog+sum
    a = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    b = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    c = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    d = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    e = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    f = ["тысяча", "тысячи", "тысяч"]
    g = ["рубль", "рубля", "рублей"]
    n1 = sum // 100000
    n2 = (sum // 10000) % 10
    n3 = (sum // 1000) % 10
    n4 = (sum // 100) % 10
    n5 = (sum // 10) % 10
    n6 = sum % 10
    chg = ""
    if n1 != 0:
        i1 = n1 - 1
        chg += e[i1] + " "
    if n2 == 1 and n3 == 0:
        chg += d[0] + " "
    if n2 != 1:
        if n2 != 0:
            i2 = n2 - 1
            chg += d[i2] + " "
    if n3 != 0:
        if n2 == 1:
            i3 = n3 - 1
            chg += c[i3] + " " + f[2] + " "
        else:
            i3 = n3 - 1
            chg += b[i3] + " "
            if n3 == 1:
                chg += f[0] + " "
            elif 1 < n3 < 5:
                chg += f[1] + " "
            else:
                chg += f[2] + " "
    if (n3 == 0) and (n2 or n1 != 0):
        chg += f[2] + " "
    
    if n4 != 0:
        i4 = n4 - 1
        chg += e[i4] + " "
    
    if n5 == 1 and n6 == 0:
        chg += d[0] + " "
    
    if n5 != 1:
        if n5 != 0:
            i5 = n5 - 1
            chg += d[i5] + " "
    if n6 != 0:
        if n5 == 1:
            i6 = n6 - 1
            chg += c[i6] + " " + g[2]
        else:
            i6 = n6 - 1
            chg += a[i6] + " "
            if n6 == 1:
                chg += g[0] + " "
            elif 1 < n6 < 5:
                chg += g[1] + " "
            else:
                chg += g[2] + " "
    if (n6 == 0) and (n5 or n4 or n3 or n2 or n1 !=0):
        chg += g[2]
    chg = chg.capitalize()
    print  ("сотрудник ", dist[line][1]+1,", машина ", tax[line][1]+1, ". сумма поездки :", sum, chg)
print ("Общая сумма: ", sum_itog)

