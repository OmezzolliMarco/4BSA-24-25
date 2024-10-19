import tkinter as tk

root = tk.Tk()
root.title("Esempio place")
root.geometry("400x300")

button = tk.Button(root, text="Cliccami")
button.place(x=50, y=20, width=150, height=50)

root.mainloop()
