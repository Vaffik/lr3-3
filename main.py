print("Введите день: ", end = "")
day = int(input()) #запрашивается день
print("Введите месяц: ", end = "")
month = int(input()) #запрашивается месяц
if(month < 0 or day < 0):
    print("Неверная дата")
elif (month == 1 and day < 32) or (month == 2 and day < 30) or (month == 12 and day < 32):  #проверка зимних месяцев
    print(f"{day}.{month} - Зима")
elif (month == 3 and day < 32) or (month == 4 and day < 31) or (month == 5 and day < 32): #проверка весенних месяцев
    print(f"{day}.{month} - Весна")
elif (month == 6 and day < 31) or (month == 7 and day < 32) or (month == 8 and day < 32): #проверка летних месяцев
    print(f"{day}.{month} - Лето")    
elif (month == 9 and day < 31) or (month == 10 and day < 32) or (month == 11 and day < 31): #проверка осенних месяцев
    print(f"{day}.{month} - Осень")
else:
    print("Неверная дата")