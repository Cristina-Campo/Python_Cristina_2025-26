import random
print("BENVENUTO NEL GIORCO DI CARTA, SASSO FORBICE!")

#Chiede il nome all'utente
nomeUtente = input("Prima di tutto, inserisci il tuo nome = ")
#Controlo che il nome abbia abbastanza caratteri e che sia valido
if len(nomeUtente) >= 3:
    print(f"{nomeUtente} preparati!")

print("###########################################################################")
#Chiede di inserire una mossa
sceltaUtente = input("Ora scgli la tua mossa. Scrivi 'carta', 'sasso' o 'forbici = ")
print(sceltaUtente)

#Determinazione della mossa del PC
numRandom = random.randint(0,2)
sceltaPc = ["carta" , "sasso", "forbici"]

if numRandom == 0:
    mossaPc = sceltaPc[0]
    print(mossaPc)
elif numRandom == 1:
    mossaPc = sceltaPc[1]
    print(mossaPc)
elif numRandom == 2:
    mossaPc = sceltaPc[2]
    print(mossaPc)  
else:
    print("IDK MAAN")    

#Determinazione del risultato

if mossaPc == "carta" and sceltaUtente == "forbici" or mossaPc == "forbici" and sceltaUtente == "sasso" or mossaPc == "sasso" and sceltaUtente == "carta":
    print("Congratulazioni" , nomeUtente , "hai vinto!")
elif mossaPc == "carta" and sceltaUtente == "sasso" or mossaPc == "forbici" and sceltaUtente == "carta" or mossaPc == "sasso" and sceltaUtente == "forbici":
    print("Mannaggia" , nomeUtente , "! Andrà meglio la prossima volta!")
elif mossaPc == "carta" and sceltaUtente == "carta" or mossaPc == "forbici" and sceltaUtente == "forbici" or mossaPc == "sasso" and sceltaUtente == "sasso":
    print("Wow un pareggio!")        
else:
    print("Non è così che si gioca!")    
