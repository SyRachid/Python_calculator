def  multiplication(a,b):
    return(a*b)
def division(a,b):
    if b == 0:
        raise ValueError("division par 0 impossible")
    else :
        return(a/b)