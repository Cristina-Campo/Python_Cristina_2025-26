#Le liste anche chiamatae array sono dei contenitori di elementi simili tra di loro
#elementi dello stesso tipo. Stringhe, numeri, ecc
#Tutt e queste liste sono "zero based". gli elementi sono indicizzati e l'indice parte da 0

mia_lista = []

numeri = [4,2,8,3,6,1]
parole = ["Ciao" , "Cristina" , "Arrivederci" , "Oggi"]
#                0          1         2         3          4
studenti = ["Cristina" , "Marco" , "Ioas" , "Andrei" , "Franco"]

#L'indice serve per poter richiamare un elemento di un array
print(studenti[2])

#lista mista: non ha molto senso logico, ma è lo stesso fattibile
mista = [2, "Paola" , True , "Ciao" , 4986 , "23"]


#proprietà length
#mi dice quanti sono gli elementi in un array

numeroStudenti = len(studenti)
print("In classe ci sono ", numeroStudenti)
#Stampa 5 perchè l'indice è solo il nome della posizione 


primoStud = studenti[0]
ultimoStud = studenti[len(studenti) - 1]
print(f"L'ultimo studnete dell'elenco è {ultimoStud}")


#Per poter stampare tutti gli elementi di un array uno alla volta
#uso il FORIN

for stud in studenti:
    print(stud)

#Scorrere con un indice
colori = ["rosso", "giallo" , "blu" , "nero" , "bianco"]    

for i in range(len(colori)):
    print(f"posizione {i} : {colori[i]}")