#Scrivi un programma per gestire una lista della spesa.
#1. Crea una lista della spesa con almeno 6 prodotti
#2. Mostra i prodotti della lista uno alla volta
#3. Cercare se esiste un prodotto nella lista (dare anche la possibilità all'utente di inserire a mano il prodotto tramite input)
#4. Contare quanti sono i prodotti presenti
#5. Mostrare solo i prodotti con più di 5 lettere
#6. Creare una nuova lista di prodotti con i precedenti ma in maiuscolo
#7. Aggiungi un prodotto alla lista chiedendo all'utente il nome del prodotto
#8. Rimuovi un prodotto a scelta dell'utente
#9. Tutto questo fallo in un menu dal quale l'utente seleziona i comandi

#Creazione lista
#listaSpesa = ["Tortiglioni 🍝" , "Latte 🥛" , "Mandarini 🍊" , "Uva 🍇" , "Prosciutto 🐖" , "Pane 🍞" , "Prosecco 🍾" , "Yogurt 🍮" , "Pizza 🍕", "Shampoo 🫧"]
listaSpesa = ["tortiglioni" , "latte" , "mandarini" , "uva" , "prosciutto" , "pane" , "prosecco" , "yogurt" , "pizza", "shampoo"]
emoji = ["🍝" , "🥛" , "🍊" , "🍇" , "🐖" , "🍞" , "🍾" , "🍮" , "🍕" , "🫧", "‼️"]

#Stampo menu di scelta
print("MENU - Benvenuto nella tua app di gestione della lista della spesa. Cosa desideri fare?")
scelta = ""

while scelta != 7:
    print("\n - Menu -")
    print("1. Mostra lista della spesa")
    print("2. Ricerca un prodotto nella lista")
    print("3. Conta quanti elementi ci sono nella lista")
    print("4. Mostra solo i prodotti con più di 5 lettere")
    print("5. Stampa la lista in MAIUSCOLO")
    print("6. Aggiungi un nuovo prodotto alla lista")
    print("7. Rimuovi un prodotto dalla lista")

    scelta = int( input("Scegli: \n"))

    if scelta == 1:
#Stampo lista
        print(" ")
        for i in range(len(listaSpesa)):
            print(f"- {listaSpesa[i]} {emoji[i]}")


    elif scelta == 2:
#Cerca un prodotto all'interno dell'array
        ricerca = input("Quale pordotto vorresti cercare all'interno della lista?  ").lower()

        if ricerca in listaSpesa:
            print(f"Trovato!✅ {ricerca} è nella lista")
        else:
            print(f"{ricerca} non si trova nella lista ❌")        

    elif scelta == 3:
#Conteggio del numero di elementi nell'array
        print(" ")
        LunghezzaSpesa = len(listaSpesa)
        print(f"Al momento ci sono {LunghezzaSpesa} prodotti segnati sulla tua lista")

    elif scelta == 4:
#Mostra solo i prodotti con più di 5 lettere
        print("Questi sono i prodotti che contengono più di 5 lettere.")
        ultimoProdotto = listaSpesa[len(listaSpesa) - 1]
        print(ultimoProdotto)

        for i in range(0,len(listaSpesa)):
            if len(listaSpesa[i]) > 5:
                print(f"- {listaSpesa[i]} {emoji[i]}")
                i += 1
            else:
                i +=1    

    elif scelta == 5:
#Creazione della lista della spesa ma in maiuscolo
        print("")
        print("**CAPS LOCK**")
        for i in range(len(listaSpesa)):
            print(f"{listaSpesa[i].upper()} {emoji[i]}")

    elif scelta == 6:
#Aggiungo un prodotto alla lista chiedendo all'utente il nome del prodotto
        add = input("Scrivi cosa desideri aggiungere al fondo della lista: ")
        listaSpesa.append(add)
        for i in range(len(listaSpesa)):
            print(f"- {listaSpesa[i]} {emoji[i]}")        
        #Ristampo il numero di elementi nella lista
        print(" ")
        LunghezzaSpesa = len(listaSpesa)
        print(f"Al momento ci sono {LunghezzaSpesa} prodotti segnati sulla tua lista")    

    elif scelta == 7:
#Rimuovo un prodotto dalla lista
        print(" ")
        remove = input("Cosa desideri rimuovere dalla lista? ")
        listaSpesa.remove(remove)
        for i in range(len(listaSpesa)):
            print(f"- {listaSpesa[i]} {emoji[i]}") 

print("Programma terminato")                   
