#Exerc_01
'''
Quantas vezes o programa executará a linha 6 (# Iteração)?

x = 1
cont = 0
while x < 3:
    y = 0
    while y <= 4:
        # Iteração
        y = y + 1
    x = x + 1

10
'''
  
#Exerc_02

'''
Quantas vezes será impressa a palavra "oi" ao ser executado o código abaixo?



fora = 5
while fora > 0:
  dentro = 0
  while dentro < fora:
    print("oi")
    dentro = dentro + 1
  fora = fora - 1

15
'''

#Exerc_03

'''
programa que imprima a tabuada de 1 a 10
'''

def tabuada():

'''
-------------------------------------------------------
    tab = 1
    while tab <= 10:
        print("Tabuada do", tab, ":", end="\t")
        i = 1
        while i <= 10:
            print(tab*i, end = "\t")
            i = i + 1
        print()
        tab = tab + 1

----------------------------------------------------------
  tab = 1
    while tab <= 10:
        i = 1
        while i <= 10:
            print(tab,"x",i,"=",tab*i)
            i = i + 1
        print()
        tab = tab + 1
----------------------------------------------------------
    tab = 0
    while tab < 10:
        tab = tab + 1
        i = 0
        while i < 10:
            i = i + 1
            print(tab,"x",i,"=",tab*i)
        print()
'''


#Exerc_04

'''
Quantas vezes a linha 6 (#comando qualquer) será executada?

x = 2
cont = 0
while x >= 0:
    y = 0
    while y >= 4:
        #comando qualquer
        y = y + 1
    x = x - 1

nenhuma
'''

#Exerc_05

'''
Quantas vezes a linha 6 (#comando qualquer) será executada?

x = 2
cont = 0
while x >= 0:
    y = 0
    while y <= 4:
        #comando qualquer
        y = y - 1
    x = x - 1
    
infinita
'''

#Exerc_06

'''
i = 0
while i < 3:
  j = 0
  while j < 3:
    #expressão
    print(3*i+j+1,end="")  
    j = j + 1
  i = i + 1
'''

#Exerc_07

'''
x = 1
while x < 3:
    y = 1
    while y < 3:
        print(x*y, end = "\t")
        y = y + 1
    x = x + 1
'''

















