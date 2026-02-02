# FUNZIONI : blocco di codice che può essere riutilizzato più volte  
# def nome_funzione(parametri):
#     blocco di codice
#     return valore_di_ritorno
# chiamata della funzione
# nome_funzione(argomenti)

def salutaQualcuno(nome):
    print(f"Ciao {nome}!")

#nome_persona = input("Chi vorresti salutare? ")
nome_persona = "Anna"
salutaQualcuno(nome_persona)    

#Passiamo più parametri nella funzione
#Funzione che calcola una somma
def somma(x,y):
    #questa variabile "risultato" è una variabile LOCALE ovvero visibile soltanto all'intero della funzione
    risultato = x+y
    print(f"La somma di {x} e {y} è {risultato} e mentre ci sei saluta pure {nome_persona}") #Qua nome_persona viene presa perchè è una variabile GLOBALE

somma(9,6.7)

#Funzione che calcola un prodotto
def prodotto(x,y):
    risultato = x * y
    print(f"Il prodotto di {x} e {y} è {risultato}")

prodotto(7,3)

#Funzioni con RETURN
def divisione(x,y):
    risultato = x / y
    return risultato #potrei scrievere anche solo "return x / y"

#Vado a racccogliere il return ella funzione
risultato_divisione = divisione(10,5)
print(f"Il risultato della divisione è {risultato_divisione}")

def esegui_calcolo():
    valoreFinale = 120 #immagina che questo valore debba essere sempre diviso per un numero
    moltiplicatore = 6

    totale = divisione(valoreFinale, moltiplicatore) #dentro totale si registra grazie al return il valore della divisione tra questi 2 numeri
    return totale
print(f"IL calcolo produce il seguente numero: {esegui_calcolo()}")


def operazioni_mate(num1, num2): #I valori posizionali sono molto importanti, sia in ingresso (parametri) che in uscita (return)
    somma = num1 + num2
    prodotto = num1 * num2
    differenza = num1 - num2
    quoziente = num1 / num2

    return somma, prodotto, differenza, quoziente

#Adesso nel recuperare i valori delle 4 operazioni devo istanziare 4 variabili
s, p, d, q = operazioni_mate(9,4)
print(f"Il valore delle 4 operazioni è \n SOMMA: {s} \n PRODOTTO: {p} \n DIFFERENZA: {d} \n QUOZIENTE: {q}")


def descriviPersona(nome, eta, citta):
    return f"{nome} ha {eta} anni e vive a {citta}"

#Devo OBBLIGATORIAMENTE passarli i parametri nell'ordine specificato nella definizione della funzione
#                              nome       eta    citta
descrizione = descriviPersona("Cristina", 31 , "Torino")
print(descrizione)

#Posso passare i parametri senza preoccuparmi dell'ordine dei parametri, però devo ridefinire ogni singolo parametro
descrizione2 = descriviPersona(citta="Berlino", nome="Tytto", eta=81)
print(descrizione2)

#funzioni con parametri di default
def salutaPersona(nome, saluto = "Buondì"):
    print(f"{saluto} {nome}")

salutaPersona("Hans") 
salutaPersona("Elsa", "Terve")

#Funzioni con parametri VARIABILI, ovvero accettano un numero variabile di parametri
def somma_tutti(*numeri): #il * indica che può ricevere un numero variabile di parametri
    totale = 0
    for n in numeri:
        totale += n
    return totale

print(f"La somma vale: {somma_tutti(1,2,3)}")
print(f"La somma vale: {somma_tutti(15,45,102,23,67,89)}")

#Funzione per calcolare l'età
def tua_eta(anno_nascita, anno_corrente=2026):
    eta = anno_corrente - anno_nascita
    return eta

print(f"Hai {tua_eta(1994)} anni")


#FUNZIONI RICORSIVE : una funzione che richiama se stessa
#sequenza di fibonacci: 0 1 1 2 3 5 8 13 21 34 55 89 ...
def fibonacci(n):
    if n<= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) #sto chiamando la funzione stessa

print(fibonacci(7))
