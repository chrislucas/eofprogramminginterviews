'''
https://docs.python.org/3/library/heapq.html
http://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
'''

'''
Pseudo Random numbers
https://docs.python.org/3/library/random.html
'''

from random import randint
from heapq import heapify, heappush

'''
algoritmo de knuth para embaralhar um array de tamanho N
https://algs4.cs.princeton.edu/code/
https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/Knuth.java.html
'''


def get_sample_list(_size):
    _l = [x for x in range(0, _size)]
    for i in range(0, _size):
        p = randint(i, _size - 1)
        aux = _l[i]
        _l[i] = _l[p]
        _l[p] = aux
    return _l


def build_heap(_list):
    _list_2 = []
    for x in _list:
        heappush(_list_2, x)
    return _list_2


_list = get_sample_list(11)
print(_list)
build_heap(_list)
print(_list)

if __name__ == '__main__':
    pass
