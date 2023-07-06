import function as f
import checker as c
i = 1
while (i == 1):
    premier,second=c.checkEntree()
    print("\n")
    print("tapez 1 pour addition\ntapez 2 pour soustraction\ntapez 3 pour multiplication\ntapez 4 pour division\n")
    operation = float(input("operation : "))
    result = c.checkOp(operation,premier,second)
    print("\n")
    print("le résultat est "+str(result))
    print("\n")
    i = float(input("tapez 1 pour effectuer une autre operation et tout autre touche pour quitter: "))
    print("\n")