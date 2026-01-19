#Abbiamo un noleggio auto, per poter noleggiare il nostro cliente deve avere una patente acquisita da almeno 3 anni, l'età maggiore di 25 una carta di credito oppure una carta di debito

anni_patente = 1
eta = 40
carta_credito = False
carta_debito = False

if anni_patente >= 3 and eta >= 25 and (carta_credito or carta_debito):
    print("Caro utente, sei abilitato al noleggio dell'auto")
elif anni_patente < 3 and eta >= 25 and (carta_debito or carta_credito):
    print("Non puoi noleggiare, la tua patente è valida da pochi anni")
elif anni_patente >= 3 and eta < 25 and (carta_credito or carta_debito):
    print("Non puoi noleggiare, non hai l'età per farlo")
elif anni_patente >= 3 and eta >= 25 and not (carta_credito or carta_debito):
    print("Non puoi noleggiare, ti serve avere una carta di credito o di debito")
else:
    print("Non noleggiare: non hai una patente valida da almeno 3 anni o non hai l'età giusta o non hai un metodo di pagamento accettato")
    

# Esempio Qualità dell'aria a torino
# 3 Livelli : 1. Aria Pessima (pm10 sono oltre la soglia di 50 OR pm2.5 sono oltre i 25 AND l'ozono è oltre il 100 o la temp è oltre i 30)
# 2 aria mediocre (pm10 > 40 oppure pm25 > 20)
# 3 aria buona

pm10 = 30
pm2_5 = 14
ozono = 80
temp = 6

if (pm10 >= 50 or pm2_5 >= 25) and (ozono >= 100 or temp >= 30):
    print("Aria PESSIMA. Att: evitare di stare all'aperto")
elif pm10 >= 40 or pm2_5 >= 20:
    print("Aria Mediocre")
else:
    print("Aria Buona")