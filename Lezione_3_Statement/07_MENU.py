import os
import time

# definisco la funzione per il gioco dell'impiccato
def gioco_impiccato():
    parola = "appartamento"

    parolaARR = [] #Questo mi serve per trasformare la parola in un array
    arrayVuoto = [] #Questo mi serve per nascondere la parola

    #Questo for trasforma la parola in un array e riempi l'array vuoto di trattini quante sono le lettere di parola
    for lett in parola:
        parolaARR.append(lett)
        arrayVuoto.append("_")


    # print(parolaARR)
    print("La parola da cercare è\n",arrayVuoto)

    tentativi = 0


    while(tentativi <= 6):
        letteraCercata = input("Inserisci una lettera")

        for i in range(len(parolaARR)):
            if(letteraCercata == parolaARR[i]):
                print(f"Trovata la lettera {letteraCercata} in posizione {i + 1}")
                arrayVuoto[i] = letteraCercata
                print(arrayVuoto)
                continue
                
        if not parolaARR.__contains__(letteraCercata):
            tentativi += 1
            print(f"Ti restano {6 - tentativi} tentativi")
        
        parolaUnita = "".join(arrayVuoto)
        print(parolaUnita)
        
        if(parolaUnita == parola):
            print("Bravo, hai trovato la parola")
            break


def pulisci():
    os.system('cls' if os.name == 'nt' else 'clear')

# QUI INIZIA IL MENU
print("=== MENU, fai la tua scelta ===\n")

scelta = ""

while scelta != 4:
    pulisci()
    print("Menu")
    print("1. Gioca al gioco dell'impiccato")
    print("2. Gioca con i dadi")
    print("3. Gioca con il pc")
    print("4. ESCI")

    scelta = int( input("Scegli: \n"))

    if scelta == 1:
        gioco_impiccato()
    elif scelta == 2:
        print("Stai lanciando i dadi...")
        time.sleep(2)
    elif scelta == 3:
        print("Stai giocando a solitario")
    elif scelta == 4:
        print("Ciao, alla prossima")
    else:
        print( "Non ho capito la scelta!! ")

print("Programma terminato")

# Testo di fine file
