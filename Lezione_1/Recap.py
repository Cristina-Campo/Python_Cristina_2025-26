# In Python esistono tipi di dato diversi: String, Number(Intger Float), Boolean

mioNome = "Dario" #Questa è una String
numero = "2" #Anche questa è una String
unioneString = mioNome + numero #Uso l'operatore + per concatenare due stringhe
print(unioneString)

#OPERATORI MATEMATICI

num2 = 56 #Questo è un Number di tippo Integer
num3 = 43 #Questo è un Number di tipo Float

somma = num2 + num3
print(somma)
diff = num2 - num3
print(diff)
molt = num2 * num3
print(molt)
quoz = num2 / num3
print("Il risultato della divisione è:" , quoz)

# NumEString = mioNome + num2
# print(NumEString)

#OPERATORE MODULO o RESTO DELLA DIVISIONE
mod1 = 4 % 2
print(mod1)

mod2 = 2 % 4
print(mod2)

mod3 = 4 % 3
print(mod3)

mod4 = 255 % 5
print(mod4)

#Altri operatori
# += Incremento
miaVar = 0
miaVar += 3 # miaVar = miaVar + 3

# ** elevamento a potenza
pow1 = 4 ** 6
print(pow1)

pow2 = 3 ** 2.8
print(pow2)

pow3 = pow(5, 2) #Att: pow() è una funzione matematica built-in
print(pow3)


# // arrotonda all'intero inferiore 
arr1 = 8.0 // 3
print(arr1)

# Radice
rad1 = 4 ** 0.5
print(rad1)

#posso fare la radice con sqrt ma stavolta devo importare la libreria math
#Di solito le librerie sono importate nelle prime righe dello script altrimenti non raggiungibili dal codice scritto prima dell'import

import math
rad2 = math.sqrt(80)
print(rad2)


#utilizzo della funzione type per capire di che tipo è una variabile
tuoNome = "Anna"
tuaEta = 30
presenza = True
numPreferito = 13.6
tuoNome = "Laura"

print(type(tuoNome))
print(type(tuaEta))
print(type(presenza))
print(type(numPreferito))

# COSTANTI, denominate tutte in maiusc
PI_GRECO = 3.14
print(PI_GRECO)

IVA = 0.22
C = 300000
E = 2.71
MINUTI_IN_ORA = 60

#INPUT. Questo metodo è in grado di ricevere un input dall'utente

nomeUser = input("Come ti chiami ?")
print("Ciao", nomeUser)

#Cast del dato. Visto che quelloo che recupero dagli input è sempre una string con int(...) forzo quella var ad essere di tipo int
anniUser = int( input("Quanti anni hai ?") )
tra10Anni = anniUser + 10

print("Hai", anniUser, "anni. Tra 10 anni ne avrai", tra10Anni)
