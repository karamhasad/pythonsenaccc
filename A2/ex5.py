n1 = float(input("Qual nota da sua primeira avaliacao?"))
n2 = float(input("Qual nota da sua segunda avaliacao?"))
n3 = float(input("Qual nota da sua terceira avaliacao?"))

notadecorte=21
notamaxima=30
notafinal= n1+n2+n3


print(f"a {n2} por cento de {n1} é {percentual}")

if (percentual>70):
    print(f"Voce foi aprovado uma vez que sua media foi {percentual}, ficando acima de 70%")

else:
    print(f"voce reprovou pois sua media foi {percentual}, menor que 70%.")
