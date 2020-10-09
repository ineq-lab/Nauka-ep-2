a = 3
b = 10
while a < b:
    b = b + a
    a = a * 2 + 2
    print('a: ', a)
    print('b: ', b)
    print('######')

haslo = 'xxx'
while haslo != 'trzaslo':
    haslo = input('Podaj haslo: ')
    if haslo != 'trzaslo':
        print('Źle próbuj ponownie')
print('Udało ci sie!')

x = int(input('Ile razy chcesz próbować? '))
for i in range(x):
    a = int(input('Pierwsza liczba '))
    b = int(input('Druga liczba '))
    if a > b:
        print('Pierwsza liczba jest większa\n', i + 1, 'proba')
    elif a < b:
        print('Druga liczba jest większa\n', i + 1, 'próba')
    else:
        print('Liczby są sobie równe\n', i + 1, 'próba')
