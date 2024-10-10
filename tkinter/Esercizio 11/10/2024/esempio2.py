import tkinter as tk

root = tk.Tk()
root.title("Esempio posizionamento")
root.geometry("300x200")

frm = tk.Frame(root, bg="lightblue")
frm.grid(row=0, column=0, sticky='nsew')

#espansione del frame per occupare tutto lo spazio disponibile
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0, weight=1)

label1 = tk.Label(frm, text="Label 1")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(frm, text="Label 2")
label2.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(frm, text="Chiudi", command=root.quit)
button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()