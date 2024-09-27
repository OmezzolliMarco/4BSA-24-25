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

r1 = Romanzo("Il signore degli anelli", "Tolkien", 1980, "Fantasy")
print(r1)

