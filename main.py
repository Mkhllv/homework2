# exercise №1
n = int(input('How many pupil ? '))
k = int(input('How many apples ? '))
print(f'Stay: {k // n} \nBasket: {k % n}')
print()

# exercise №2
# import math
a = int(input('Students in first grade: '))
b = int(input('Students in second grade: '))
c = int(input('Students in third grade: '))
desk = (a + b + c) / 2
# # print(f'Total desks: {math.ceil(desk)}')
if (a + b + c) % 2 == True:
    print(f'{desk + 0.5}')
else:
    print(f'Total desks: {desk}')
print()

# Exercise №3
# variant №1
print(input('Enter the number: ')[-1::-1])
print()
# variant №2
a = int(input('Enter the number: '))
b = 0
while a > 0:
    c = a % 10
    a = a // 10
    b = b * 10
    b = b + c
print(f'Answer: {b}')
print()
# variant №3
a = int(input('Enter the number: '))
b = a % 10 * 100
print(b)
c = a // 10 % 10 * 10
print(c)
d = a // 10 // 10
print(d)
print(f'Answer: {b+c+d}')
print()

# Exercise №4
a = int(input('Seconds: '))
hour = a // 3600
residue = a % 3600
minutes = residue // 60
seconds = residue % 60
print(f'Full Time: {hour}:{minutes}:{seconds}')
