import function as f
def checkEntree():
    while True:
        nombre1 = input("Entrez le premier nombre : ")
        nombre2 = input("Entrez le deuxième nombre : ")
        
        if not(nombre1.isnumeric()) or not(nombre2.isnumeric()):
            print("Veuillez entrer des nombres valides.")
        else:
            break
    
    return float(nombre1), float(nombre2)

i = 1
def checkOp(op,nombre1,nombre2):
    if (op == 1):
        return f.addition(nombre1,nombre2)
    if (op == 2):
        return f.soustraction(nombre1,nombre2)
    if (op == 3):
        return f.multiplication(nombre1,nombre2)
    if (op == 4):
        return f.division(nombre1,nombre2)
    else :
        print("vérifier l'entrée\n")
        operation = float(input("operation : "))
        checkOp(operation,nombre1,nombre2)
while (i == 1):
    premier,second=checkEntree()
    print("tapez 1 pour addition\n tapez 2 pour soustraction\n tapez 3 pour multiplication\n tapez 4 pour division\n")
    operation = float(input("operation : "))
    result = checkOp(operation,premier,second)
    print(result)
    i = float(input("tapez 1 pour effectuer une autre operation et tout autre touche pour quitter: "))
