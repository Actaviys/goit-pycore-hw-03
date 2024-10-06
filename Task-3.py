import re

#Список номерів
phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    " 5803-565gh35e33",
    "335634"
]

def normalize_phone(phone) -> list:
    number = str(''.join(re.findall(r"[+0-9]", phone))) #Витягую всі потрібні символи з рядка в список і перетворюю одразу в рядок
    num_len = len(number) #Зберігаю в змінну кількість символів в номері
    
    if num_len < 10 or num_len > 13: # Роблю перевірку на коректність номера
        return f"Невірний номер: {number}" #Повертаю помилку
    
    #Добавляю символи міжнародного коду в залежності від кількості символів
    if num_len == 12: number = f"+{number}" #Добавляю + 
    if num_len == 11: number = f"+3{number}" #Добавляю +3
    if num_len == 10: number = f"+38{number}" #Добавляю +38
    
    return number #Повертаю номер


sanitized_numbers = [normalize_phone(num) for num in phone_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
