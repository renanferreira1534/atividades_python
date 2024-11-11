alimentos = ["Maça","Arroz","Feijão"]
categoria = ("Grãos","Frutas","Legumes")
pessoa = {"Nome":"paula","Idade":"38","Altura":"1.65"}

print(alimentos)
print(type(alimentos))
print(len(alimentos))
# adicionar masi um alimneto
alimentos.append("Macarrão")
print(alimentos)
print(len(alimentos))

print(categoria)
print(type(categoria))
print(len(categoria))

print(pessoa)
print(type(pessoa))
print(len(pessoa))
# adicionar masi um item a pessoa
#adicionar uma nova chave com o seu respectivo valor
# esta sendo adicionado a chave email com o valor 
# email da pessoa
pessoa["Email"]="paula@gmail.com"
print(pessoa)
print(len(pessoa))
