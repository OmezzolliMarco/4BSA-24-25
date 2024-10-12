class MetodoPagamento:
    def __init__(self, #...):
        #...
    def paga(self, importo):
        print("Questo metodo deve essere implementato nelle classi derivate")

class CartaDiCredito(MetodoPagamento):
    #aggiungere il costruttore

    def paga(self, importo):
        print(f"Pagato {importo} con carta di credito.")

class PayPal(MetodoPagamento):
    def paga(self, importo):
        print(f"Pagato {importo} tramite PayPal.")

#aggiungi un altro metodo di pagamento a tua scelta, esegui l'overrife della funzione paga

def effettua_pagamento(metodo: MetodoPagamento, importo):
    #utilizzando il polimorfismo di tipo completa questa funzione
    metodo.paga(importo)
#crea un ciclo infinito che continua a chiedere all'utente che pagamento vuole 
#effetturare, 1 - carta di credito, 2 - PayPal, 3 - Metodo aggiunto e 0 per uscire.
#Chiedi quindi un importo e richiama il pagamento sull'istanza creata.
#ATTENZIONE, SI POTREBBE OTTIMIZZARE IL CODICE PER CREARE SOLO 3 ISTANZE DEGLI OGGETTI PAGAMENTO E
#RICHIAMARE DI VOLTA IN VOLTA QUELLA CHE SCEGLIE L'UTENTE

paypal = Paypal()
cc = CartaDiCredito()
tipo = 1
while tipo != 0:
    tipo = int(input("Inserisci 1 per la carta di credito, 2 per Paypal e 0 per uscire"))
    if tipo == 1:
        qta = float(input("Inserisci la quantità da pagare: "))
        paypal.paga(qta)
    elif tipo == 2:
        qta = float(input("Inserisci la quantità da pagare: "))
        effettua_pagamento(cc, qta)
    elif tipo == 0:
        print("Hai deciso di chiudere il programma, arrivederci!")
    else:
        print("hai sbagliato")