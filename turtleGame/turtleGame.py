import turtle
turtle.setup(600,600)

# Константы координат квадрата цели
A = 225,280
B = 250,280
C = 250,255
D = 225,255

# Констана для определения силы удара
POWER_multiplie = 26

# Рисуем квадрат цели 
turtle.begin_fill()
turtle.speed(1)
turtle.penup() # поднять перо
turtle.goto(A)
turtle.pendown() # опустить перо
turtle.goto(B)
turtle.goto(C)
turtle.goto(D)
turtle.goto(A)
turtle.penup()

# возвращаем черепаху на исходную позицию
turtle.goto(0,0)

# запрос от пользователя параметров удара
angle = float(input('введите угол удара от 0 до 90: '))
turtle.left(angle)
strikePower = float(input('введите силу удара от 1 до 20: '))
speed = int(input('введите скорость удара от 1 до 10: '))

# блок выполнения удара по заданным параметрам
turtle.pencolor('red')
turtle.speed(speed)
turtle.forward(strikePower * POWER_multiplie)

# блок проверки попадания в цель
xposition = turtle.xcor()
yposition = turtle.ycor()
xposition = format(xposition,'.0f')
yposition = format(yposition,'.0f')
xposition = int(xposition)
yposition = int(yposition)
if xposition > 225 and xposition < 250 and yposition > 255 and yposition < 280:
    turtle.fillcolor('red')
    turtle.end_fill()
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(5)
    
if xposition < 225 or xposition > 250 or yposition < 255 or yposition > 280:
    print('Вы промахнулись')
if angle < 45:
    print('Добавь угла!')
if angle > 51:
    print('Уменьши угол атаки!')
if strikePower < 13 or strikePower > 15:
    print('Измени силу удара!')


print(xposition)
print(yposition)

turtle.done()