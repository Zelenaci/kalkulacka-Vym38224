
import math
import tkinter as tk

from os.path import basename, splitext


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Kalkulačka")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Konec", command=self.quit)
        self.btn.pack()
        



zasobnik = []


def operace(token):
    if token.upper() == "Q":
        exit()
    if token.upper() == "PI":
        zasobnik.append(math.pi)
    if token == "+":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(a + b)
    if token == "-":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(a - b)
    if token == "*":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(a * b)
    if token == "**":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(a ** b)
    if token == "sin":
        a = zasobnik.pop()
        zasobnik.append(math.sin(a))
    if token == "cos":
        a = zasobnik.pop()
        zasobnik.append(math.cos(a))


dva_operandy = {}
dva_operandy["+"] = lambda a, b: a + b
dva_operandy["-"] = lambda a, b: a - b
dva_operandy["*"] = lambda a, b: a * b
dva_operandy["/"] = lambda a, b: a / b
dva_operandy["//"] = lambda a, b: a // b
dva_operandy["**"] = lambda a, b: a ** b

jeden_operand = {}
jeden_operand["sin"] = math.sin
jeden_operand["cos"] = math.cos
jeden_operand["tg"] = math.tan
jeden_operand["tan"] = math.tan


def operace(token):
    if token.upper() == "Q":
        exit()
    if token.upper() == "PI":
        zasobnik.append(math.pi)
    if token.upper() == "SW":
        b = zasobnik.pop()
        a = zasobnik.pop()
        zasobnik.append(b)
        zasobnik.append(a)
    if token in dva_operandy.keys():
        if len(zasobnik) >= 2:
            b = zasobnik.pop()
            a = zasobnik.pop()
            zasobnik.append(dva_operandy[token](a, b))
        else:
            print("Nemám dost operandů!!!")
    if token in jeden_operand.keys():
        if len(zasobnik) >= 1:
            a = zasobnik.pop()
            zasobnik.append(jeden_operand[token](a))
        else:
            print("Nemám dost operandů!!!")


def zpracuj(radek):
    tokeny = radek.split()
    for token in tokeny:
        try:
            zasobnik.append(float(token))
        except ValueError:
            operace(token)


# čtu vstup
while True:
    radek = input(zasobnik.__repr__() + ">>> ")
    zpracuj(radek)



    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()