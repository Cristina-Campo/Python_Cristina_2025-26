import Operaziony #Importa tutto i lmodulo attraverso il nome del file

risultato = Operaziony.moltiplicazione(9,5)
print(f"Il risultato della moltiplicazione è {risultato}")

#OPZIONE 2: importo solo quello che mi serve
from Operaziony import somma, divisione

risultato2 = somma(10,4)
risultato3 = divisione(40,3)
print(f"Il risultato della somma è {risultato2}")
print(f"Il risultato della divisione è {risultato3}")
