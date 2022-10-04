"""flake8 - придира. а модуль делает то, что делает функция."""


def lettercounter(inp):

    
    """Принимает слова через пробел, возвращает % слов, в которых заглавных букв больше."""
    words = inp.split(' ')
    big_word = 0
    for index in range(len(words)):
        upper = 0
        for letter in words[index]:
            if (letter.isupper()):
                upper += 1
        if upper >= len(words[index]) / 2:
            big_word += 1
    return ('{0}%'.format(big_word * 100 // (len(words))))
