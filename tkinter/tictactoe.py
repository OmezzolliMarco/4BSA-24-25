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
        global griglia

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
        if self.pulsanti[i].cget("text") == "":
            self.pulsanti[i].configure(text=self.player)
            griglia[i//3][i%3] = self.player
            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"

            winner = self.controllaVincitore()
            if winner != None: #controlla che non sia None
                #ho trovato vincitore o pareggio
                if winner == "X" or winner == "O":
                    messagebox.showinfo("Vincitore", "Ha vinto " + winner)
                if winner == "Pareggio":
                    messagebox.showinfo("Vincitore", "Pareggio")
                self.resetGame()

    def controllaVincitore(self):
        #controllo orizzontali e verticali
        for i in range(3):
            if griglia[i][0] == griglia[i][1] == griglia[i][2] != "":
                return griglia[i][0]
            if griglia[0][i] == griglia[1][i] == griglia[2][i] != "":
                return griglia[0][i]
        #controllo diagonali
        if griglia[0][0] == griglia[1][1] == griglia[2][2] != "":
            return griglia[0][0]
        if griglia[0][2] == griglia[1][1] == griglia[2][0] != "":
            return griglia[1][1]
        
        #controllo pareggio
        if all(all(cell != "" for cell in row)for row in griglia):
            return "Pareggio"
        else:
            return None
    def resetGame(self):
        for pulsante in self.pulsanti:
            pulsante.configure(text="")
        for i in range(3):
            for j in range(3):
                griglia[i][j]=""
#main

#creazione la griglia
griglia = []
for i in range(3):
    #definizione delle righe
    griglia.append([])
    for j in range(3):
        griglia[i].append("") #celle vuote che andranno riempite con X o O

root = tk.Tk()
ttt = TicTacToe(root)

root.mainloop()