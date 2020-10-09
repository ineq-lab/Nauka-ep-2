
names = ['Janek', 'Arek', 'Adam', 'Ola', 'Kasia', 'Zenek']
name = str(input('Podaj imie ')).capitalize()
names = names + [name]
print(list(names))

for name in names:
    print('Cześć', name)

a = input('Podaj nazwe: ')
for x in a.split():
    print(x)