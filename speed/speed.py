# назначаение целевых перемнных

start_speed = 60 #начальная скорость
end_speed = 131 #конечная скорость
increment_step = 10 #шаг увеличения
conversion_factor = 0.6214 #коеффициент для перевода в мили/ч

#цикл

for speed in range (start_speed, end_speed, increment_step):
    speed = speed * conversion_factor
    print(format(speed, '.2f')) #вывод значения с форматом числа до
                                                    #двух знаков после зяпятой
