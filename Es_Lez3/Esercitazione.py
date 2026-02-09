#Scrivi un programma per gestire una lista della spesa (inserisci in partenza almeno 6 prodotti). Tutto questo fallo in un menu dal quale l'utente seleziona i comandi

#2. Mostra i prodotti della lista uno alla volta
#3. Cercare se esiste un prodotto nella lista (dare anche la possibilità all'utente di inserire a mano il prodotto tramite input)
#4. Contare quanti sono i prodotti presenti
#5. Mostrare solo i prodotti con più di 5 lettere
#6. Creare una nuova lista di prodotti con i precedenti ma in maiuscolo
#7. Aggiungi un prodotto alla lista chiedendo all'utente il nome del prodotto
#8. Rimuovi un prodotto a scelta dell'utente

lista = ["dario", "cristina", "marco"]
cosaDaCercare = input("Cosa vuoi cercare ? ")

for i in range(len(lista)):
    if cosaDaCercare == lista[i]:
        print("Trovato")

for cosa in lista:
    if cosa == cosaDaCercare:
        print("Trovato")