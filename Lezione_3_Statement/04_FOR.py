#Il ciclo for serve a ripetere un'istruzione o un blocco di istruzioni un numero finito di volte

# i sta per indice
for i in range(5):
    print("Ciao",i)

for i in range(0,46, 4):
    print(i)

#Stampa tutti i numeri da 1 a 100. Quando stampi un multiplo di 3 stampa Zoom, quando stampa un multipli di 5 stampa Boom, quando stampi un multiplo di 3 e di 5 stampa Bangherang
print("========  Giochino ZOOM BOOM Bangherang =========")

quantZOOM = 0
quantBOOM = 0
quantBANG = 0

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "Bangarang")
        quantBANG += 1
    elif i % 3 == 0: 
        print(i, "ZOOM")
        quantZOOM += 1
    elif i % 5 == 0:
        print(i, "BOOM")
        quantBOOM += 1
    else:
        print(i)


print(f"Il totale di ZOOM è {quantZOOM}. Multipli di 3")
print(f"Il totale di BOOM è {quantBOOM}")
print(f"Il totale di BANG è {quantBANG}")