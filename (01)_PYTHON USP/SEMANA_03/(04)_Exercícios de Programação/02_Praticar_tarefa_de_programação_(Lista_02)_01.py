x1 = float(input("Digite um número:"))
y1 = float(input("Digite um número:"))
x2 = float(input("Digite um número:"))
y2 = float(input("Digite um número:"))

dist = (((x1 - x2)**2) + ((y1 - y2)**2))**0.5

if (dist >= 10 ):
    print("longe")
else:
    print("perto")
