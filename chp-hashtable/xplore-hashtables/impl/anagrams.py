'''
Duas palavras sao anagramas se o resultado de ordenacao
do caracteres for o mesmo
'''


def is_anagram(str_a, str_b):
    return sorted(str_a) == sorted(str_b)


print(is_anagram("lives", "levis"))
print(is_anagram("algorithm", "logarithm"))
print(is_anagram("plgorithm", "logarithm"))

if __name__ == '__main__':
    pass
