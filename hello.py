minimi_pituus = 37
kuhan_pituus = input("Kirjoita kuhan pituus")
kuhan_pituus = int(kuhan_pituus)
if kuhan_pituus < minimi_pituus:
    print("Laske kuha takaisin järveen. Se on alimittainen", minimi_pituus - kuhan_pituus, "cm")
else:
    print("Kuha on oikean pituinen")

hytti_luokka = input("Valitse laivan hytti luokka (LUX, A, B, C)")
if hytti_luokka == "lux":
    print("LUX on hytti, jossa on parveke yläkannella")
elif hytti_luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif hytti_luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif hytti_luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")

sukupuoli = input("Ilmoita sukupuoli")
hemoglobiini = float(input(("Ilmoita hemogolbiini")))
if sukupuoli.lower() == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")
if sukupuoli.lower() == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")

vuosi = int(input("Anna vuosiluku"))
if vuosi % 4 == 0:
    print("Vuosi on karkausvuosi!")
elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print("Vuosi on karkausvuosi!")
else:
    print("Vuosi ei ole karkausvuosi!")











