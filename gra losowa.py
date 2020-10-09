from tkinter import *
import random

t = Tk()
t.title("Wybierz przycisk")
t.geometry("250x300")


def wstaw_przyciski():
    ile_przyciskow = 8
    global przyciski
    przyciski = []
    dobry = random.randint(0, ile_przyciskow - 1)
    for i in range(ile_przyciskow):
        if i == dobry:
            przyciski.append(Button(t, text="trafiony", command=trafiony))
        else:
            przyciski.append(Button(t, text="pudlo", command=pudlo))
    for i in przyciski:
        i.pack(fill=BOTH, expand=YES)


def trafiony():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text="Trafiłeś dobry przycisk")
    etykieta.pack(fill=BOTH, expand=YES)
    t.after(1000, restart)


def pudlo():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text="Trafiłeś zły przycisk")
    etykieta.pack(fill=BOTH, expand=YES)
    t.after(500, restart)


wstaw_przyciski()


def restart():
    etykieta.destroy()
    wstaw_przyciski()


t.mainloop()
