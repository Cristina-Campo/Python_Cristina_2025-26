
studenti = []

def aggiungi_studente(nome, cognome, voto):
    studenti.append(f"{nome} {cognome}, voto :{voto}")
    print(f"Studente {nome} aggiunto con successo.")


def stampa_studenti():
    for stud in studenti:
        print(f"\n",stud)    

aggiungi_studente("Mario", "Rossi", 20)
aggiungi_studente("Luigi", "Verdi", 18)
aggiungi_studente("Anna", "Bianchi", 30)     
aggiungi_studente("Carla", "Neri", 25)   

stampa_studenti()
