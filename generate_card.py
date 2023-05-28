import random
import datetime


def generate_credit_card_number():
    """Генерация случайного номера кредитной карты"""
    number = "4"  # Номер Visa-карты начинается с цифры 4
    for i in range(1, 16):
        if i % 4 == 0:
            number += ' '
        number += str(random.randint(0, 9))
    return number


def generate_cvv():
    """Генерация случайного CVV-кода"""
    return str(random.randint(100, 999))


def generate_expiry_date():
    """Генерация даты окончания срока действия кредитной карты"""
    current_year = datetime.date.today().year
    expiry_year = current_year + 5  # Дата окончания - через два года от текущей
    expiry_month = datetime.date.today().month
    if expiry_month == 12:  # Если текущий месяц - декабрь, то следующий месяц - январь нового года
        expiry_month = 1
        expiry_year += 1
    else:
        expiry_month += 1
    return "{:02d}/{:02d}".format(expiry_month, expiry_year % 100)  # Возвращаем дату в формате MM/YY
