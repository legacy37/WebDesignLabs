import math
print("1.1 введите число для модуля")
print(abs(int(input())))
print("1.2 введите 5 чисел для минимума")
b = [0,0,0,0,0]
for i in range (0,5):
    b[i] = int(input())
print(min(b))
print("1.3 введите 5 чисел для максимума")
b = [0,0,0,0,0]
for i in range (0,5):
    b[i] = int(input())
print(max(b))
print("1.4 введите числа для гипотенузы")
a1 = int(input())
b1 = int(input())
print(math.hypot(a1,b1))
print("1.5 Введите числа для сочетания")
k = int(input())
n = int(input())
print(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
print("1.6 введите число офицеров и мобилизованных")
a1 = int(input())
b1 = int(input())
print(math.ceil((a1+b1)/30))
print("1.7 Введите стоимость ручки")
a = int(input())*0.85
print(math.floor(1000/a))
print("1.8 Введите 3 числа")
a1 = int(input())
a2 = int(input())
a3 = int(input())
print(a1, " ", a2, " ", a3)
print("1.9 введите 3 числа")
a1 = int(input())
a2 = int(input())
a3 = int(input())
print(a1,"\n", a2,"\n", a3)
print("1.10 введите 2 числа для возведения в степень")
a1 = int(input())
a2 = int(input())
print(pow(a1,a2))
print(a1**a2)
for i in range(0,a2):
    a1 = a1*a1
print(a1)
print("1.11 Введите 2 вещественных числа")
a1 = float(input())
a2 = float(input())
print(a1+a2)
print("1.12 введите число синих и зелёных ручек")
a1 = int(input())
a2 = int(input())
print(a1+a2+2*a1+4*a2)
print("1.13введите длину и ширину")
a1 = int(input())
a2 = int(input())
print(2*(a1+a2))
print("1.14 число пи")
print(round(math.pi,3))
print("1.15 введите число рублей копеек и количество пирожков")
a1 = int(input())
a2 = int(input())
n = int(input())
print(math.floor(a1*n+(a2*n)/100)," ", (a2*n/100-math.floor(a2*n/100))*100)
print("1.16 кратность трём Введите float число")
a = float(input())
b = int(a)
print(not bool(b%3))
print("1.17 ВВедите float число 2 знака после запятой")
a = round(float(input()),2)
a = (a-int(a))*100
print(bool(a//50))
print("1.18 введите 3 стороны треугольника")
a1 = int(input())
a2 = int(input())
a3 = int(input())
print(bool((a1+a2)/a3) and bool((a1+a3)/a2) and bool((a3+a2)/a1))
print("1.19 Введите вещественное число (проверка на попадание в промежуток)")
a = float(input())
print((a>=(-3) and a<=3) or (a>=5 and a<=10))
print("1.20 введите количество учеников 1 2 и 3 класса")
a1 = int(input())
a2 = int(input())
a3 = int(input())
print(math.ceil(a1/2)+math.ceil(a2/2)+math.ceil(a3/2))