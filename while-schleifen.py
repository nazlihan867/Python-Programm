# Programm, das den Benutzer auffordert, eine Zahl einzugeben, bis eine gerade Zahl eingegeben wird
while True:
    zahl = int(input("Bitte geben Sie eine Zahl ein: "))
    if zahl % 2 == 0:
        print(f"Die gerade Zahl ist: {zahl}")
        break

