def  multiplication(a,b):
    return(a*b)
def division(a,b):
    if b == 0:
        raise ValueError('divisble par 0 impossible')
    else :
        return(a/b)
def addition(a,b):
    return(a+b)
def soustraction(a,b):
    return(a-b)
def puissance (a,b):
    return pow(a,b)