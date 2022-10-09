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
    notesdict = {}
    daynow = date(year, month, day)
    for note in noteslist:
        notesdict[str(daynow)] = note
        daynow += timedelta(1)
    return notesdict
