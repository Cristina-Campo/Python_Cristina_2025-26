
studenti = []

def aggiungi_studente(nome, cognome, voto):
    studenti.append(f"{nome} {cognome}, voto: {voto}")
    print(f"Studente {nome} aggiunto")


def stampa_studenti():
    for stud in studenti:
        print(stud)

aggiungi_studente("Mario", "Rossi", 20)
aggiungi_studente("Laura", "Verdi", 25)
aggiungi_studente("Luca", "Bianchi", 30)
aggiungi_studente("Marta", "Gialli", 30)

stampa_studenti()