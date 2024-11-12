numero = []
for x in range(0,5):
    p = int(input("escreva o valor: "))
    numero.append(p)

m = numero[0]
for x in numero:
    if x > m:
        m = x
print("O valor maior é "+str(m))
