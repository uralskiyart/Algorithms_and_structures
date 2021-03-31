''') Закодируйте любую строку по алгоритму Хаффмана.'''

import heapq
from collections import Counter, namedtuple


class Node(namedtuple(('Node'), ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple(('Leaf'), ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def code_table(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq_1, count_1, left = heapq.heappop(h)
        freq_2, count_2, right = heapq.heappop(h)
        heapq.heappush(h, (freq_1 + freq_2, count, Node(left, right)))
        count += 1

    [(freq, count, root)] = h
    code_table = {}
    root.walk(code_table, "")

    return code_table


def encode(s, code):
    return ''.join(code[ch] for ch in s)


def decode(enc_str, code):
    dec_str = ''
    i = 0
    pivot = 0

    for i in range(len(enc_str)):
        spam = enc_str[pivot: i + 1]

        for dec_ch, enc_ch in code.items():
            if enc_ch == spam:
                dec_str += dec_ch
                pivot = i + 1
                break

    return dec_str


def main():
    s = str(input('Введите строку: '))
    code = code_table(s)
    print(5 * '*', ' КОДИРОВКА ', 5 * '*')
    for ch in sorted(code):
        print(f'{ch} - {code[ch]}')

    s = encode(s, code)
    print(f'Строка закодирована: {s}')

    s = decode(s, code)
    print(f'Строка декодирована: {s}')


if __name__ == '__main__':
    main()
