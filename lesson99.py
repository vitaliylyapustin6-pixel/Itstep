# text = input("Введіть рядок англійською мовою: ")
#
# count = 0
# for letter in text:
#     if letter in "aeiou":
#         count += 1
#
# print(f"Кількість голосних літер: {count}")

user_text = input('Введите текст:')

while True:
    user_definite_text = input('Введите слово:')
    if user_definite_text == 'EXIT':  # выход из цикла
            print('Вы свободны')
            break
    if user_definite_text in user_text:
        total = user_text.replace(user_definite_text, user_definite_text.upper())
        print(total)
        break

user_sentences = input('Введите предложения:')
total = 0
for i in user_sentences:
    if i in '.!?':
        total += 1
print(total)
