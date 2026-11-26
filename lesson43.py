user_row = input('Введите рядок')
user_symbol = input('Введете символ')
print(user_row.count(user_symbol))

total = 0

for i in user_row:
    if user_symbol == i:
        total += 1
print(total)

user_word = input("Введите рядок:")

print(len(user_word))
print(user_word.count('szh'))
if user_word in "python":
    print('Слова python есть!')

text = input("Введіть текст: ")

result = text.replace(" ", "-")
print(f"Змінений текст: {result}")

word = input('Введите предложение:')
word_text = input('Введите слово:')
total = 0
for i in word.split():
    if i == word_text:
        total += 1
print(total)

items = input("Введіть ваші речі: ").lower()

if "ніж" in items or "гроші" in items or "отрута" in items:
    print("У вас є речі які заборонено перевозити")
else:
    print("Оформлено доставку")

text = input('Введите текст: ')
letters = 0
digits = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print('Букв:', letters)
print('Цифр:', digits)

user_password_create = input('Придумайте пароль:')

if len(user_password_create) > 8:
#Уже не знал как назвать переменные, знаю что так делать нельзя.
    a = 0
    x = 0
    for i in user_password_create:
        if i.isalpha() > 0:
            a += 1
        if i.isdigit() > 0:
            x += 1
    if a > 0 and x > 0:        
        print('Пароль хароший')
    else: print('Пароль слабый')
else: print('Слабый пароль')
  
