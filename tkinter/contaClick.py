import tkinter as tk

#funzione
def conta():
    global count
    count += 1
    label_conta.config(text=f"Numero click: {count}")

#main
root = tk.Tk()
root.title("Conta click")
root.geometry("400x300")

count = 0

frm = tk.Frame(root, bg="lightgreen")
frm.pack(padx=5, pady=5, fill="both", expand=True)

#creo la label contatore
label_conta = tk.Label(frm, text=f"Numero di click: {count}", font=("Monsterrat", 12), bg="lightgreen")
label_conta.pack(pady=10)

#pulsante da cliccare
button = tk.Button(frm, text="Cliccami!", command=conta, height=30)
button.pack(pady=20)

#mainloop
root.mainloop()