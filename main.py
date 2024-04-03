import tkinter as tk
from tkinter import messagebox


def calcular_mcd(a, b):
    if a == 0 and b == 0:
        return None
    while b != 0:
        a, b = b, a % b
    return abs(a)


def limpiar_campos():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)


def calcular_y_mostrar_mcd():
    num1_str = entry_num1.get()
    num2_str = entry_num2.get()

    if not num1_str.isdigit() or not num2_str.isdigit():
        messagebox.showerror("Error", "Por favor, ingresa solo números enteros positivos.")
        limpiar_campos()
        return

    num1, num2 = int(num1_str), int(num2_str)
    if num1 <= 0 or num2 <= 0:
        messagebox.showerror("Error", "Por favor, ingresa números enteros positivos.")
        limpiar_campos()
        return

    resultado = calcular_mcd(num1, num2)
    if resultado is None:
        messagebox.showinfo("Resultado", "El máximo común divisor de 0 no está definido.")
    else:
        messagebox.showinfo("Resultado", f"El máximo común divisor de {num1} y {num2} es: {resultado}")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora de MCD")

# Etiquetas y campos de entrada
label_num1 = tk.Label(ventana, text="Primer número:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = tk.Label(ventana, text="Segundo número:")
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Botón para calcular el MCD
btn_calcular = tk.Button(ventana, text="Calcular MCD", command=calcular_y_mostrar_mcd)
btn_calcular.grid(row=2, columnspan=2, padx=5, pady=5)

# Ejecutar la ventana
ventana.mainloop()
