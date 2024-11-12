bs = int(input("Digite o valor para a base "))
ex = int(input("Digite o valor para o expoente "))

n = bs
for i in range(0,ex-1):
    n = n * bs

print("O resultado da potencia é "+str(n))