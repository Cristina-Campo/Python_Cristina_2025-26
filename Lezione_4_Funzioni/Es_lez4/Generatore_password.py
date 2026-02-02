#Utilizzando un menu di scelta crea il seguente generatore di password
#1 - genera psw semplice -> lettere e numeri
#2 - genera psw forte -> lettere, numeri e caratteri speciali (. ; : - _ ! ? )
#3 - genera psw numerica -> numeri solamente
#4 - testa forza della psw -> verifica se 1) la psw ha almeno 8 caratteri (+1) 2) se ha caratteri in uppercase(+1) 3) contiene numeri(+1) 4) contiene caratteri speciali(+1)

#Imposta un punteggio della forza
#se è <= 2 = debole
#se è 3 <= media
#se è > 3 = forte


import random

password = ""
caratteri_speciali = [".", ";", ":", "-", "_", "!", "?"]
lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lettere_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeri = ["0","1","2","3","4","5","6","7","8","9"]

print("<<<<<< GENERATORE DI PASSWORD >>>>>>")
print("MENU - Scegli il tipo di password da generare")
scelta = ""

# FUNZIONE PER GENERARE PASSWORD SEMPLICE
def psw_semplice(numMaiuscole, numMinuscole, numNumeri):
    password = []

    for i in range(numMaiuscole):
        if numMaiuscole == 0 or numMaiuscole > 2:
            print("Errore: Ricorda che questa è una password semplice. Il numero di maiuscole non può essere 0 o maggiore di 2.")
        else:
            password.append(random.choice(lettere_upper))

    for i in range(numMinuscole):
        if numMinuscole == 0 or numMinuscole > 2:
            print("Errore: Ricorda che questa è una password semplice. Il numero di minuscole non può essere 0 o maggiore di 2.")
        else:
            password.append(random.choice(lettere))

    for i in range(numNumeri):
        if numNumeri == 0 or numNumeri > 2:
            print("Errore: Ricorda che questa è una password semplice. Il numero di numeri non può essere 0 o maggiore di 2.")
        else:
            password.append(random.choice(numeri))

    random.shuffle(password)
    return "".join(password)    


# FUNZIONE PER GENERARE PASSOWORD FORTE
def password_forte(numMaiuscole, NumMinuscole, numNumeri, numSpeciali):
    password = []

    for i in range(numMaiuscole):
        if numMaiuscole == 0 or numMaiuscole > 5:
            print("Errore: Il numero di maiuscole deve essere compreso tra 1 e 5.")
        else:
            password.append(random.choice(lettere_upper))

    for i in range(NumMinuscole):
        if NumMinuscole == 0 or NumMinuscole > 5:
            print("Errore: Il numero di minuscole deve essere compreso tra 1 e 5.")
        else:
            password.append(random.choice(lettere))

    for i in range(numNumeri):
        if numNumeri == 0 or numNumeri > 5:
            print("Errore: Il numero di numeri deve essere compreso tra 1 e 5.")
        else:
            password.append(random.choice(numeri))

    for i in range(numSpeciali):
        if numSpeciali == 0 or numSpeciali > 5:
            print("Errore: Il numero di caratteri speciali deve essere compreso tra 1 e 5.")
        else:
            password.append(random.choice(caratteri_speciali))            

    random.shuffle(password)
    return "".join(password)

# FUNZIONE PER GENERARE PINCODE
def genera_pincode(lunghezza):
    password = []

    for i in range(lunghezza):
        if lunghezza < 4 or lunghezza > 10:
            print("Errore: La lunghezza del PINCODE deve essere compresa tra 4 e 10.")
        else:
            password.append(random.choice(numeri))

    random.shuffle(password)
    return "".join(password)

#FUNZIONE PER TESTARE LA FORZA DELLA PASSWORD
def stress_test(password):
    punteggio = 0

    if len(password) >= 8:
        punteggio += 1

    if any(char.isupper() for char in password):
        punteggio += 1

    if any(char.isdigit() for char in password):
        punteggio += 1

    if any(char in caratteri_speciali for char in password):
        punteggio += 1

    if punteggio <= 2:
        forza = "Debole **/5"
    elif punteggio == 3:
        forza = "Media ***/5"
    else:
        forza = "Forte *****/5"

    return forza        

while scelta != 5:
    print("\n - Menu -")
    print("1. Genera password semplice")
    print("2. Genera passowrd forte")
    print("3. Genera PINCODE")
    print("4. Testa forza della password")
    print("5. ESCI")

    scelta = int( input("Scegli: \n"))

    if scelta == 1:
        a = int(input("Quante lettere MAIUSCOLE vuoi nella password? (max 2): "))
        b = int(input("Quante lettere minuscole vuoi nella password? (max 2): "))
        c = int(input("Quanti numeri vuoi nella password? (max 2): "))
        password = psw_semplice(a,b,c)
        print(f"La tua password semplice è: {password}")
    elif scelta == 2:
        a = int(input("Quante lettere MAIUSCOLE vuoi nella password? (max 5): "))
        b = int(input("Quante lettere minuscole vuoi nella password? (max 5): "))
        c = int(input("Quanti numeri vuoi nella password? (max 5): "))
        d = int(input("Quanti caratteri speciali vuoi nella password? (max 5): "))
        password = password_forte(a,b,c,d)
        print(f"La tua password forte è: {password}")
    elif scelta == 3:
        lunghezza = int(input("Di che lunghezza vuoi il PINCODE? (4-10): "))
        password = genera_pincode(lunghezza)
        print(f"La tua PINCODE è: {password}")
    elif scelta == 4:
        password = input("Inserisci la password da testare: ")
        forza = stress_test(password)
        print(f"La forza della password è: {forza}")
    elif scelta == 5:
        print("Ciao, alla prossima")    
    else:
        print("Non ho capito la scelta")

print("Programma terminato")
