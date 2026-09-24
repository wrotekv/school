#imie = input("Jak masz na imie? ")
#wiek = int(input("Ile masz lat? "))

#za_rok = wiek + 1
#print(imie + ", za rok będziesz miał " + str(za_rok) + " lat")


#cena = float(input("Jaka jest cena produktu? "))
#sztuki = int(input("Ile posiadasz sztuk produktu? "))

#wynik = cena * sztuki
#print("Calkowity koszt to: " + str(round(wynik,3)) + " zl")


#temperatura_c = float(input("Podaj temperature w Celcjuszach: "))

#temperatura_f = temperatura_c * 1.8 + 32
#print("Podana temperatura w Farenheitach to: " + str(round(temperatura_f,3)))

temperatura_f = float(input("Podaj temperature w Farenheitach: "))

temperatura_c = (temperatura_f - 32) * 5/9
print("Podana temperatura w Celcjuszach to: " + str(round(temperatura_c,3)))