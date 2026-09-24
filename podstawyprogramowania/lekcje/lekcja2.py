sekundy = int(input("Podaj sekundy: "))
godziny = sekundy // 3600
minuty = (sekundy % 3600) // 60
sekundy %= 60
print(str(godziny) + " h " + str(minuty) + " m " + str(sekundy) + " s ")