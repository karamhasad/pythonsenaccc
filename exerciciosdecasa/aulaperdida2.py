import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
'dias': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
'Venda': [500, 200, 1000, 150, 1950]})
plt.bar(df['dias'], df['Venda'], color='blue')
plt.title('Vendas por Dias')
plt.xlabel('Dia da Semana')
plt.ylabel('Valor Vendido')
plt.show()