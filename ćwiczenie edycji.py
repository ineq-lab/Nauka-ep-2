names = ['Janek', 'Arek', 'Adam', 'Ola', 'Kasia', 'Zenek']
# sortowanie i odwrócenie bez print inaczej wyjdzie none
names.sort()
names.reverse()
print(names)
for i in names:
    print('Siema!', i)
a = names[2].swapcase().replace('a', '').__add__(' kamienia').lower()
b = names[3].replace('O', 'Wio')
c = names[4].rstrip('ia').__add__('jana')
names = names + [a, b, c] + ['Wiesiek', 'Henryk', 'Tadzik']
print(names)
for j in names:
    print(j.upper())
txt = 'Pociąg sobie jechal i uderzył w drzewo'
message = 'wiadomośćzostaławyslana'

txt = [txt, message]
print(txt)
names.remove(a)
print(names)
names.append(b)
names.insert(6, 'Polibuda')  # wpierw indeks gdzie wstawić później str lub zmienną
print(names)
names.pop(0)  # podaje sie indeks
names.remove(c)  # podaje sie string lub zmienna
names.sort()
print('Ilość argumentów: ', len(names))
names[7:] = ['Podolskie wieśniactwo']
names[4] = 'Barabara'
names[5] = 'Lechu'
names[-5] = 'Janusz'
print(names)
digits = []
dig = 5, 234, 547, 123, 687, 234, 675467, 323, 664, 3245, 63, 32, 5, 23, 443, 55
for i in dig:
    (digits.append(i))
    print(digits)
