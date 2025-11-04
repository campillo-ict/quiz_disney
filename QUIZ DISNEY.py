import tkinter as tk
from tkinter import messagebox
import json
import os


def cargar_usuarios():
    """Carga los usuarios del archivo JSON."""
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            return json.load(f)
    else:
        return {}

def guardar_usuarios(usuarios):
    """Guarda los usuarios en el archivo JSON."""
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f, indent=4)


def registrar():
    usuario = entry_usuario.get().strip()
    contrasena = entry_contrasena.get().strip()

    if not usuario or not contrasena:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        return

    usuarios = cargar_usuarios()
    if usuario in usuarios:
        messagebox.showerror("Error", "El usuario ya existe.")
        return

    usuarios[usuario] = contrasena
    guardar_usuarios(usuarios)
    messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
    entry_usuario.delete(0, tk.END)
    entry_contrasena.delete(0, tk.END)

def iniciar_sesion():
    usuario = entry_usuario.get().strip()
    contrasena = entry_contrasena.get().strip()

    usuarios = cargar_usuarios()

    if usuario in usuarios and usuarios[usuario] == contrasena:
        messagebox.showinfo("Bienvenido", f"Inicio de sesión exitoso.\n¡Hola, {usuario}!")
        entry_usuario.delete(0, tk.END)
        entry_contrasena.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")


root = tk.Tk()
root.title("Sistema de Login con Tkinter")
root.geometry("350x250")
root.resizable(False, False)

titulo = tk.Label(root, text="Log in / Sing up", font=("Calibri", 14, "bold"))
titulo.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Usser:", font=("Lexend", 11)).grid(row=0, column=0, pady=5, padx=5)
entry_usuario = tk.Entry(frame, font=("Lexend", 11))
entry_usuario.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Password:", font=("Lexend", 11)).grid(row=1, column=0, pady=5, padx=5)
entry_contrasena = tk.Entry(frame, show="*", font=("Lexend", 11))
entry_contrasena.grid(row=1, column=1, pady=5)

frame_botones = tk.Frame(root)
frame_botones.pack(pady=15)

btn_login = tk.Button(frame_botones, text="Log in", width=17, command=iniciar_sesion)
btn_login.grid(row=0, column=0, padx=10)

btn_registro = tk.Button(frame_botones, text="Sing up", width=17, command=registrar)
btn_registro.grid(row=0, column=1, padx=10)

root.mainloop()



holi caracoli 