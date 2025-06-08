import tkinter as tk
from tkinter import messagebox

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation.get()

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            messagebox.showerror("Erreur", "Opération invalide")
            return

        label_result.config(text=f"Résultat : {result}")

    except ValueError as ve:
        messagebox.showerror("Erreur", f"Erreur de saisie : {ve}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur inattendue : {e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Entrée du premier nombre
tk.Label(root, text="Premier nombre :").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

# Entrée du deuxième nombre
tk.Label(root, text="Deuxième nombre :").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Choix de l’opération via un menu déroulant
tk.Label(root, text="Opération :").grid(row=2, column=0, padx=10, pady=5)
operation = tk.StringVar(root)
operation.set('+')  # valeur par défaut
option_menu = tk.OptionMenu(root, operation, '+', '-', '*', '/')
option_menu.grid(row=2, column=1, padx=10, pady=5)

# Bouton calculer
btn_calculate = tk.Button(root, text="Calculer", command=calculate)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Label pour afficher le résultat
label_result = tk.Label(root, text="Résultat : ")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Boucle principale Tkinter
root.mainloop()
