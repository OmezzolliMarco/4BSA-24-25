class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    def descrizione(self):
        pass

class Auto(Veicolo):
    def __init__(self, marca:str, modello:str, porte:int):
        super().__init__(marca, modello)
        self.porte = porte
    def descrizione(self): #override
        print(f"Auto {self.marca}, {self.modello}, {self.porte}")    

class Moto(Veicolo):
    def __init__(self, marca, modello, tipo):
        super().__init__(marca, modello)
        self.tipo = tipo
    def descrizione(self): #override
        print(f"Moto {self.marca}, {self.modello}, {self.tipo}")    

#main
a1 = Auto("Audi", "RS4", 5)
a1.descrizione() #uso della funzione sovrascritta nella classe figlia

m1 = Moto("Ducati", "Panigale", 1000)
m1.descrizione() #uso della funzione sovrascritta nella classe figlia