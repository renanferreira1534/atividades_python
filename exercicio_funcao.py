def soma (num1,num2):
    return num1 + num2
   

def converter_celcius(tempcelcius):
    fahrehein = 1.8 * tempcelcius + 32
    return fahrehein


def parimpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    


def inverter(texto):
    tam = len(texto)
    # criar variavel que devolve o texto invertido
    txt_invertido=""
    for i in range(tam-1,-1,-1):
        txt_invertido = texto[i]
    return txt_invertido


def palindromedo(palavra): Ovo == ovO
    palavra = palavra.lower()
    cp_palavra = palavra
    if cp_palavra==inverter(palavra):
        return "É um palindromo"
    else:
        return "Não é um palindromo"
         