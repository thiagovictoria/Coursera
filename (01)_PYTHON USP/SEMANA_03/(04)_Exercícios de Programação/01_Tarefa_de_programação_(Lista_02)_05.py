x = int(input("Digite um número inteiro:"))
y = int(input("Digite um número inteiro:"))
z = int(input("Digite um número inteiro:"))

lista=[x,y,z]

if (lista[0]<lista[1] and lista[1]<lista[2]):
    print("Crescente")
else:
    print("Não está em ordem crescente")
