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
print(user_word.count(szh))
if user_word in "python":
    print('Слова python есть!')


