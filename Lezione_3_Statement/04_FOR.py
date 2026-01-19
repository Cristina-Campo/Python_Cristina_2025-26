#Il ciclo for serve a ripetere un'istruzione o un blocco di istruzioni un numero definito di volte

# i sta per indice
for i in range(5):
    print("Ciao",i)

for i in range(0,46, 4):
    print(i)

#Stampa tutti i numeri da 1 a 100. Quando stampi un multiplo di 3 stampa Zoom, quando stampa un multipli di 5 stampa Boom, quando stampi un multiplo di 3 e di 5 stampa Bangherang
print("========  Giochino ZOOM BOOM Bangherang =========")
for i in range(1,101):
    if i % 3 == 0: 
        print(i, "ZOOM")
    else:
        print(i)


# Fare le LISTE, cioè quello che noi chiamiamo Array
