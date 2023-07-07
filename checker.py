import function as f
def checkEntree():
    while (True):
        nombre1 = input("Entrez le premier nombre : ")
        nombre2 = input("Entrez le deuxième nombre : ")
        if not (nombre1.replace('.', '', 1).replace('-', '', 1).isdigit()) or not (nombre2.replace('.', '', 1).replace('-', '', 1).isdigit()):
            print("Veuillez entrer des nombres valides.")
        else:
            break
    return float(nombre1), float(nombre2)

"""   while True:
        nombre1 = input("Entrez le premier nombre : ")
        nombre2 = input("Entrez le deuxième nombre : ")
        
        if not(nombre1.isnumeric()) or not(nombre2.isnumeric()):
            print("Veuillez entrer des nombres valides.")
        else:
            break
    
    return float(nombre1), float(nombre2)
"""

def checkOp(op,nombre1,nombre2):
    if (op == 1):
        return f.addition(nombre1,nombre2)
    if (op == 2):
        return f.soustraction(nombre1,nombre2)
    if (op == 3):
        return f.multiplication(nombre1,nombre2)
    if (op == 4):
        return f.division(nombre1,nombre2)
    if (op == 5):
        return f.puissance(nombre1,nombre2)
    else :
        print("vérifier l'entrée\n")
        operation = float(input("operation : "))
        return  checkOp(operation,nombre1,nombre2)