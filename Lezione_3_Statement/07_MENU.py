print("=== MENU, fai la tua scelta ===\n")

scelta = ""

while scelta != 4:
    print("Menu")
    print("1. Gioca con i numeri")
    print("2. Gioca con i dadi")
    print("3. Gioca con il pc")
    print("4. ESCI")

    scelta = int( input("Scegli: \n"))

    if scelta == 1:
        print("Stai giocando con i numeri...")
    elif scelta == 2:
        print("Stai lanciando i dadi...")
    elif scelta == 3:
        print("Stai giocando a solitario")
    elif scelta == 4:
        print("Ciao, alla prossima")
    else:
        print( "Non ho capito la scelta!! ")

print("Programma terminato")

# Testo di fine file