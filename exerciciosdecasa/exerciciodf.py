import pandas as pd
import numpy as np

df_pesquisa = pd.read_csv('exerciciosdecasa/pesquisa_satisfacao.csv', sep = ';')
#print(df_pesquisa)


temp_array= np.array(df_pesquisa['Tempo de Espera (min)'])

media_temp = np.mean(temp_array)
mediana_temp = np.median(temp_array)

q1_temp = np.quantile(temp_array, 0.25)
q2_temp = np.quantile(temp_array, 0.50)
q3_temp = np.quantile(temp_array, 0.75)

print(f'A media é {media_temp}')
print(f'A mediana é {mediana_temp}')
print(f'O primeiro quantis é {q1_temp}')
print(f'O segundo quantis é {q2_temp}')
print(f'O terceiro quantis é {q3_temp}')

print('------------------------------------------')
df_satisf_alta = df_pesquisa[df_pesquisa['Satisfação'] == 'Alta']
#print(df_satisf_alta)


temp_satisf_alt_array = np.array(df_satisf_alta['Tempo de Espera (min)'])

media_satisf_alt = np.mean(temp_satisf_alt_array)
mediana_satisf_alt = np.median(temp_satisf_alt_array)

q1_satisf_alt = np.quantile(temp_satisf_alt_array, 0.25)
q2_satisf_alt = np.quantile(temp_satisf_alt_array, 0.50)
q3_satisf_alt = np.quantile(temp_satisf_alt_array, 0.75)


print(f'A media é {media_satisf_alt}')
print(f'A mediana é {mediana_satisf_alt}')
print(f'O primeiro quantis é {q1_satisf_alt}')
print(f'O segundo quantis é {q2_satisf_alt}')
print(f'O terceiro quantis é {q3_satisf_alt}')


#Comentario: Em geral, todos os dados (media, mediana, q1,q2 e q3) apresentam uma tendência de espera menor no recorte de alta satisfação.