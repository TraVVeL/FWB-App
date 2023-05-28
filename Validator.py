import re
from datetime import datetime


def is_card(card_num):
    # Удаляем все пробелы и дефисы из номера карты
    card_num = card_num.replace(' ', '').replace('-', '')

    # Проверяем, что после удаления ненужных символов мы получили строку, содержащую только цифры
    if not card_num.isdigit():
        return False

    # Проверяем, что длина номера карты соответствует одному из стандартных форматов
    if (len(card_num) == 16 or len(card_num) == 15) and card_num[0] in ['3', '4', '5']:
        return True
    return False


def is_cvv(cvv):
    if len(cvv) != 3:
        return False
    try:
        int(cvv)
    except ValueError:
        return False
    return True


def is_card_date(card_date):
    # Проверяем, соответствует ли введенная строка формату MM/YY
    if not re.match(r'^\d{1,2}/\d{2}$', card_date):
        return False

    try:
        # Пробуем распарсить дату из строки
        date = datetime.strptime(card_date, '%m/%y')

        # Проверяем, что дата не меньше текущей
        if date < datetime.now():
            return False

        return True
    except ValueError:
        return False


def conc_card(card):
    card = card.replace('-', '').replace(' ', '')
    parts = [card[i:i + 4] for i in range(0, len(card), 4)]
    result = ' '.join(parts)
    return result


def is_digit(input_string):
    try:
        float(input_string)
        if float(input_string) > 0:
            return True
        return False
    except ValueError:
        return False

