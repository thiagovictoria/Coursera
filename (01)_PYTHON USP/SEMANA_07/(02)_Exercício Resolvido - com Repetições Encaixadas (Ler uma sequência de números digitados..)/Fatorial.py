'''
Exercício de aula:

n = int(input("Digite uma numero inteiro positivo: "))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n -1
    print(fatorial)
    n = int(input("Digite uma numero inteiro positivo: "))

'''

# Desafio de aula

def main():
    n = int(input("Digite uma numero inteiro positivo: "))
    calculo (n)

def calculo(a):
    while a >= 0:
        fat(a)
        a = int(input("Digite uma numero inteiro positivo: "))
      
def fat(x):
    fatorial = 1
    while x > 1:
        fatorial = fatorial * x
        x = x - 1
    print(fatorial)
