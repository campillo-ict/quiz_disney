import tkinter as tk
from tkinter import messagebox
from api_login import *

user = ""
nomGrup="grup 1"

def mostrar_splash():
    #FINESTRA SPLASH
    global arrel  
    def mostrar_principal():
        splash.destroy()
        arrel.deiconify()
        
    splash = tk.Toplevel()
    splash.title("Carregant...")
    canvasSplash = tk.Canvas(splash, width=1000, height=600)
    canvasSplash.pack()
    splash.imatge_2 = tk.PhotoImage(file="SPLASH DISNEY.png") 
    possa_imatge2 = canvasSplash.create_image(0, 0, anchor=tk.NW, image=splash.imatge_2) 

    splash.after(3000, mostrar_principal)


def obrir_segona_finestra():
    #FINESTRA LOGIN
    def ferLogin():
        global user
        global nomGrup
        user = entradaUser.get()
        contra = entradaPass.get()
        #aqui fa el login
        if (api_login(nomGrup, user,password)):            
            messagebox.showinfo("benvingut", user)
            segona.destroy()
        else:
            messagebox.showerror("Usuari o contrasenya incorrecte")
            

    def ferSignUp():
        global user
        global nomGrup
        user = entradaUser.get()
        contra = entradaPass.get()
        #aqui fa el sign up
        if (api_register(nomGrup, user,contra)):
            segona.destroy()
        else:
            messagebox.showerror("Usuari o contraseña incorrecte")

   

    segona = tk.Toplevel(arrel)
    segona.title("LOGIN")
    segona.geometry("300x300")

    entradaUser = tk.Entry(segona, width=20)
    entradaUser.insert(0, "User")
    entradaUser.pack(pady=10)

    entradaPass = tk.Entry(segona, width=20)
    entradaPass.insert(0, "password")
    entradaPass.pack(pady=10)

    tk.Button(segona, text="Login", command=ferLogin).pack(pady=10)
    tk.Button(segona, text="sing up", command=ferSignUp).pack(pady=10)

    segona.grab_set()
    segona.focus_set()
    arrel.wait_window(segona)


  

# PANTALLA PRINCIPAL
arrel = tk.Tk()
arrel.title("Finestra principal")
arrel.geometry("300x200")
arrel.withdraw()  

tk.Button(arrel, text="Login", command=obrir_segona_finestra).pack(pady=50)

mostrar_splash()
arrel.mainloop()
