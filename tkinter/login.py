import tkinter as tk
from tkinter import messagebox

class FinestraLogin:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")
        
        #costruzione della finestra
        self.label_nome = tk.Label(root, text="Nome utente: ")
        self.label_nome.pack(pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady = 5)

        self.password_label = tk.Label(root, text="Password")
        self.password_label.pack(pady=20)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.pulsanteLogin = tk.Button(root, text="LOGIN", command=self.verificaLogin)
        self.pulsanteLogin.pack(pady=20)

    def verificaLogin(self):
        username = self.username_entry.get() #recupero il valore nella entrye lo salvo nella variabile username
        password = self.password_entry.get()

        #utenti registrati (dizionario di utenti con password)
        utenti = {"giorgio": "cactus", "gabriele":"gianni", "aurora": "trulli"}

        #variabile di controllo per il login
        controllo_login = False

        #controllo a scorrimento su tutti gli utenti
        for u, p in utenti.items():
            if username==u and password==p:
                controllo_login = True
                messagebox.showinfo("Login", "Accesso riuscito")

        #controllo per evitare la messagebox se sono riuscito ad eseguire il login
        if controllo_login == False:
            messagebox.showerror("Login", "Accesso fallito")     


#main
root = tk.Tk()
finestra = FinestraLogin(root)

#mainloop
root.mainloop()