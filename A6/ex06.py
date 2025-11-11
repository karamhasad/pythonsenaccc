n=0
while n>=0 and n<=10:
    try:
        n=int(input('digite um numero de 0 a 10'))
        print('Uhuuuuuuuuuuuuul')
    except ValueError:
        print('Entrada inavalida. Digite outro numero')
print(f'Nota invalida registrada: {n}')