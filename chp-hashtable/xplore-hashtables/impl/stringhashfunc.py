from functools import reduce

'''
https://docs.python.org/3/library/functools.html
reduce(function x, y, operation, seq, initializer)
x = valor acumulador
y = i-esima valor da estrutura sequencial
operation = operacao que sera feita com os valores da estrutura sequencial
seq = estrutura sequencial
initializer = valor opcional que eh usado como retorno caso a estrutura
sequencial esteja vazia 
'''

_mod = (1 << 12)

'''
ord: https://docs.python.org/3/library/functions.html#ord
recebe um caracter como argumento e retorna um valor inteiro que representa o valor Unicode deste caracter
chr: https://docs.python.org/3/library/functions.html#chr
recebe um inteiro como argumento que representa um valor Unicode de um determinado caracter
e se estiver dentro do intervalo (0 a 1.114.111(0x10FFFF)) retorna o caracter corresponde ao unicode
'''


def string_hash(_str):
    return reduce(lambda v, c: (v * 1023 + ord(c)) % _mod, _str, 0)


def string_hash_2(_str):
    acc = 0
    for _chr in _str:
        acc = (acc * 1023 + ord(_chr)) % _mod
    return acc


def test_chr_function():
    return [chr(i) for i in range(0x10FF90, 0x110000)]


print(string_hash("christoffer"))
print(string_hash_2("christoffer"))
print(string_hash("christoerff"))
print(string_hash_2("christoerff"))
#print(test_chr_function())

if __name__ == '__main__':
    pass
