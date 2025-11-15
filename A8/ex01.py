var = input('Digite uma palavra')
vogal = ['a','e','i','o','u', 'A', 'E', 'I','O', 'U']
def contar_letras(palavra):
    contadorgeral=0
    for _ in palavra:
            contadorgeral+=1
    return contadorgeral

def contar_vogais(palavra):
    contadorvogal=0
    for _ in palavra:
        if _ in vogal:
            contadorvogal+=1
    return contadorvogal

def contar_conso(palavra):
    contadorconsoante=0
    for _ in palavra:
         if _ not in vogal:
              contadorconsoante+=1
    return contadorconsoante

vogais =contar_vogais(var)
consoantes = contar_conso(var)
letras = contar_letras(var)
print (f"A palavra {var} tem {letras} letras, sendo {vogais} vogais e {consoantes}")
