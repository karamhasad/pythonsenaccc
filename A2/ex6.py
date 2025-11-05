n1= float(input("Digite a nota da primeira prova"))
n2= float(input("Digite a nota da segunda prova"))
n3= float(input("Digite a nota da terceira prova"))
n4= float(input("Digite a nota da quarta prova"))

soma=n1+n2+n3+n4
media = soma/4
notamaxima=40
percentual=(soma*100)/40

if (media>=6):
    print(f"Voce foi aprovado pois sua nota foi {media} e ficou maior ou igual a 6. Voce teve {percentual}% de aproveitamento do curso")
else:
    print(f"Voce foi reprovado pois sua nota foi {media} e ficou abaixo de 6. Voce teve {percentual}% de aproveitamento do curso")
