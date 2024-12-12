#Tarea Numero 2
   #Edison Cabezas
     #Tercer Semestre Carrera Desarrollo de Software
        #Deber de adivinar un numero, del 1 al 100, dando la oportunidad de 10 intentos.

import tkinter as tk
from tkinter import messagebox
import random


class NumeroAdivinarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Adivinar el Numero")

        # Configurar el tamaño de la ventana
        self.root.geometry("400x400")
        self.root.config(bg="#808080")  # Fondo gris claro

        # Rango de números a adivinar
        self.min_num = 1
        self.max_num = 100
        self.intentos_maximos = 10

        # Generación del número aleatorio
        self.numero_correcto = random.randint(self.min_num, self.max_num)

        # Inicialización de los intentos
        self.intentos_restantes = self.intentos_maximos

        # Crear los widgets
        self.crear_widgets()

    def crear_widgets(self):
        # Etiqueta de instrucción (con fondo y color)
        self.intento_label = tk.Label(self.root, text="Ingresa un número:", font=("Castellar", 13), bg="#000000", fg="white")
        self.intento_label.pack(pady=10)

        # Campo de texto para ingresar el intento
        self.intento_entry = tk.Entry(self.root, font=("Castellar", 13), width=10)
        self.intento_entry.pack(pady=10)

        # Botón de adivinar con color personalizado
        self.adivinar_button = tk.Button(self.root, text="Adivinar", font=("Castellar", 13), bg="#000000", fg="white",
                                         command=self.adivinar_numero)
        self.adivinar_button.pack(pady=10, ipadx=10, ipady=5)

        # Retroalimentación del juego
        self.retroalimentacion_label = tk.Label(self.root, text="", font=("Castellar", 13), bg="#000000")
        self.retroalimentacion_label.pack(pady=10)

        # Número de intentos restantes
        self.intentos_label = tk.Label(self.root, text=f"Intentos restantes: {self.intentos_restantes}",
                                       font=("Castellar", 13), bg="#000000")
        self.intentos_label.pack(pady=10)

        # Botón de reiniciar con color personalizado
        self.reiniciar_button = tk.Button(self.root, text="Reiniciar", font=("Castellar", 13), bg="#FF5722", fg="white",
                                          command=self.reiniciar_juego)
        self.reiniciar_button.pack(pady=10, ipadx=10, ipady=5)

    def adivinar_numero(self):
        intento = self.intento_entry.get()

        # Validar que el intento sea un número válido
        if not intento.isdigit():
            messagebox.showerror("NO", "ingresa un número válido.")
            return

        intento = int(intento)

        if intento < self.min_num or intento > self.max_num:
            messagebox.showerror("NO", f"El número debe estar entre {self.min_num} y {self.max_num}.")
            return

        # Aqui se empiezan a restar los intentos que se vayan realizando.
        self.intentos_restantes -= 1
        self.intentos_label.config(text=f"Te quedan estos intentos: {self.intentos_restantes}")

        # Verificamos el numero
        if intento == self.numero_correcto:
            self.retroalimentacion_label.config(text="¡Felicidades! Has adivinado el número.", fg="#4CAF50")
            self.intentos_label.config(text="¡Felicidades!", fg="#4CAF50")
            self.adivinar_button.config(state="disabled")
        elif intento < self.numero_correcto:
            self.retroalimentacion_label.config(text="Numero muy bajo. Intenta con un número más alto.", fg="#FF9800")
        else:
            self.retroalimentacion_label.config(text="Numero muy alto. Intenta con un número más bajo.", fg="#FF9800")

        # Aqui comprobamos que la cantidad de intentos permitidos, a sido completada
        if self.intentos_restantes == 0:
            self.retroalimentacion_label.config(text=f"Has perdido. El número correcto era {self.numero_correcto}.",
                                                fg="#f44336")
            self.intentos_label.config(text="¡Perdiste!", fg="#f44336")
            self.adivinar_button.config(state="disabled")

    def reiniciar_juego(self):
        # Aqui reiniciamos los intentos del juego.
        self.numero_correcto = random.randint(self.min_num, self.max_num)
        self.intentos_restantes = self.intentos_maximos
        self.intento_entry.delete(0, tk.END)
        self.retroalimentacion_label.config(text="", fg="black")
        self.intentos_label.config(text=f"Intentos restantes: {self.intentos_restantes}", fg="black")
        self.adivinar_button.config(state="normal")
        self.intentos_label.config(text=f"Intentos restantes: {self.intentos_restantes}")


# Creamos la ventana principal de la aplicacion
root = tk.Tk()
app = NumeroAdivinarApp(root)

# Iniciamos la aplicación
root.mainloop()