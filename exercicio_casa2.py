numeros = []
for x in range(0,5):
    n = int(input("Escreva um valor"))
    numeros.append(n)
print(numeros)

soma = 0
for i in numeros:
    soma+=i

print("A soma dos valores é: "+str(soma))

print("a media dos valores é: "+str(soma/len(numeros)))