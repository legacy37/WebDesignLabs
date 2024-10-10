print("Задание 7.1. Вводится целое положительное число n.")
n = int(input())
squares = {i: i**2 for i in range(1, n + 1)}
print(squares)
print("Задание 7.2. Вводятся данные в формате ключ=значение в одну строчку через пробел.")
data = input().split()
d = dict(item.split('=') for item in data)
d = {k: int(v) for k, v in d.items()}
print(*sorted(d.items()))
print("Задание 7.3. Вводятся данные в формате ключ=значение в одну строчку через пробел.")
data = input().split()
d = {}
for item in data:
    key, value = item.split('=')
    d[int(key)] = value
print(*sorted(d.items()))
print("Задание 7.4. Вводятся данные в формате ключ=значение в одну строчку через пробел.")
data = input().split()
d = dict(item.split('=') for item in data)
if 'house' in d and 'True' in d and '5' in d:
    print("Yes")
else:
    print("No")
print("Задание 7.5. Вводятся номера телефонов в одну строчку через пробел с разными кодами стран.")
phones = input().split()
d = {}
for phone in phones:
    code = phone[:2]
    if code not in d:
        d[code] = []
    d[code].append(phone)
print(*sorted(d.items()))
print("Задание 7.6. Вводятся номера телефонов в формате (пока не встретится число 0):")
d = {}
while True:
    entry = input().split()
    if entry[0] == '0':
        break
    number, name = entry
    if name not in d:
        d[name] = []
    d[name].append(number)
print(*sorted(d.items()))
print("Задание 7.7. Пользователь вводит в цикле целые положительные числа, пока не введет число 0.")
cache = {}
while True:
    num = int(input())
    if num == 0:
        break
    if num in cache:
        print(f"значение из кэша: {cache[num]}")
    else:
        sqrt_value = round(num ** 0.5, 2)
        cache[num] = sqrt_value
        print(sqrt_value)
print("Задание 7.8. Вводится строка из русских букв и символов пробела.")
morse_dict = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
    'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
    'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
    'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--',
    'Я': '.-.-', ' ': ' '
}

text = input().upper()
morse_code = ' '.join(morse_dict[char] for char in text)
print(morse_code)
print("Задание 7.9. Имеется закодированная строка с помощью азбуки Морзе.")
morse_code = input().split()
decoded_message = ''.join(morse_dict[code] for code in morse_code)
print(decoded_message)
print("Задание 7.10. Вводится список целых чисел в одну строчку через пробел.")
numbers = list(map(int, input().split()))
unique_dict = {num: True for num in numbers}
unique_list = list(unique_dict.keys())
print(' '.join(map(str, unique_list)))
print("Задание 7.11. Вводятся данные в формате (пока не встретится число 0):")
birthdays = {}
while True:
    entry = input().split()
    if entry[0] == '0':
        break
    date, name = entry
    if date not in birthdays:
        birthdays[date] = []
    birthdays[date].append(name)

for date, names in birthdays.items():
    print(f"{date}: {', '.join(names)}")
print("Задание 7.12. Имеется словарь с наименованиями предметов и их весом (гр.).")
items = {
    'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 'брюки': 1000, 'бумага': 200,
    'молоток': 600, 'пила': 400, 'удочка': 1200, 'расческа': 40, 'котелок': 820, 'палатка': 5240,
    'брезент': 2130, 'спички': 10
}

N = int(input()) * 1000
sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
backpack = []
total_weight = 0

for item, weight in sorted_items:
    if total_weight + weight <= N:
        backpack.append(item)
        total_weight += weight

print(' '.join(backpack))
print("Задание 7.13. Вводится строка из которой требуется создать словарь.")
text = input()
letter_count = {char: text.count(char) for char in text}
print(letter_count)