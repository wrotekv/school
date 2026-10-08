#liczba = int(input("Podaj liczbe: "))

#if liczba % 2 == 0:
    #print("parzysta")
#else:
    #print("nie parzysta")

'''
punkty = int(input("podaj liczbe punktow"))

if 0 <= punkty <= 39:
    print("szmata")
elif 40 <= punkty <= 55:
    print("oporowo, 2")
elif 56 <= punkty <= 75:
    print("oporowo, 3")
elif 76 <= punkty <= 90:
    print("nawet ok")
elif 91 <= punkty <= 95:
    print("ladnie")
elif 96 <= punkty <= 100:
    print("jupi 6")
else:
    print("wpisz od 0-100")
'''

'''
def calc(a, b, dzialanie):
    if dzialanie == "+":
        print(a + b)
    elif dzialanie == "-":
        print(a - b)
    elif dzialanie == "*":
        print(a * b)
    elif dzialanie == "/" or dzialanie == "//" or dzialanie == ":":
        if b == 0:
            print("dzielenie przez 0 nie dziala")
            return
        print(a / b)
    elif dzialanie == "^" or dzialanie == "**":
        print(a ** b)
    elif dzialanie == "%":
        print(a % b)
    else:
        print("podaj dzialanie tylko np: %,*")

    return


l1 = input("Pierwsza liczba ")
l2 = float(input("Druga liczba "))
dzialanie = input("podaj dzialanie ")

calc(l1, l2, dzialanie)
'''

'''
a = int(input("Podaj a "))
b = int(input("Podaj b "))
c = int(input("Podaj c "))

if a + b > c and b + c > a and a + c > b:
    print("mozna zbudowac trojkat")
else:
    print("nie mozna")
'''

rok = int(input("Podaj rok "))
if rok % 400 == 0 or rok % 4 == 0 and rok % 100 != 0:
    print("rok jest przestepny")
else:
    print("rok nie jest przestepny")