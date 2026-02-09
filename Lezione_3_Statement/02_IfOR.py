# con l'utilizzo dell'or logico valuto più condizioni contemporaneamente e mi basta che una delle varie condizioni sia true affinché quella globale risulti essere true

# Voglio capire se la temp ambiente è ottimale per le mie piante. Quest piante crescono bene tra 18 e 24 gradi
tempCasa = 30


#   False              True
if (tempCasa < 18 or tempCasa > 24):
    print("Siamo fuori dal range ottimale di temperatura")
else:
    print("Tutto ok, temp perfetta")


#Esempio login: posso loggarmi sia con la mia email sia con lo username admin

username = "dario.mennillo@email.com"
password = "1235"

if( username == "admin" or username == "dario.mennillo@email.com") and password == "12345":
    print("Benvenuto nella piattaforma")
else:
    print("Mi spiace, c'è qualcosa che non va")
    print("Mi spiace, c'è qualcosa che non va")
