def ler_inteiro():
    try:
        numero=int(input('Digite um numero inteiro'))
    except ValueError:
        print('Erro: Voce deve digitar apenas numeros inteiro!')
    else:
        print(f'Numero digitado com sucesso {numero}')
    finally:
        print('Fim do programa de conversão')

ler_inteiro()
