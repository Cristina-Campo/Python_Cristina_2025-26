# Il while rientra nei cicli indefiniti
#SINTASSI:
# while condizione:

counter = 0

while counter < 10:
    print(f"Il contatore vale: {counter}")
    counter += 2


###ESEMPIO

password = ""
tentativi = 0

while password != "abcdef":
    password = input("Inserisci la password")
    tentativi += 1

print(f"Bravo, hai trovato la password in {tentativi} tentativi")
#A priori non so quanti tentativi impiegherà l'utente per poter entrare

###Esempio con break, interrompe il ciclo while ed esce

contatore = 1

while True: #Ciclo infinito
    print(contatore)
    contatore += 1

    if contatore > 10:
        break #con questo, al verificarsi della condizione dell'if esco dal ciclo


###Esempio con continue, salta un'iterazione

numero = 0

while numero < 10:
    numero += 1

    if numero % 2 == 0: #se il numero è pari allora salta un'iterazione, quando incontra il continue non arriva al print sotto poiché sale subito in alto
        continue
    
    print(numero)


### Data una lista di numeri, se appare il 42 lancia un messaggio, per tutti gli altri stampa solo il numero
print("=== LISTA NUMERI ===")
listaNum = [2,5,6,32,1,6,42,2,1,57,42,53]

for num in listaNum:
    if num == 42:
        print(f"DON'T PANIC !!")
        #break
        continue #il continue se ne fotte di tutto ciò che si trova sotto
       
    print(num)


### Validazione con input

print("=== Validazione input ===")

while True:
    try:
        eta = int( input("Inserisci la tua età: \n") )

        if eta < 0 or eta > 120 :
            print("Età inserita non valida, riprova")
            continue
        
        break
    
    except ValueError:
        print("Non hai inserito un numero")

print(f"La tua età è {eta}")