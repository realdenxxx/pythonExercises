

# программа наносит звезды созвездия Ориона
import turtle
turtle.speed(1)
turtle.bgcolor('black')
turtle.pencolor('blue')
turtle.pensize(2)
# размер окна
turtle.setup(500,600)

# установить черепаху
turtle.penup()
turtle.hideturtle() # не показывать черепаху на экране

#создать именованные константы для звёздных координат
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# наносим звёзды
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #ЛЕВОЕ ПЛЕЧО
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #ПРАВОЕ ПЛЕЧО
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) #ЛЕВАЯ ЗВЕЗДА В ПОЯСЕ
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) #СРЕДНЯЯ ЗВЕЗДА
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) #ПРАВАЯ ЗВЕЗДА
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #ЛЕВОЕ КОЛЕНО
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) #ПРАВОЕ КОЛЕНО
turtle.dot()

#ВЫВЕСТИ НАЗВАНИЯ ЗВЕЗД.
turtle.pensize(1)
turtle.pencolor('white')
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #ЛЕВОЕ ПЛЕЧО
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #ПРАВОЕ ПЛЕЧО
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) #ЛЕВАЯ ЗВЕЗДА В ПОЯСЕ
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) #CРЕДНЯЯ ЗВЕЗДА
turtle.write('Альнилам')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) #ПРАВАЯ ЗВЕЗДА
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #ЛЕВОЕ КОЛЕНО
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) #ПРАВОЕ КОЛЕНО
turtle.write('Ригель')

#НАНЕСТИ ЛИНИЮ ИЗ ЛЕВОГО ПЛЕЧА В ЛЕВУЮ ЗВЕЗДУ ПОЯСА
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

#Нанести линию из правого плеча в правую звезду пояса
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

#Нанести линию из левой звезды пояса в среднюю звезду пояса
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

#Нанести линию из седней звезды пояса в правую звезду пояса
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

#Нанести линию из левой звезды пояса в левое колено
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

#Нанести линию из правой звезды пояса в правое колено
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

turtle.done()