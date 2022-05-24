bookAmount = int(input("Введите количество приобретённых книг: "))

if bookAmount == 0 or bookAmount == 1:
    points = 0
elif bookAmount >= 2 and bookAmount <= 3:
    points = 5
elif bookAmount >= 4 and bookAmount <=5:
    points = 15
elif bookAmount >= 6 and bookAmount <= 8:
    points = 30
elif bookAmount >= 8:
    points = 80
    
print("Ваше количество очков", points)