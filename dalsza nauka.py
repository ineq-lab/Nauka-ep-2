# -*- coding: utf-8 -*-

colours = ['red', 'blue', 'yellow', 'yellow', 'green', 'black', 'white']
plurals = ['sky', 'water', 'sea', 'T-shirt']
actors = ['Angelina Jolie', 'Jeniffer Lopez', 'Pamela Anderson', 'Megan Fox']
colours.pop(0)
print('Nr indeksu:', colours.index('white'))
print('lista:', colours)
print('ilość stringów tych samych', colours.count('yellow'))  # zlicza ile razy coś wystąpi to samo
colours.sort()
print(colours)
actors.reverse()
print(actors)


def sayhi(name, age):  # name,age to zmienne,parametry
    print('Hello', name, 'you are', age, 'years old')


sayhi('Jerry', 5)
sayhi('Tom', 30)


def cube(num):
    print('code')
    return num * num * num  # funkcja return zwraca wynik pod cube print po return  nie ma efektu


print(cube(2))


def max_num(num1, num2, num3):  # 3 różne zmienne
    if num1 >= num2 and num1 >= num3:
        return num1  # zwraca wynik spełnienia warunku if else i elif
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(10, 55, 329))

month_convers = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',
}
month_convers['Her'] = 'Herself'  # dodanie nowego klucza z wartością
month_convers.pop('Jan')  # usunięcie klucza wraz wartością
month_convers['Dec'] = 'Grudzień'  # modyfikacja wartośći klucz
print(month_convers.values())
i = 1
while i <= 20:  # wykonuj pętle zmiennej i gdy:
    print(i)
    i = i + 1
print("done loop")

date = str(1492)
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != date and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input('Data odkrycia Ameryki ')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print('Koniec szans przegrałeś')
else:
    print('To prawidłowa odpowiedź!')
