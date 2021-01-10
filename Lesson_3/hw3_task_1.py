# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9.


array = [i for i in range(2, 100)]
print(array)

for i in range (2, 10):
    res = len([j for j in array if j % i == 0])
    print(f'{res} чисел кратных {i}')
