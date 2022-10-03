def counter(inp):
    words = inp.split(' ')
    big_word = 0
    for index in range(len(words)):
        upper = 0
        for letter in words[index]:
            if (letter.isupper()):
                upper += 1
        if upper >= len(words[i]) / 2:
            big_word += 1
    return ('{0}%'.format(big_word * 100 // (len(words))))
