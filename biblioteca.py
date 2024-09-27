#definizione delle classi

class Libro:
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

class Romanzo(Libro):
    def __init__(self, titolo, autore, anno, genere):
        super().__init__(titolo, autore, anno)
        self.genere = genere
    def __str__(self):
        return f"{self.titolo}, {self.autore}, {self.anno}, {self.genere}"
    def toString(self):
        return f"{self.titolo}-{self.autore}-{self.anno}-{self.genere}"


class Saggio(Libro):
    def __init__(self, titolo, autore, anno, tema):
        super().__init__(titolo, autore, anno)
        self.tema = tema
    def __str__(self):
        return f"{self.titolo}, {self.autore}, {self.anno}, {self.tema}"
    def toString(self):
        return f"{self.titolo}-{self.autore}-{self.anno}-{self.genere}"

#definizione classe biblioteca
class Biblioteca:
    def __init__(self):
        self.libri = []
    def aggiungi_libro(self, libro):
        self.libri.append(libro)
    def visualizza_libri(self):
        for libro in self.libri:
            print(libro)



l1 = Romanzo("Il signore degli anelli", "Tolkien", 1980, "Fantasy")
l2 = Romanzo("Harry Potter 1", "Rowling", 2001, "Fantasy")

b = Biblioteca()
b.aggiungi_libro(l1)
b.aggiungi_libro(l2)
b.visualizza_libri()