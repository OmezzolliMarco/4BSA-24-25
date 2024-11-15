import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Il gioco del Tris")
        self.root.geometry("400x400")

        #giocatori
        self.player = "O" #il giocatore che inizia parte con la x

        #piano di gioco
        self.board = [] #risultati

        #struttura del piano da gioco
        self.pulsanti = []

        self.creaTavoloGioco()
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
    
    def creaTavoloGioco(self):
        for i in range(9):
            button = tk.Button(self.root, text="", width=10, height=10, command=lambda i=i: self.clickPulsante(i))
            button.grid(row=i//3, column=i%3, sticky="NSEW")
            self.pulsanti.append(button)

    def clickPulsante(self, i):
        self.pulsanti[i].configure(text=self.player)
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"
    def controllaVincitore(self):
        #da completare...
#main
root = tk.Tk()
ttt = TicTacToe(root)

root.mainloop()