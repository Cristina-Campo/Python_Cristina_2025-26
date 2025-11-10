# Le variabili sono dei "contenitori" di un'informazione singola
#Regole per le variabili
# 1. Le var devono avere un nome parlante, cioè deve essere descrittivo
# 2. NON posso utilizzare parole chiave: for, if, assert, True, False, ecc
# 3. Posso utlizzare i seguenti Case per poterle denominare
# camelCase (saldoConto)
# PascalCase (SaldoConto)
# snake_case (saldo_conto)
# kebab-case (saldo-conto) SCONSIGLIATO
# UPPER_CASE (SALDO_CONTO) solitamente utilizzato per le costanti

# ISTANZIO UNA VARIABILE (dichiaro e assegno)
# nomeVariabile = valore
mioNome = "Dario"
eta = 36
corsi = 4
studentiTotale = 90
corsoAttuale = "Tecnico Sistemista Reti"

# Vado a richiamare una o più variabili
print(mioNome)

# Metto insieme più variabili (sto facendo una concatenazione tra stringhe)
print("Ciao, sono", mioNome, ", ho", eta, "anni e insegno sul corso di", corsoAttuale)

print("Ciao, sono " + mioNome )

# Calcolo matematico semplice
primoNumero = 3
secondoNumero = 6

# RI-ASSEGNO una variabile, cioè gli cambio il valore. Qui capisco cosa vuol dire usare una variabile, cioè qualcosa che cambia
primoNumero = 7

somma = primoNumero + secondoNumero
print("La somma vale",somma)

prodotto = primoNumero * secondoNumero
print("Il prodotto vale", prodotto)

differenza = primoNumero - secondoNumero
print("La differenza vale", differenza)

quoziente = primoNumero / secondoNumero
print("La divisione vale", quoziente)