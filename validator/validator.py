# условия выполнения программы
x = 'y'
while x == 'y' or x == 'Y':

    # получаем входные данные два числа
    num_1 = int(input("Type number 1: "))
    num_2 = int(input("Type number 2: "))

    # валидатор входных данных
    while num_1 < 0 or num_2 < 0:
        print("Numbers can not be negative!")
        print("Dial positive numbers!")
        num_1 = int(input("Type number 1: "))
        num_2 = int(input("Type number 2: "))

    print("Numbers amount = ", num_1 + num_2, sep='')
    x = input("One more count? Y or N: ")
