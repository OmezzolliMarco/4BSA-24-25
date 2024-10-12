import tkinter as tk
#funzioni
contatore=0
def cambia_testo():
    label.config(text="hai cliccato!")

#main
root = tk.Tk() #istanza dell'oggeto Tk
root.title("La mia prima finestra")
root.geometry("400x300")

#contenitore
frm = tk.Frame(root, bg="blue")
frm.grid(padx=10, pady=10, sticky='nswe')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)



#avvio del mainloop
root.mainloop()