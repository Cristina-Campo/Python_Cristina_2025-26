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
for stud in studenti:
    print(stud)


# Scorrere con un indice
#           0          1       2       3        4  
colori = ["rosso", "giallo", "blu", "nero", "bianco"]

for i in range(len(colori)):
    print(f"posizione {i+1} - colore {colori[i]}")
