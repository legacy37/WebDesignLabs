
print("6.1 введите 2 числа")
a = int(input())
b = int(input())
while a <= b:
    print(a**2, end = " ")
    a += 1

print("6.2 введите float стоимость книги")
a = float(input())
i = 2
while i <= 10:
    print(round(a*i,1),end=" ")
    i += 1
    
print("6.3 введите n")
a = int(input())
i = 1
sum = 0
while i <= a:
    sum += 1/i
    i += 1
print(round(sum,3))

print("6.4 введите числа пока не встретится 0")
sum = 0
while True:
    a = int(input())
    if a == 0: break
    sum += a
print(sum)

print("6.5 введите строку с дефисами")
a = input()
while '--' in a:
    a = a.replace('--','-')
    a = a.replace('---','-')
print(a)

print("6.6 введите число ")
n = int(input())
b = 1
while n > 0:
    b *= n % 10
    n //= 10
print(b)
print("6.7 введите количество чисел фиббоначи")
n = int(input())
a, b = 1, 1
result = "1 1"
i = 2
while i < n:
    a, b = b, a + b
    result += f" {b}"
    i += 1
print(result)
print("6.8 введите количество часов")
n = int(input())
cells = 1
hours = 0
while hours < n:
    cells *= 2
    hours += 3
print(cells)
print("6.9 введите количество лет")
n = int(input())
deposit = 1000
years = 0
while years < n:
    deposit *= 1.05
    years += 1
print(round(deposit, 2))
print("6.10 введите 2 числа")
n, m = map(int, input().split())
result = ""
while n <= m:
    if n % 2 != 0:
        result += f"{n} "
    n += 1
print(result.strip())
print("6.11 ")
n = 100
result = ""
while n < 1000:
    if n % 47 == 43 and n % 3 == 0:
        result += f"{n} "
    n += 1
print(result.strip())
print("6.12")
lst = [0] * 10
count = 0
while count < 5:
    p = int(input())
    if lst[p] == 1:
        continue
    lst[p] = 1
    count += 1
print(" ".join(map(str, lst)))
print("6.13 ")
product = 1
while True:
    n = int(input("введите число "))
    if n == 0:
        break
    if n < 0:
        continue
    product *= n
print(product)
print("6.14 ")
cities = input().split()
i = 0
while i < len(cities):
    if len(cities[i]) <= 5:
        print("No")
        break
    i += 1
else:
    print("Yes")
print("6.15 введите имена")
names = input().split()
i = 0
while i < len(names):
    if names[i].lower().startswith(names[i][0].lower()) and names[i].lower().endswith(names[i][0].lower()):
        print("Yes")
        break
    i += 1
else:
    print("No")
print("6.16 введите число")
n = int(input())
if n >= 100:
    print("слишком большое значение n")
else:
    result = ""
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            result += f"{i} "
        i += 1
    print(result.strip())
print("6.17 введите число")
n = int(input())
i = 1
while i * i <= n:
    i += 1
print(i)
print("6.18 введите число")
x = int(input())
distance = 10
day = 1
while distance <= x:
    distance *= 1.1
    day += 1
print(day)
print("6.19")
books = []
while True:
    book = input("введите название книги ")
    if book == "":
        break
    books.append(book)
result = ""
for book in books:
    if " " not in book:
        result += f"{book} "
print(result.strip())
print("6.20 ")
print(" ".join(map(str, range(11))))
print("6.21")
print(" ".join(map(str, range(10, -1, -1))))
print("6.22 ")
print(" ".join(map(str, range(-10, 0, 2))))
print("6.23")
print(" ".join(map(str, range(1, 20, 3))))
print("6.24 введите числа через пробел")
numbers = list(map(int, input().split()))
sum_odd = 0
for num in numbers:
    if num % 2 != 0:
        sum_odd += num
print(sum_odd)
print("6.25 введите названия городов")
cities = input().split()
lengths = []
for city in cities:
    lengths.append(len(city))
print(" ".join(map(str, lengths)))

print("6.26 введите число n ")
n = int(input())
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=' ')
print("6.27 введите n")
n = int(input())
a = 0
for i in range(1,n+1):
    if n%i == 0:
        a += 1
if a == 2:
    print("ДА")
else:
    print("НЕТ")
print("6.28 введите в строку названия городов: ")
cities = input().split()
for i in range(len(cities) - 1):
    last_char = cities[i][-1]
    if last_char in 'ьъы':
        last_char = cities[i][-2]
    if cities[i + 1][0].lower() != last_char.lower():
        print("No")
        break
else:
    print("Yes")
print("6.29 введите число n")
n = int(input())
sum = 0
for i in range(1,n):
    if n%i == 3 or n%5 == 0:
        sum += i
print(sum)
print("6.30 введите строку")
s = input()
indices = [i for i in range(len(s) - 1) if s[i:i+2] == 'ра']
print(' '.join(map(str, indices)) if indices else -1)
print("6.31 введите номер телефона")
phone = input()
if len(phone) == 16 and phone[0] == '+' and phone[1] == '7' and phone[2] == '(' and phone[6] == ')' and phone[10] == '-' and phone[13] == '-':
    for i in range(3, 6):
        if not phone[i].isdigit():
            print("No")
            break
    else:
        for i in range(7, 10):
            if not phone[i].isdigit():
                print("No")
                break
        else:
            for i in range(11, 13):
                if not phone[i].isdigit():
                    print("No")
                    break
            else:
                for i in range(14, 16):
                    if not phone[i].isdigit():
                        print("No")
                        break
                else:
                    print("Yes")
else:
    print("No")
print("6.32 введите мат выражение")
expression = input().replace(" ", "")
result = 0
current_number = ""
current_operator = "+"

for char in expression:
    if char.isdigit():
        current_number += char
    else:
        if current_operator == "+":
            result += int(current_number)
        else:
            result -= int(current_number)
        current_number = ""
        current_operator = char

if current_operator == "+":
    result += int(current_number)
else:
    result -= int(current_number)

print(result)
print("6.33 введите целые числа в строку через пробел")
numbers = list(map(int, input().split()))
for i, num in enumerate(numbers):
    numbers[i] = num ** 2
print(' '.join(map(str, numbers)))
print("6.34 введите целые числа в строку через пробел")
numbers = input().split()
result = []
for num in numbers:
    result.extend([num, num])
print(' '.join(result))
print("6.35 введите вещественные числа в строку через пробел")
numbers = list(map(float, input().split()))
min_value = numbers[0]
for num in numbers[1:]:
    if num < min_value:
        min_value = num
print(min_value)
print("6.36 введите вещественные числа в строку через пробел")
numbers = list(map(float, input().split()))
for i, num in enumerate(numbers):
    if num < 0:
        numbers[i] = -1.0
print(' '.join(map(str, numbers)))
print("6.37 введите список городов")
cities = iter(input().split())
print(next(cities))
print(next(cities))
print("6.38 введите строку")
s = iter(input())
for char in s:
    if char == ' ':
        break
    print(char, end='')
print("6.39 введите четырёхзначное целое число")
number = input()
digits = iter(number)
print(' '.join(digits))
print("6.40 введите n")
N = int(input())
matrix = [[1] * N for _ in range(N)]
for row in matrix:
    row[-1] = 5
for row in matrix:
    print(' '.join(map(str, row)))
print("6.41 введите url")
urls = [input().replace(" ", "-") for _ in range(int(input()))]
for url in urls:
    print(url)
print("6.42 введите n")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
primes = [str(i) for i in range(2, n) if is_prime(i)]
print(' '.join(primes))
print("6.43 введите матрицу 5 на 5")
matrix = [list(map(int, input().split())) for _ in range(5)]

def check_neighbors(i, j):
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if 0 <= x < 5 and 0 <= y < 5 and (x != i or y != j):
                if matrix[x][y] == 1:
                    return False
    return True

valid = True
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            if not check_neighbors(i, j):
                valid = False
                break
    if not valid:
        break

print("Yes" if valid else "No")
print("6.44 введите матрицу 5 на 5")
matrix = [list(map(int, input().split())) for _ in range(5)]

symmetric = True
for i in range(5):
    for j in range(5):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break
    if not symmetric:
        break

print("Yes" if symmetric else "No")
print("6.45 введите n")
n = int(input())
bills = [64, 32, 16, 8, 4, 2, 1]
result = []
for bill in bills:
    while n >= bill:
        result.append(bill)
        n -= bill
print(' '.join(map(str, result)))
print("6.46 введите вещественные числа в строку черзе пробел")
numbers = [abs(float(x)) for x in input().split()]
print(numbers)
print("6.47 введите семизначное число ")
number = input()
digits = [int(x) for x in number]
print(digits)
print("6.48 введите названия городов в строку через пробел")
cities = [city for city in input().split() if len(city) > 5]
print(' '.join(cities))
print("6.49 введите число N")
n = int(input())
divisors = [i for i in range(1, n + 1) if n % i == 0]
print(' '.join(map(str, divisors)))
print("6.50 введите число N")
N = int(input())
matrix = [[i] * N for i in range(N)]
for row in matrix:
    print(' '.join(map(str, row)))
print("6.51 введите список вещественных чисел")
numbers = list(map(float, input().split()))
even_index_numbers = [num for i, num in enumerate(numbers) if i % 2 == 0]
print(' '.join(map(str, even_index_numbers)))
print("6.52 введите 2 списка чисел одинаковой длины через пробел")
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
sum_list = [list1[i] + list2[i] for i in range(len(list1))]
print(' '.join(map(str, sum_list)))
print("6.53 введите список")
data = input().split()
cities_population = [[data[i], int(data[i + 1])] for i in range(0, len(data), 2)]
print(cities_population)
print("6.54 введите пароль")
import re

password = input()
if (re.search(r'[a-z]', password) and
    re.search(r'[A-Z]', password) and
    re.search(r'[0-9]', password) and
    re.search(r'[$#@!%?^&]', password) and
    len(password) >= 6):
    print("Yes")
else:
    print("No")