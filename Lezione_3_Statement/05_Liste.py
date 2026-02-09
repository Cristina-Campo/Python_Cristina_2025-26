#Le liste (anche chiamate array) sono dei contenitori di elementi simili tra loro, cioè elementi dello stesso tipo. Queste liste sono 0-based, cioè la conta parte da 0. Sono indicizzati e l'indice iniziale è 0

mia_lista = []

numeri = [4,2,8,3,6,1]

parole = ["Ciao", "Dario", "Arrivederci", "Oggi"]

#               0          1        2       3         4 
studenti = ["Cristina", "Marco", "Ioas", "Franco", "Andrei"]

#lista mista: non ha molto senso logico pur essendo fattibile
mista = [2, "Parola", True, "Ciao", 23, "23"]
studente = ["Paolo", "Rossi", 25, True, "TSS"]


#L'indice mi serve per poter richiamare il valore dell'array (lista) in quell'esatta posizione
print(studenti[0])

# Propr len : mi dice quanti sono gli elementi in una lista
numStud = len(studenti)
print(f"In classe ci sono {numStud} studenti")


primoStud = studenti[0]
ultimoStud = studenti[len(studenti) - 1]

print(f"ultimo studente dell'elenco è {ultimoStud} ma non per importanza")
# print("l'ultimo nella lista è", ultimoStud , "ma non per importanza")

#Per poter stampare tutti gli elementi uno alla volta uso il FORIN
# stud è una var locale che crei al volo nel costrutto 
for studente in studenti:
    print(studente)


# Scorrere con un indice
#           0          1       2       3        4  
colori = ["rosso", "giallo", "blu", "nero", "bianco"]

# Modificare un elemento della lista oppure modificare la lista
# trasformo in viola il colore blu
colori[2] = "viola"

# aggiungo un colore alla lista (al fondo)
colori.append("arancione")

# aggiungo un elemento in una posizione
colori.insert(2, "blu")
colori.insert(0, "azzurro")

# rimuovo un colore
colori.pop() # senza numeri rimuove sempre l'ultimo elemento
colori.pop(1) #rimuove il colore nella posizione che li stiamo passando
colori.remove("giallo")

# metodi vari
colori.reverse() #inverte la lista
colori.sort() #mette in ordine alfabetico crescente


for i in range(len(colori)):
    print(f"posizione {i} - colore {colori[i]}")


# altri metodi con liste di numeri
numeri = [4,8,100,9,3,21,1]

print(max(numeri))
print(min(numeri))
print(len(numeri))
print(sum(numeri))

totale = 0
i = 0

for num in numeri:
    i += 1
    totale += num
    print("parziale:", i, " = ", totale)

print(totale)


#WHILE - BREAK - CONTINUE
