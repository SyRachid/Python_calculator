def entree():
    print("entrez le premier nombre\n") 
    premier=input("nombre 1: ")
    print("entrez le deuxième nombre: ")
    second = input("nombre 2: ")
def checkEntree():
    while (type(premier)!=number and type(second)!=number):
        entree()
i = 1
def checkOp(op,nombre1,nombre2):
    if (op == 1):
        return addition(nombre1,nombre2)
    if (op == 2):
        return soustraction(nombre1,nombre2)
    if (op == 3):
        return multiplication(nombre1,nombre2)
    if (op == 4):
        return division(nombre1,nombre2)
    else :
        print("vérifier l'entrée\n")
        operation = input("operation : ")
        checkOp(operation,nombre1,nombre2)
while (i == 1):
    entree()
    checkEntree()
    print("tapez 1 pour addition\n,tapez 2 pour soustraction, tapez 3 pour multiplication\n, tapez 4 pour division")
    operation = input("operation : \n")
    result = checkOp(operation,premier,second)
    print("le resultat est "+result+"\n")
    i = input("tapez 1 pour effectuer une autre operation et 0 pour quitter: ")
