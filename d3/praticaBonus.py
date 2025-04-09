import re

def analizza_testo(testo):
    testo = testo.lower()

    testo = re.sub(r'[^\w\s]', '', testo)
    
    parole = testo.split()
    
    occorrenze = {}
    for parola in parole:
        if parola in occorrenze:
            occorrenze[parola] += 1
        else:
            occorrenze[parola] = 1
    
    return occorrenze


testo = input("Inserisci una stringa di parole: ")
risultato = analizza_testo(testo)
print(risultato)
