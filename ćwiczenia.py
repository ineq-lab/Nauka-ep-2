# 1.Character Input
name = str(input('Enter the name ')).capitalize()
age = int(input('Enter your age '))
year100 = 2020 + (100 - age)
copies = 11
while 10 < copies or copies < 1:
    copies = int(input('Enter the digit 1-10 '))
    if 10 < copies or copies < 1:
        print('Error try again')
    else:
        print(copies * ('\nHey {} in the year {} you will turn 100 years'.format(name, year100)))

# 2.Odd or even
number = int(input('Enter the number '))
if number % 4 == 0:
    print('Number is multiple of 4')
elif number % 2 == 0:
    print('The number is even')
elif number % 2 != 0:
    print('The number is odd')
num = int(input('Enter the number '))
check = int(input('Enter the number '))
if num % check == 0:
    print('Number divide evenly')
else:
    print('Number not divide evenly')

# 3.List Less Than Ten
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for nums in a:
    if nums < 10:
        print(nums)
print('Lista z a', [nums for nums in a if nums < 10])
new_list = []
for i in a:
    if i < 10:
        new_list.append(i)
print('Nowa lista ', new_list)
number = int(input('Enter the number 10-89 '))
new_list = []
for i in a:
    if number > i:
        new_list.append(i)
print('Lista z liczby {}'.format(number), new_list)

# 4.Divisors
number = int(input('Enter the number '))
divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)
print('Lista dzielników:', divisors)
# 5.List overlap
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for x in b:
    c.append(x)
print(c)
for x in a:
    if x not in b:
        c.append(x)
print(c)
import random

a.clear()
b.clear()
c.clear()
