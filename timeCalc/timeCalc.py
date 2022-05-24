print() # этот принт для отступа

# получаем входные данные в секундах
time = int(input("Type number of seconds: "))

# далее производим перевод секунд в часы и минуты и дни

if time < 60:
    day = 0
    hours = 0
    min = 0
    sec = time 

elif time >= 60 and time < 3600:
    day = 0
    hours = 0
    min = time // 60
    sec = time % 60
    
elif time >= 3600 and time < 86400:
    day = 0
    hours = time // 3600
    min = time % 3600 // 60
    sec = time % 3600 % 60

elif time >= 86400:
    day = time // 86400
    hours = time % 86400 // 3600
    min = time % 86400 % 3600 // 60
    sec = time % 86400 % 3600 % 60

print()   
print(day, hours, min, sec, sep=':')