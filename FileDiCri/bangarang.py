#Stampa tutti i numeri da 1 a 100
#per i multipli di 3 stampa ZUM
#per i multipli di 5 stampa BUM
#per i multipli di 3 E 5 stampa BANGARANG

zum = 0
bum = 0
bang = 0

for i in range (1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("BANGARANG")
    bang += 1
  elif i % 3 == 0:
    print("ZUM")
    zum += 1
  elif i % 5 == 0:
    print("BUM")
    bum += 1
  else:
    print(i)

print("Zum totali: ", zum)
print("Bum totali: ", bum)
print("Bangarang totali: ", bang)

#E se volessi contarli?    

