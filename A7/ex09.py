def indicador(a,b):
    if a > b: 
        return print(f"{a} é maior que {b}")
    else:
        return print(f"{b} é maior que {a}")

num1= int(input('Digite um numero'))
num2= int(input('Digite outro numero'))

maior=indicador(num1,num2)
