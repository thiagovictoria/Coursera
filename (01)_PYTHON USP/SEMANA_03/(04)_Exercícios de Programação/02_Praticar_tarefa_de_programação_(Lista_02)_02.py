import math
a = float(input("Digite a constante A? "))
b = float(input("Digite a constante B? "))
c = float(input("Digite a constante C? "))

delta = ((b**2)-(4*a*c))


if delta >0:
    x1= (-b + math.sqrt(delta))/(2*a)
    x2= (-b - math.sqrt(delta))/(2*a)
    if(x1 > x2):
        print ("as raízes da equação são", x2,"e", x1)
    else:
        print ("as raízes da equação são", x1,"e", x2)
elif delta==0:
    x= (-b)/(2*a)
    print ("a raiz desta equação é", x)
else:
        print ("esta equação não possui raízes reais")
