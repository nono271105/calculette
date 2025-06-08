import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculatrice")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expression = ""

        # Affichage (Entry non éditable par l’utilisateur directement)
        self.entry = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        self.entry.configure(state='readonly')

        # Création des boutons
        buttons = [
            ('C', 1, 0), ('±', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3),
        ]

        for (text, row, col, colspan) in [(b[0], b[1], b[2], b[3] if len(b) > 3 else 1) for b in buttons]:
            button = tk.Button(self, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        # Configuration des poids pour que les boutons s’étendent correctement
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_entry()
        elif char == '±':
            # Changer le signe du nombre en cours
            if self.expression:
                if self.expression.startswith('-'):
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
                self.update_entry()
        elif char == '=':
            try:
                # Évaluer l'expression mathématique
                result = str(eval(self.expression))
                self.expression = result
                self.update_entry()
            except Exception:
                self.expression = ""
                self.update_entry()
                self.entry.configure(state='normal')
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erreur")
                self.entry.configure(state='readonly')
        elif char == '%':
            try:
                val = float(self.expression)
                val /= 100
                self.expression = str(val)
                self.update_entry()
            except Exception:
                pass
        else:
            self.expression += char
            self.update_entry()

    def update_entry(self):
        self.entry.configure(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)
        self.entry.configure(state='readonly')

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()

