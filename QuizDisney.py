import tkinter as tk
from tkinter import messagebox
import json
import os

root = tk.Tk()
root.title("Mostra Foto")
canvas = tk.Canvas(root, width=1000, height=600)
canvas.pack()

imatge_1 = tk.PhotoImage(file="fondologin.png")
possa_imatge1 = canvas.create_image(0, 0, anchor=tk.NW, image=imatge_1)

root.mainloop()