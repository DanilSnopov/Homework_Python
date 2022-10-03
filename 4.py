x = input()
words = x.split(' ')
big_word = 0
for i in range(len(words)):
    upper = 0
    for letter in words[i]:
        if (letter.isupper()):
            upper += 1
    if upper >= len(words[i]) / 2:
        big_word += 1
print('{0}%'.format(big_word * 100 // (len(words))))
