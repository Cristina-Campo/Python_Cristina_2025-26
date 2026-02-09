#ESERCIZIO 1 - Calcolatrice base
#Utilizzando un menu di  scelta crea una calcolatrice di base co le 4 operazioni
#Ogni operazione è una funzioe a se stante
#Parametri: 2 numeri


print("<<<<<< CLCOLATRICE SEMPLICE >>>>>>")
print("MENU - Che operazione vuoi fare?")
scelta = ""

def somma(a,b):
    risultato = a+b
    return risultato

def sottrazione(a,b):
    risultato = a - b
    return risultato

def moltiplicazione(a,b):
    risultato = a * b
    return risultato

def divisione(a,b):
    risultato = a / b
    return risultato

while scelta != 4:
    print("\n - Menu -")
    print("1. ADDIZIONE")
    print("2. SOTTRAZIONE")
    print("3. MOLTIPLICAZIONE")
    print("4. DIVISIONE")
    print("5. ESCI")

    scelta = int( input("Scegli: \n"))

    if scelta == 1: #Somma
        x = int(input("Inserisci il primo numero: "))
        y = int(input("Inserisci il secondo numero: "))
        risultato_somma = somma(x,y)
        print(f"Il risultato della somma è: {risultato_somma}")
    elif scelta == 2:#Sottrazione
        x = int(input("Inserisci il primo numero: "))
        y = int(input("Inserisci il secondo numero: "))
        risultato_sottrazione = sottrazione(x,y)
        print(f"Il risultato della sottrazione è: {risultato_sottrazione}")
    elif scelta == 3:#Moltiplicazione
        x = int(input("Inserisci il primo numero: "))
        y = int(input("Inserisci il secondo numero: "))
        risultato_moltiplicazione = moltiplicazione(x,y)
        print(f"Il risultato della moltiplicazione è: {risultato_moltiplicazione}")
    elif scelta == 4:#Divisione
        x = int(input("Inserisci il primo numero: "))
        y = int(input("Inserisci il secondo numero: "))
        risultato_divisione = divisione(x,y)
        print(f"Il risultato della divisione è: {risultato_divisione}")
    else:
        print("Non ho capito la scelta")

print("Programma terminato")


