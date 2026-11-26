# #1 Задание
# s =[1, 8, -5, 9]
#
# print(s)
#
# for i in s:
#     i += 3
#     print(i)
#
# #2 Задание
#
# spisok = []
#
# while True:
#     user_number = int(input('Введите число:'))
#     if user_number == -1:
#         break
#     spisok.append(user_number)
# print(len(spisok))
# print(sum(spisok))
# print(min(spisok))
# print(max(spisok))
#
# #3 Задание
# positive = []
# negative = []
#
# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#     if number == 0:
#         break
#     if number > 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
# print("Додатні числа:", positive)
# print("Від'ємні числа:", negative)

#4 Task

money_list = []
new_money_list = []

while True:
    user_money = int(input('Введите число:'))
    if user_money == -1:
        user_vidsotok = int(input('Введите видсоток:'))
        for i in money_list:
            total = i + (i / 100 * user_vidsotok)
            salary = new_money_list.append(total)
            print(new_money_list)
            break
    money_list.append(user_money)

