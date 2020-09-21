
import math

'''
a = float(input("Digite a constante A? "))
b = float(input("Digite a constante B? "))
c = float(input("Digite a constante C? "))


delta = ((b**2)-(4*a*c))

if delta >0:
    x1= (-b + math.sqrt(delta))/(2*a)
    x2= (-b - math.sqrt(delta))/(2*a)
    print ("As raizes são", x1,"e", x2)

elif delta==0:
    x= (-b)/(2*a)
    print ("A raiz é", x)
else:
        print (" Não há raizes reais")

'''

# Refatorando (mesma lógica do anterior)

def delta (a,b,c):
    return((b**2)-(4*a*c))

def main():
    a_digitado = float(input("Digite a constante A: "))
    b_digitado = float(input("Digite a constante B: "))
    c_digitado = float(input("Digite a constante C: "))
    imprime_raizes(a_digitado,b_digitado,c_digitado) # imprime_raizes(a,b,c): chamada de função

def imprime_raizes(a,b,c):
    d = delta(a,b,c)# delta(a,b,c): chamada de função
                    # d => variável local
    if d >0: 
        x1= (-b + math.sqrt(d))/(2*a)
        x2= (-b - math.sqrt(d))/(2*a)
        print ("As raizes são", x1,"e", x2)
    elif d==0:
        x= (-b)/(2*a)
        print ("A raiz é", x)
    else:
        print (" Não há raizes reais")
