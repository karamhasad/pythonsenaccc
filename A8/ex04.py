def dividir(a,b):
    try:
        resultado = (a + b)/2
    except ZeroDivisionError:
        print('Digite um número diferente de zero')
    except ValueError:
        print('Digite um valor válido')
    else:
        print(f'A média é {resultado}')
    finally:
        print('Encerrando operação.')

num1=float(input('Digite um valor'))
num2=float(input('Digite outro valor'))
media = dividir(num1,num2)