"""Модуль делает то, что делает функция."""


def lettercounter(inp):
    """Принимает.

    Args:
        inp(string): несколько слов, разделенных пробелами

    возвращает: % слов, в которых заглавных букв больше.
    """
    words = inp.split(' ')
    big_word = 0
    for index in list(enumerate(words)):
        upper = 0
        for letter in words[index[0]]:
            if (letter.isupper()):
                upper += 1
        if upper >= len(words[index[0]]) / 2:
            big_word += 1
    return ('{0}%'.format(big_word * 100 // (len(words))))
