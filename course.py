def moc(liczba, pow):
    wynik = 1
    for x in range(pow):
        wynik = wynik * liczba
    return wynik


print(moc(9, 7))


def gra():
    haslo = ''
    limit_szans = 3
    szanse = 0
    while haslo != 'moneta' and limit_szans != szanse:
        haslo = input('Podaj hasło: ')
        szanse += 1
        if haslo == 'moneta':
            answer = input('To prawidłowa odpowiedź,chcesz rozpocząć jeszcze raz? t/n? ')
            if answer == 't':
                haslo = ""
                szanse = 0
            elif answer == 'n':
                exit('Koniec programu')
        elif haslo != 'moneta' and limit_szans != szanse:
            print('Źle próbuj ponownie')
    else:
        print('Koniec gry,straciłeś wszystkie szanse')
        answer = input('Chcesz zagrać jeszcze raz? t/n? ')
        if answer == 't':
            gra()
        elif answer == 'n':
            exit('Koniec programu')


gra()
