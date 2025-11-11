produto = input("Digite o nome do produto").strip().lower()

if (produto=="mouse"):
    preco=10
elif (produto =="teclado"):
    preco=20
elif (produto=="memoria"):
    preco=100
else:
    preco = 0
    print("Produto nao encontrado")

quantidade = int(input("Quantos produtos desse voce comprara?"))

total=quantidade*preco

if (quantidade>10):
    imposto=total*0.05
else:
    imposto=total*0.10

v_final=(total+imposto)
<<<<<<< HEAD
print(f"Voce comprou {quantidade} {produto}s, sob o preco bruto de {total} gerando um acrescimo {imposto} reais . O valor final da sua compra é {v_final}.")
=======
print(f"Voce comprou {quantidade} {produto}s, sob o preco bruto de {total} gerando um acrescimo {imposto} reais . O valor final da sua compra é {v_final}.")



teste!

tesste
>>>>>>> 445d0c8fbd5bd356679a19bfc22b62a746f44779
