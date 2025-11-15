def calculadora():
    try:
        a=float(input('Digite o primeiro numero:'))
        b=float(input('Digite o segundo numero:'))
        op=input('Digite a operação (+,-,*,/):')

        match op:
            case '+':
                resultado = a + b
            case '-':
                resultado = a - b
            case '*':
                resultado = a * b
            case '/':
                resultado = a / b 
            case _:
                raise ValueError ("Operação Invalida")
    except ZeroDivisionError:
        print('Erro: divisão por zero')
    except ValueError as e:
        print (f'{e}')
    else:
        print(f'Resultado {resultado}')
    finally:
        print('Calculo encerrado.')

calculadora()