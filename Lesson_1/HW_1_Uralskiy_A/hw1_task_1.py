# https://drive.google.com/file/d/1d5aNHKa0rKZX3QE49UaQ_Dxfxf61tIl5/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трёхзначное число: '))

s = (a % 10)
a = a // 10

s = s + (a % 10)
a = a // 10

s = s + a

print(s)
