import random
print("BENVENUTO NEL GIORCO DI CARTA, SASSO FORBICE!")

#Chiede il nome all'utente
nomeUtente = input("Prima di tutto, inserisci il tuo nome = ")

#Chiede di inserire una mossa
sceltaUtente = input("Ora scgli la tua mossa. Scrivi 'carta', 'sasso' o 'forbice = ")
print(sceltaUtente)

#Determinazione della mossa del PC
sceltaPc = random.randint(0,2)
mossaPc = ["carta" , "sasso" "forbici"]
mossaPc = ""
if sceltaPc == 1:
    mossaPc = 
    print(f"La mossa del pc è {mossaPc}")
elif sceltaPc == 2:
    mossaPc == "forbici"
    print(f"La mossa del pc è {mossaPc}")
elif sceltaPc == 3:
    mossaPc == "sasso"
    print(f"La mossa del pc è {mossaPc}")
else:
    print("Mossa non valida. ERRORE SUL RANDOM")     


#Determinazione del risultato

if mossaPc == "carta" and sceltaUtente == "forbici" or mossaPc == "forbici" and sceltaUtente == "sasso" or mossaPc == "sasso" and sceltaUtente == "carta":
    print("Congratulazioni" , nomeUtente , "hai vinto!")
elif mossaPc == "carta" and sceltaUtente == "sasso" or mossaPc == "forbici" and sceltaUtente == "carta" or mossaPc == "sasso" and sceltaUtente == "forbici":
    print("Caspita" , nomeUtente , "! Andrà meglio la prossima volta!")
elif mossaPc == "carta" and sceltaUtente == "carta" or mossaPc == "forbici" and sceltaUtente == "forbici" or mossaPc == "sasso" and sceltaUtente == "sasso":
    print("Wow un pareggio!")        
else:
    print("Non è così che si gioca!")    
