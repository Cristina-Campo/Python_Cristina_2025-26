#Crea una lista della spesa con almeno 6 prodotti
#Mostra gli elementi della lista uno alla volta
#Cerca se esiste un prodotto nella lista (DARE ANCHE LA POSSIBILITÀ DI INSERIRE IL PRODOTTO TRAMITE INPUT)
#Conta quanti prodotti ci sono
#Mostra solo i prodotti con più di 5 lettere
#Crea una nuova lista di prodotti uguale a quella di prima ma tutto in MAIUSCOLO 

#Crea la lista

listaSpesa = ["Tortiglioni" , "Besciamella" , "Mandarini" , "Uva" , "Prosciutto" , "Pane" , "Prosecco" , "Yogurt" , "Pizza"]

#Stampa la lista della spesa

for prodotti in listaSpesa:
    print(prodotti)

#Cerca un prodotto all'interno dell'array

ricerca = input("Quale pordotto vorresti cercare all'interno della lista?  ")

if ricerca in listaSpesa:
    print("Eccolo!")
else:
    print("404")    


#Conta quanti prodotti ci sono

LunghezzaSpesa = len(listaSpesa)
print(f"Ci sono {LunghezzaSpesa} prodotti segnati sulla tua lista")


#Mostra solo i prodotti con più di 5 lettere

ultimoProdotto = listaSpesa[len(listaSpesa) - 1]
print(ultimoProdotto)

for i in range(0,len(listaSpesa)):
    if len(listaSpesa[i]) > 5:
        print(listaSpesa[i])
        i += 1
    else:
        i +=1    


#Crea una nuova lista di prodotti uguale a quella di prima ma tutto in MAIUSCOLO

print("Se ci vedi male ti ristampo la lista in maiuscolo")
print([listaSpesa.upper()])