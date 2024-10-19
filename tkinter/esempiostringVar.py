import tkinter as tk

root = tk.Tk()
root.title("Esempio")
root.geometry("400x300")

testo = tk.StringVar() #variabile che contiene del testo
label = tk.Label(root, textvariable=testo)
label.pack(pady=20)

#creo un campo di input
testo_input = tk.Entry(root, width=10, textvariable=testo)
testo_input.pack(pady=10)

#button

root.mainloop()