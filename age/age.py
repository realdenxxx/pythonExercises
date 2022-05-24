age = int(input("введите возраст: "))


if age <= 1:
    print("младенец")
elif age > 1 and age < 13:
    print("ребёнок")
elif age > 13 and age < 20:
    print("подросток")
elif age > 20:
    print("взрослый")