print("Задание 8.1. Вводятся вещественные числа в одну строчку через пробел.")
s = set(map(float, input().split()))
print(*sorted(s))
print("Задание 8.2. Вводится текст в одну строку, слова разделены пробелом.")
words = input().lower().split()
unique_words = set(words)
print(len(unique_words))
print("Задание 8.3. Вводится строка, содержащая латинские символы, пробелы и цифры.")
text = input()
digits = {char for char in text if char.isdigit()}
if digits:
    print(' '.join(sorted(digits)))
else:
    print("No")
print("Задание 8.4. В ночном клубе фиксируется список гостей.")
guests = set()
while True:
    name = input()
    if name == '0':
        break
    guests.add(name)
print(len(guests))
print("Задание 8.5. В аккаунте youtube Сергея прокомментировали очередное видео.")
commentators = set()
while True:
    comment = input()
    if comment == '0':
        break
    name = comment.split(':')[0]
    commentators.add(name)
print(len(commentators))
print("Задание 8.6. Пользователь с клавиатуры вводит названия городов (пока не введет число 0).")
cities = set()
while True:
    city = input()
    if city == '0':
        break
    cities.add(city)
print(len(cities))
print("Задание 8.7. Вводятся два списка целых чисел каждый с новой строки.")
list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))
common_unique_numbers = list1 & list2
print(*sorted(common_unique_numbers))
print("Задание 8.8. Вводятся два списка целых чисел каждый с новой строки.")
list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))
unique_numbers = list1 - list2
print(*sorted(unique_numbers))
print("Задание 8.9. Вводятся два списка целых чисел каждый с новой строки.")
list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))
unique_numbers = list1 ^ list2
print(*sorted(unique_numbers))
print("Задание 8.10. Вводятся два списка городов каждый с новой строки.")
list1 = set(input().split())
list2 = set(input().split())
if list1 == list2:
    print("Yes")
else:
    print("No")
print("Задание 8.11. Вводится список оценок студента - его ответов у доски по предмету 'Информатика' в виде чисел от 2 до 5 в одну строку через пробел.")
grades = set(map(int, input().split()))
if 2 in grades:
    print("НЕ ДОПУЩЕН")
else:
    print("ДОПУЩЕН")
print("Задание 8.12. Вводятся два списка городов каждый с новой строки.")
list1 = set(input().split())
list2 = set(input().split())
if list1.issubset(list2):
    print("Yes")
else:
    print("No")
print("Задание 8.13. Вводится натуральное число, которое может быть получено простыми множителями из следующих: 2, 3, 5, 7, 11, 13.")
n = int(input())
factors = {2, 3, 5}
prime_factors = set()

for prime in [2, 3, 5, 7, 11, 13]:
    while n % prime == 0:
        prime_factors.add(prime)
        n //= prime

if factors.issubset(prime_factors):
    print("Yes")
else:
    print("No")
print("Задание 8.14. Вводятся целые числа в одну строчку через пробел.")
numbers = list(map(int, input().split()))
unique_numbers = sorted(set(numbers), reverse=True)
if len(unique_numbers) >= 3:
    print(unique_numbers[2])
else:
    print("No")
print("Задание 8.15. Вводится текст в одну строку, слова разделены пробелом.")
text = input().split()
word_count = {}

for word in text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word}: {count}")