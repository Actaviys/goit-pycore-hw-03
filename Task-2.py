from random import randint


def get_numbers_ticket(min, max, quantity): # Функція для генерування списку чисел
    try: # Пробую зберегти вхідні дані як int (Перевіряю чи ввели числа)
        min = int(min)
        max = int(max)
        quantity = int(quantity)
    
        if min <= 0 or max >= 1000 or quantity >= max: #Перевірка коректності введених параметрів
            return f"Невірні параметри" #Виводжу попередження 
        
        num = 0
        res = []
        while quantity > 0: #Цикл для створення списку випадкових чисел
            num = randint(min, max) #Зберігаю число для перевірки
            res.append(num) #Добавляю Число в список
            
            for r in res: #Читаю список для перевірки на співпадіння
                if r == num: #Якщо є співпадіння то замінюю число
                    res.remove(r) #Видаляю співпадіння
                    rand = randint(min, max) #Зберігаю нове випадкове число 
                    res.append(rand) #Додаю випадкове число
                    
                    for rr in res: #Ще раз читаю список на співпадіння
                        if rr == rand: #Якщо є співпадіння то замінюю число
                            res.remove(rr) #Видаляю співпадіння
                            rand = randint(min, max) #Зберігаю нове випадкове число 
                            if rand == rr: #Якщо попереднє число дорівнює новому то ще раз генерую число
                                rand = randint(min, max) #Зберігаю нове випадкове число

                            res.append(rand) #Додаю випадкове число
                            
            quantity -= 1 #Віднімаю від quantity по 1 за ітерацію
    
        res.sort() #Сортую список
        return res #Виводжу результат
    
    except: return "Введіть числа" #Повертаю помилку





inp_min = input("Введіть мінімальне число-> ")
inp_max = input("Введіть максимальне число-> ")
inp_quantity = input("Введіть кількість випадкових чисел чисел-> ")
lottery = get_numbers_ticket(inp_min, inp_max, inp_quantity)

print("Ваші лотерейні числа:", lottery)