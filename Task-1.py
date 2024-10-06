from datetime import datetime as dt #Імпортую модуль datetime і називаю скорочено dt


def get_days_from_today(date): #Функція для вирвховування різниці між поточною і введеною датами
    res = 0 #Для результату
    dt_now = dt.now().date() #Зберігаю поточну дату
    
    try: #Перевіряю на правильний формат
        dt_date = dt.strptime(date, "%Y-%m-%d").date() #Зберігаю перетворене в datetime об'єкт введене значення
        res = dt_now - dt_date #Вираховую різницю
        return res.days #Повертаю результат
    
    except: return "Невірний формат \nВведіть у форматі (рррр-мм-дд)" #Якщо неправильний формат виводжу попередження


in_data = input("Введіть дату: ")
print("Днів:", get_days_from_today(in_data))