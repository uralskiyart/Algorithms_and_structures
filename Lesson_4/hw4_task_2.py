import timeit
import math
import cProfile

def sieve(n):
    if n == 1:
        return 2

   # k = 1 / (n * 2 / (n * 1.333) * (len(str(n)) * 10))

    sieve = [i for i in range(int(n ** 1.7))]
    HOLE = 0
    sieve[1] = 0

    for i in range(2, int(n ** 1.7)):
        if sieve[i] != HOLE:
            j = i * 2
            while j < int(n ** 1.7):
                sieve[j] = HOLE
                j += i

    sieve = [i for i in sieve if i != 0]

    return sieve[n - 1]


def prime(n):
    # k =  1 / (n * 1.333 / (len(str(n**2)) * 10))
    # print(k)
    arr = [2, 3, 5, 7]


    for i in range(8, int(n ** 1.7)):
        if i % 2 != 0 or i % 3 != 0 or i % 5 != 0 or i % 7 != 0:
            for j in arr:
                if i % j == 0:
                    break
            else:
                arr.append(i)

    return arr[n - 1]

print(sieve(10))
print(prime(10))

print(timeit.timeit('sieve(10)', number=100, globals=globals()))
print(timeit.timeit('sieve(20)', number=100, globals=globals()))
print(timeit.timeit('sieve(40)', number=100, globals=globals()))
print(timeit.timeit('sieve(80)', number=100, globals=globals()))


print(timeit.timeit('prime(10)', number=100, globals=globals()))
print(timeit.timeit('prime(20)', number=100, globals=globals()))
print(timeit.timeit('prime(40)', number=100, globals=globals()))
print(timeit.timeit('prime(80)', number=100, globals=globals()))


# cProfile.run('sieve(1000)')
#
# cProfile.run('prime(1000)')
