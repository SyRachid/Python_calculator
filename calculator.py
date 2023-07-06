import function as f
import checker as c
i = 1
while (i == 1):
    premier,second=c.checkEntree()
    print("tapez 1 pour addition\n tapez 2 pour soustraction\n tapez 3 pour multiplication\n tapez 4 pour division\n")
    operation = float(input("operation : "))
    result = c.checkOp(operation,premier,second)
    print("le résultat est "+str(result))
    i = float(input("tapez 1 pour effectuer une autre operation et tout autre touche pour quitter: "))
