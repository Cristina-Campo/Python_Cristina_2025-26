#Utilizzando un menu di  scelta crea una lista della spesa fornendo le seguenti funzionalità
#1 - Aggiungi un elemento
#2 - mostra lista
#3 - rimuovi un elemento
#4 - conta prodotti
#5 - pulisci lista

print("<<<<<< GESTIONE LISTA DELLA SPESA >>>>>>")
print("MENU - Fai la tua scelta")
scelta = ""

lista_spesa = ["uova","pasta","verza","succo di mela","taralli"]

#Aggiungi un elemento
def aggiungi_prodotto(prodotto):
    lista_spesa.append(prodotto)

#Mostra lista
def mostra_lista():
    for i in range(len(lista_spesa)):
        print(f"- {lista_spesa[i]}")

#Rimuovi un elemento
def rimuovi_prodotto(prodotto):
    lista_spesa.remove(prodotto)

#Conta i prodotti
def conta_prodotti():
    len_lista = len(lista_spesa)
    return len_lista

#Pulisci lista
def pulisci_lista():
    lista_spesa.clear()            


while scelta != 5:
    print("\n - Menu -")
    print("1. Aggiungi un elemento")
    print("2. Mostra lista")
    print("3. Rimuovi un elemento")
    print("4. Conta prodotti")
    print("5. Pulisci lista")

    scelta = int( input("Scegli: \n"))

    if scelta == 1:
        prodotto = str(input("Inserisci il prodotto da aggiungere: "))
        aggiungi_prodotto(prodotto)
        print(f"{prodotto} è stato aggiunto alla lista.")
    elif scelta == 2:
        print("La tua lista della spesa contiene:")
        mostra_lista()
    elif scelta == 3:
        prodotto = str(input("Inserisci il prodotto da rimuovere: "))
        rimuovi_prodotto(prodotto)
        print(f"{prodotto} è stato rimosso dalla lista.")
    elif scelta == 4:
        print(f"La tua lista contiene {conta_prodotti()} prodotti.")
    elif scelta == 5:
        pulisci_lista()
        print("La lista è stata pulita.")
    else:
        print("Non ho capito la scelta")

print("Programma terminato")
