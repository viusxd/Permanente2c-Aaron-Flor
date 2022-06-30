from ast import Lambda
import tkinter as tk
from turtle import width
import random
import string
import time

def minusculas():
    return random.choice(string.ascii_lowercase)


def mayusculas():
    return random.choice(string.ascii_uppercase)


def simbolos():
    sim = ["@", "!", "$", "&", "."]
    return str(random.choice(sim))


def nums():
    return str(random.randint(1, 20))


def nums19():
    return str(random.randint(1, 9))


longitud_pss = random.randint(7, 11)

def Fcontra():
    global longitud_pss
    contra = []
    cont_final = []

    for i in range(longitud_pss):
        defs = [minusculas, mayusculas, simbolos, nums19]
        d_index = random.randint(0, 3)
        contra.append(defs[d_index]())
        cont_final = "".join(contra)
    return cont_final


def PIN4():
    pin4 = []
    p4f = []
    for i in range(4):
        pin4.append(nums19())
        p4f = "".join(pin4)
    return p4f

#def det_num():

    pinD = 0
    numdes = 0
    while numdes == 0:
        print("Desea crear o generar un PIN"
                       "\n1. Crear"
                       "\n2. Generar")
        numdes = input("Opción: ")

        while numdes == "1":
            try:
                pinD = int(input("Introduzca su PIN: "))
                tam_pinD = len(str(pinD))
            except ValueError:
                print("El PIN debe contener sólo numeros.")
                continue

            if tam_pinD >= 5 or tam_pinD <= 3:
                print("El PIN debe ser de 4 cifras")
                numdes = "1"
            elif tam_pinD <= 4:
                print("Tu PIN es: "+ str(pinD))
                return pinD

        if numdes == "2":
            pinD = PIN4()
            print("Tu PIN es: " + str(pinD))
            return str(pinD)

        else:
            print("No es una opcíon válida.")
            numdes = 0
            time.sleep(1)

#def des_num():
    numE = int(det_num())
    Fnum = 0

    print("El numero es "+ str(numE))
    time.sleep(2)

    while Fnum != numE:
        Fnum = random.randint(1000, 9999)
        print(Fnum)
    print("Tu PIN es "+ str(numE))

def limp_widgets(frame): # Se encarga de limpiar las ventanas luego de cambiarlas.
    for widget in frame.winfo_children():
        widget.destroy()

def cargar_f1(): # Pantalla 1
    limp_widgets(frame2)
    limp_widgets(frame3)
    frame1.tkraise()
    frame1.pack_propagate(False)
    
    #Textos y botones
    tk.Label(
        frame1, text = "¿Qué desea hacer?",
        bg = bg_color,
        fg = "white",
        font = ("TkMenuFont", 50)
        ).pack(pady = 60)

    tk.Button(
        frame1, text = "Generar contraseña",
        font = ("TkHeadingFont", 20),
        bg = "#190719",
        fg = "white",
        cursor = "hand2",
        activebackground = "#badee2",
        activeforeground = "black",
        command =lambda:cargar_f2()).pack(pady = 20)
    
    tk.Button(
        frame1, text = "Generar PIN de 4 números",
        font = ("TkHeadingFont", 20),
        bg = "#140718",
        fg = "white",
        cursor = "hand2",
        activebackground = "#badee2",
        activeforeground = "black",
        command =lambda:cargar_f3()).pack(pady = 20)

#Ventana N°2
def cargar_f2():
    limp_widgets(frame1)
    frame2.tkraise()
    frame2.pack_propagate(False)
    cont_f = str(Fcontra())
    tk.Label(
        frame2, text = "Su contraseña es:",
        bg = bg_color,
        fg = "white",
        font = ("TkMenuFont", 40)
        ).pack(pady = 60)
    tk.Button(
        frame2, text = cont_f,
        bg = "#140718",
        fg = "white",
        font = ("TkMenuFont", 40)
        ).pack(pady = 50)

    tk.Button(
        frame2, text = "Atrás",
        font = ("TkHeadingFont", 20),
        bg = "#140718",
        fg = "white",
        cursor = "hand2",
        activebackground = "#badee2",
        activeforeground = "black",
        command =lambda:cargar_f1()).pack(pady = 30)

#Ventana N°3
def cargar_f3():
    limp_widgets(frame1)
    frame3.tkraise()
    frame3.pack_propagate(False)
    pin_f = str(PIN4())
    tk.Label(
        frame3, text = "Su PIN es:",
        bg = bg_color,
        fg = "white",
        font = ("TkMenuFont", 40)
        ).pack(pady = 60)
    tk.Button(
        frame3, text = pin_f,
        bg = "#140718",
        fg = "white",
        font = ("TkMenuFont", 40)
        ).pack(pady = 50)

    tk.Button(
        frame3, text = "Atrás",
        font = ("TkHeadingFont", 20),
        bg = "#140718",
        fg = "white",
        cursor = "hand2",
        activebackground = "#badee2",
        activeforeground = "black",
        command =lambda:cargar_f1()).pack(pady = 30)


# Para iniciar
ventana = tk.Tk()
ventana.title("sí")
ventana.eval("tk::PlaceWindow . center") #puede ser tambien ventana.geometry("n de pixeles x n de pixeles")

bg_color = "#220A29"

#Especificaciones de las ventanas
frame1 = tk.Frame(ventana, width = 960, height = 600, bg = bg_color)
frame2 = tk.Frame(ventana, bg = bg_color)
frame3 = tk.Frame(ventana, bg = bg_color)

for frame in (frame1, frame2, frame3):
    frame.grid(row = 0, column = 0, sticky="nesw")

cargar_f1()

# Inicio
ventana.mainloop()
