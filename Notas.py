nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7.0:
    print("Parabéns! Você foi aprovado com média:", media)
else:
    print("Infelizmente, você foi reprovado com média:", media)
