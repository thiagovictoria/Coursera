n = int(input("Digite um numero:"))
x=0
while n>0:
    i=n%10
    x+=i
    n=n//10
print(x)
