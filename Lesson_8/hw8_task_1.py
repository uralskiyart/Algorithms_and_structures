'''Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9'''


import hashlib


def substring_counter(s):
    repeat_subs_hash = []

    for i in range(len(s)):
        for j in range(i, len(s)):

            spam_hash = hashlib.sha256(s[i: j + 1].encode('utf-8')).hexdigest()
            if spam_hash not in repeat_subs_hash:
                repeat_subs_hash.append(spam_hash)

    return f'Ответ: {len(repeat_subs_hash) - 1}'


print(substring_counter('sova'))
