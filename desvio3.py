nota = int(input("Digite a nota: "))

if nota > 85 and nota <= 100:
    print("Parabens voce tirou nota A...")
elif nota > 60 and nota <=85:
    print("Parabes voce tirou nota b+...")
elif nota > 40 and nota <= 60:
    print("Voce tirou nota b...")
elif nota > 30 and nota <= 40:
    print("Voce tirou nota c...")
else:
    print("Voce esta reprovado!")
    
