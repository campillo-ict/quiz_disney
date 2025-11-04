import tkinter as tk
from tkinter import messagebox
from api_login import *

# Variable global per guardar el nom de l'usuari
user = ""
nomGrup="Pepes"

def mostrar_splash():
    #-------------------------FINESTRA SPLASH------------------------------------
    global arrel  
    def mostrar_principal():
        # Destrueix el splash i mostra la finestra principal
        splash.destroy()
        arrel.deiconify()
        
    splash = tk.Toplevel()
    splash.title("Carregant...")
    canvasSplash = tk.Canvas(splash, width=1000, height=547)
    canvasSplash.pack()
    # Contingut del splash
    # Carregar una imatge de fons, ha de ser png
    splash.imatge_2 = tk.PhotoImage(file="imatgeSplash.png") 
    possa_imatge2 = canvasSplash.create_image(0, 0, anchor=tk.NW, image=splash.imatge_2) 
    # Tanca el splash després de 3 segons i mostra la finestra principal
    splash.after(3000, mostrar_principal)


def obrir_segona_finestra():
    #-------------------------FINESTRA LOGIN----------------------------------------
    def ferLogin():
        global user
        global nomGrup
        user = entradaUser.get()
        contra = entradaPass.get()
        #aqui fa el login
        if (api_login(nomGrup, user,contra)):            
            messagebox.showinfo("Benvingut", user)
            segona.destroy()
        else:
            messagebox.showerror("ERROR")
            

    def ferSignUp():
        global user
        global nomGrup
        user = entradaUser.get()
        contra = entradaPass.get()
        #aqui fa el sign up
        if (api_register(nomGrup, user,contra)):
            segona.destroy()
        else:
            messagebox.showerror("ERROR")


        

    segona = tk.Toplevel(arrel)
    segona.title("LOGIN")
    segona.geometry("250x220")

    entradaUser = tk.Entry(segona, width=20)
    entradaUser.insert(0, "Usuari")
    entradaUser.pack(pady=10)

    entradaPass = tk.Entry(segona, width=20)
    entradaPass.insert(0, "Contrasenya")
    entradaPass.pack(pady=10)

    tk.Button(segona, text="Login", command=ferLogin).pack(pady=10)
    tk.Button(segona, text="Crear Usuari", command=ferSignUp).pack(pady=10)

    segona.grab_set()
    segona.focus_set()
    arrel.wait_window(segona)


  

# --------------PANTALLA PRINCIPAL-------------------------------------
arrel = tk.Tk()
arrel.title("Finestra principal")
arrel.geometry("300x200")
arrel.withdraw()  # Amaga la finestra principal fins que des de SPLASH la mostri

tk.Button(arrel, text="Login", command=obrir_segona_finestra).pack(pady=50)

mostrar_splash()
arrel.mainloop()
