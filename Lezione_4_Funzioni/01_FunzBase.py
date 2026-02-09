# FUNZIONI: blocco di codice riutilizzabile che esegue delle istruzioni specifiche. Le funzioni possono essere richiamate da qualsiasi punto del mio codice

#SINTASSI
#dichiaro una funzione
def nome_funzione():
    #Corpo della funzione
    print("Ciao dalla funzione")

#richiamo la funzione
nome_funzione() #Output: "Ciao dalla funzione"


#dichiaro una funzione con parametri
def saluta_qualcuno(nome):
    print(f"Ciao {nome}")

nome_persona = input("Chi vuoi salutare ??")
saluta_qualcuno(nome_persona)

#dichiaro una funzione con più parametri
numeroFortunato = 3 #Questa è una variabile GLOBALE quindi visibile dappertutto

def somma(x,y):
    #la variabile risultato è una variabile LOCALE, è visibile solo all'interno della funzione. Globalmente io non posso leggere questa variabile
    risultato = x + y
    print(f"Il risultato della somma è {risultato}")
    print(f"Il mio num fortunato è il {numeroFortunato} ")

somma(8,9)


def prodotto(x,y):
    risultato = x*y
    print(f"Il risultato del prodotto è {risultato}")

prodotto(8,2)

# Funzioni con return (non è obbligatorio avere dei parametri)
def dividi(x,y):
    risultato = x/y
    return risultato

#Vado a raccogliere il return della funzione
risultato_divisione = dividi(10,5)
print(f"Il risultato della divisione vale {risultato_divisione}")

def esegui_calcolo():
    valoreFinale = 120 #immagina che questo valore debba essere sempre diviso per un numero
    moltiplicatore = 6

    totale = dividi(valoreFinale, moltiplicatore) #dentro totale si registra, grazie al return, il valore della divisione tra questi due numeri 
    # print(f"Il calcolo produce il seguente numero: {totale}")
    return totale

print(f"Il totale vale {esegui_calcolo()}")
# posso anche registrare il valore in uscita all'interno di una variabile
totale = esegui_calcolo()
print(f"Il risultato del calcolo vale: {totale}")


def operazioni_mat(num1, num2):
    somma = num1 + num2
    prodotto = num1 * num2
    differenza = num1 - num2
    quoziente = num1 / num2

    return somma, prodotto, differenza, quoziente

# Adesso nel recuperare i valori delle 4 operazioni devo istanziare 4 variabili

s, p, d, q = operazioni_mat(9,4)
print(f"Il valore delle 4 operazioni è:\nSomma:{s}\nProdotto:{p}\nDifferenza:{d}\nQuoz:{q}")

# ATT: l'ordine di uscita(return) e l'ordine di ingresso(parametri della funzione) sono importanti, poiché sono posizionali

def descrivi_persona(nome, eta, citta):
    return f"{nome} ha {eta} anni e vive a {citta}"

# Devo obbligatoriamente passargli nome, età e città non li posso invertire
#                               nome    eta   citta
descrizione = descrivi_persona( "Dario", 36, "Torino")

print(descrizione)

# Posso passare i parametri senza occuparmi della posizione però devo ridefiniri ogni singolo parametro
descrizione2 = descrivi_persona(eta=30, citta="Napoli", nome="Anna")
print(descrizione2)

#funzioni con parametri di default. Posso anche rivalorizzare il parametro di default
def saluta_persona(nome, saluto="Ciao"):
    print(f"{saluto} {nome}")

saluta_persona("Luca")
saluta_persona("Marco", "Buongiorno")

# FUNZIONI con parametri variabili (accettano un numero variabile di parametri)
# Tutto il gioco lo fa *
def somma_tutti(*numeri):
    totale = 0
    for n in numeri:
        totale += n
    return totale

print(f"La somma vale {somma_tutti(1,2,3)}")
print(f"La somma vale {somma_tutti(10,5,33,8,9,10)}")


#Funzioni Ricorsive: funzioni che chiamano se stesse
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

totale = 0
def ricorsiva(n):
    totale = n+1
    print(totale)
    if(totale <= 100):
        ricorsiva(n+1)
    

ricorsiva(1)

    