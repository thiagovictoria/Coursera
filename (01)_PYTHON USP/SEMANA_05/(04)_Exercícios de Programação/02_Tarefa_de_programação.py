def éprimo(k):
    #IDÉIA: numero primo é quando o numero é dividido APENAS por ele e por 01. Logo, abaixo iremos contar contadores de 01 até o numero inserido e verificar onde há resto 0. 
    inicio = 1
    contar_divisores = 0
    while inicio <= k:
        if k % inicio == 0:
            contar_divisores += 1
        inicio += 1

    if contar_divisores > 2:
        return False
    else:
        return True

def maior_primo(x):
    inicio = 2
    primo_maior = 0
    while inicio <= x:
        if éprimo(x) == True:
            primo_maior = x
            return primo_maior
        x = x -1
    return x
    
        
    
    

    




    
