#Utilizzando un menu crea il seguente gioco
#Indovina un numero tra 1 e 50 (easy mode) - TENTATIVI ILLIMITATI
#Indovina un numero tra 1 e 100 (hard mode) - TENTATIVI MASSIMI 10
#ogi volta che l'untente inserisce un numero suggerisci se questo è troppo alto o troppo basso rispetto a quello da indovinare
#attenzione IL NUMERO DA INDOVINARE DEVE ESSERE SCELTO IN MODO RANDOM!



import random
print("<<<<<< INDOVINA IL NUMERO >>>>>>")
print("Scegli la modalità di gioco:")

scelta = ""

#FUNZIONE EASY MODE
def easy_mode():
    numero_da_indovinare = random.randint(1,50)
    tentativi = 0
    indovinato = False
    print("Modalità Easy: Indovina un numero tra 1 e 50. Tentativi illimitati!")

    while not indovinato:
        tentativi += 1
        tentativo_utente = int(input("Inserisci il tuo tentativo: "))
        if tentativo_utente == numero_da_indovinare:
            print(f"Congratulazioni! Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi.")
            indovinato = True
        elif (tentativo_utente - numero_da_indovinare == 2) or (numero_da_indovinare - tentativo_utente == 2):
            print("UUUUUUH FUOCHINO! Ci sei quasi!")                
        elif tentativo_utente > numero_da_indovinare:
            print("Il numero è troppo alto.")
        else:
            print("Il numero è troppo basso.")

#FUNZIONE HARD MODE
def hard_mode():
    numero_da_indovinare = random.randint(1,100)
    tentativi = 0
    max_tentativi = 10
    indovinato = False
    print("Modalità Hard: Indovina un numero tra 1 e 100. Hai un massimo di 10 tentativi!")

    while not indovinato and tentativi < max_tentativi:
        tentativi += 1
        tentativo_utente = int(input(f"Tentativo {tentativi}/{max_tentativi}. Inserisci il tuo tentativo: "))
        if tentativo_utente == numero_da_indovinare:
            print(f"Congratulazioni! Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi.")
            indovinato = True
        elif (tentativo_utente - numero_da_indovinare == 2) or (numero_da_indovinare - tentativo_utente == 2):
            print("UUUUUUH FUOCHINO! Ci sei quasi!")
        elif tentativo_utente > numero_da_indovinare:
            print("Il numero è troppo alto.")
        else:
            print("Il numero è troppo basso.")

    if not indovinato:
        print(f"Mi dispiace, hai esaurito i tuoi tentativi. Il numero era {numero_da_indovinare}.")

while scelta != 3:
    print("\n - Menu -")
    print("1. Easy mode")
    print("2. Hard mode")
    print("3. Esci")

    scelta = int( input("Scegli: \n"))

    if scelta == 1:
        easy_mode()
    elif scelta == 2:
        hard_mode()
    elif scelta == 3:
        print("Ciao alla prossima!")
    else:
        print("Non ho capito la scelta")

print("Programma terminato")