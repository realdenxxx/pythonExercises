# условие для работы и повторения программы 
cont = 'y'

while cont == 'y': # цикл для работы и повторения программы
    num = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    while not num.isdigit() or not num2.isdigit(): # вложенный цикл валидатор
        print("Это не число!")
        print("Попробуйте ещё раз")
        num = input("Введите число: ")
        num2 = input("Введите второе число: ")

    if num.isdigit() and num2.isdigit():
        num = int(num)
        num2 = int(num2)
        op = input("Выберите операцию - + , - , / , *: ")
        if op == '+':
            print("Сумма = ", num + num2)
        elif op == '-':
            print("Разность = ", num - num2)
        elif op == '/':
            print("Частное = ", num / num2)
        elif op == '*':
            print("Произведение = ", num * num2)

    print()
    cont = input("Ещё раз? Y or N: ")
