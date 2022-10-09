"""Проверка даты на действительность."""


def date_checker(date):
    """Функция проверки даты.

    Args:
        date(str): дата в формате дд.мм.гггг
    """
    if (date[6:].isdigit() or (date[7:].isdigit() and date[6] == '-')):
        if ((date[0:2] + date[3:5]).isdigit() and (date[2] + date[5]) == '..'):
            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:])
            month1 = 13 > month > 0
            year1 = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
            day1 = (32 > day > 0) and (month in [1, 3, 5, 7, 8, 10, 12])
            day2 = (31 > day > 0) and (str(month) in [4, 6, 9, 11])
            day3 = (29 > day > 0) and (month == 2)
            day4 = (day == 29 and year1)
            days = day1 or day2 or day3 or day4
            return (month1 and days)
