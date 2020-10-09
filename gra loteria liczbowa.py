import random

gramy = 'tak'
podane = []
wylosowane = []
while gramy == 'tak':
    for i in range(6):
        podane.append(int(input('Podaj liczbe numer ' + str(i + 1) + ':')))
        wylosowane.append(random.randint(1, 20))
    trafione = 0
    for z in podane:
        for j in wylosowane:
            if z == j:
                trafione = trafione + 1

    print('Twoj wynik to: ', trafione)
    print('Wylosowane liczby:' + str(list(wylosowane)))
    podane.clear()
    wylosowane.clear()
    gramy = str(input('Czy chcesz zagrac jeszcze raz? tak/nie '))
    if gramy == 'nie':
        exit('Koniec programu')


