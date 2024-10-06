from datetime import datetime, timedelta

#Словники з користувачами і ДН 
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Dima Ilin", "birthday": "2002.10.07"},
    {"name": "Willy Wonka", "birthday": "1997.10.06"}
]


def get_upcoming_birthdays(users: list[dict]) -> list[dict]: #Функція для пошу ДН з на цьому тижні з поправкою на вихідні
    today = datetime.today().date() #Зберігаю поточну дату
    results = [] #Змінна для результату
    
    for user in users: #Читаю список
        birthday = datetime.strptime(user["birthday"], '%Y.%m.%d').date() #Перетворюю ДН з словника в об'єкт datetime
        birt_year = birthday.replace(year=today.year) #Витягую рік з ДН
        week_day = birt_year.weekday() #Зберігаю день тижня
        
        res_bird = int((birt_year - today).days) #Віднімаю поточну дату від ДН
        if res_bird <= 7 and res_bird >= 0: #Перевіряю чи на цьому тижні ДН
            
            if week_day > 4: #Перевіряю чи попадає ДН на вихідні якщо так то додаю різницю між ДН і днем тижня
                day_off = 7 - week_day #Різниця між днем тижня і ДН
                birthday = birthday + timedelta(days=day_off) #Додаю різницю до ДН
            
            dict_res = {"name": user["name"], "congratulation_date": str(birthday)} #Створюю словник з відкорегованими та перевіреними ДН
            results.append(dict_res) #Добавляю перевірені ДН до результату
            
    return results #Повертаю результат


print("Список привітань на цьому тижні:", get_upcoming_birthdays(users)) #Виводжу результат

