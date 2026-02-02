parola = "appartamento"

parolaARR = [] #Questo mi serve per trasformare la parola in un array
arrayVuoto = [] #Questo mi serve per nascondere la parola

#Questo for trasforma la parola in un array e riempi l'array vuoto di trattini quante sono le lettere di parola
for lett in parola:
    parolaARR.append(lett)
    arrayVuoto.append("_")


# print(parolaARR)
print("La parola da cercare è\n",arrayVuoto)

tentativi = 0


while(tentativi <= 6):
    letteraCercata = input("Inserisci una lettera")

    for i in range(len(parolaARR)):
        if(letteraCercata == parolaARR[i]):
            print(f"Trovata la lettera {letteraCercata} in posizione {i + 1}")
            arrayVuoto[i] = letteraCercata
            print(arrayVuoto)
            continue
            
    if not parolaARR.__contains__(letteraCercata):
        tentativi += 1
        print(f"Ti restano {6 - tentativi} tentativi")
