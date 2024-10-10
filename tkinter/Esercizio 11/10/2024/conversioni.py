import tkinter as tk

#funzioni
def conversione():
    try:
        value = float(piedi.get()) #leggo il contenuto della variabile piedi di tipo StringVar
        metri.set(float(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except:
        pass

#main
root = tk.Tk()
root.title("Piedi a metri")

frm = tk.Frame(root, bg="lightblue")
frm.grid(column=0, row=0, sticky='nsew', padx=20, pady=20)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

piedi = tk.StringVar()
piedi_inserimento = tk.Entry(frm, width=7, textvariable=piedi)
piedi_inserimento.grid(column=2, row=1, sticky='we')

metri = tk.StringVar()

etichetta_metri = tk.Label(frm, textvariable=metri)
etichetta_metri.grid(column=2, row=2, sticky="w")

converti = tk.Button(frm, text='Calcola', command=conversione)
converti.grid(column=3, row=3, sticky="w")

tk.Label(frm, text="piedi").grid(column=3, row=1, sticky='w')
tk.Label(frm, text="sono equivalenti a").grid(column=1, row=2, sticky='e')
tk.Label(frm, text="meters").grid(column=3, row=2, sticky='e')

#recupero tutti i figli presenti nel frame e applico uno spostamento
for child in frm.winfo_children():
    child.grid_configure(padx=10, pady=10)

#all'apertura del programma il campo per l'inserimento è già selezionato
piedi_inserimento.focus()

root.mainloop()


