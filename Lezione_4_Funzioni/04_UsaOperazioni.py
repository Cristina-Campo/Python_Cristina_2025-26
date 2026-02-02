#OPZIONE 1: importo tutto il modulo con il nome del file
import operazioni 

risultato = operazioni.moltiplicazione(9,5)
print(risultato)

#OPZIONE 2: importo solo quello che mi serve
from operazioni import somma, divisione

risultato2 = somma(10,4)
risultato3 = divisione(40,3)

print(risultato2)
print(risultato3)
