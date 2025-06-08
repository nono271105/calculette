def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro"

def calculator():
    print("Bienvenue dans la calculatrice !")
    print("Options :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        choice = int(input("Choisissez une option (1/2/3/4) : "))
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
            
            if choice == 1:
                print("Résultat :", add(num1, num2))
            elif choice == 2:
                print("Résultat :", subtract(num1, num2))
            elif choice == 3:
                print("Résultat :", multiply(num1, num2))
            elif choice == 4:
                print("Résultat :", divide(num1, num2))
        else:
            print("Option invalide.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer des nombres.")

if __name__ == "__main__":
    calculator()