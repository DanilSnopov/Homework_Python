"""Журнал капитана."""
from datetime import timedelta, date


def notes(year, month, day, noteslist):
    """Создает список из ежедневных записей.

    Args:
        year(int): год первой записи
        month(int): месяц первой записи
        day(int): день первой записи
        noteslist(list): список ежедневных записей
    """
    with open("Captain.txt", 'a') as fil:
        daynow = date(year, month, day)
        for note in noteslist:
            fil.write("{0}: {1}\n".format(str(daynow), note))
            daynow += timedelta(1)


notes(2001, 4, 28, ['one', 'two', 'three', 'four', 'five'])
