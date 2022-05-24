# получаем входные данные от пользователя
# номеер кармана должен быть от 0 до 36
print()
pocket = int(input("Введите номер кармана от 0 до 36: "))

# инструкция для определения цвета кармана

if pocket == 0:
    pocketColour = "зелёный"
elif pocket >= 1 and pocket <= 10:
    if pocket % 2 == 1:
        pocketColour = "красный"
    else:
        pocketColour = "чёрный"
if pocket >= 11 and pocket <= 18:
    if pocket % 2 == 1:
        pocketColour = "чёрный"
    else:
        pocketColour = "красный"
if pocket >= 19 and pocket <= 28:
    if pocket % 2 == 1:
        pocketColour = "красный"
    else:
        pocketColour = "чёрный"
if pocket >= 29 and pocket <= 36:
    if pocket % 2 == 1:
        pocketColour = "чёрный"
    else:
        pocketColour = "красный"
if pocket < 0 or pocket > 36:
    print("ошибка")

else:
    print()
    print("число",'\t', "цвет")
    print("----------------")        
    print(pocket,'\t', pocketColour)
        



