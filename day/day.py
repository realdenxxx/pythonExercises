day = int(input("Напишите число от 1 до 7: "))
if day >= 1 and day <= 7:
    if day == 1:
        print("понедельник")
    elif day == 2:
        print("вторник")
    elif day == 3:
        print("среда")
    elif day == 4:
        print("четверг")
    elif day == 5:
        print("пятница")
    elif day == 6:
        print("суббота")
    elif day == 7:
        print("воскресение")
else:
    print("ошибка")