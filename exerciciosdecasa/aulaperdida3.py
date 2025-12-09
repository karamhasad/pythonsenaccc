import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
'dias': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
'Venda': [500, 200, 1000, 150, 1950]})

plt.barh(df['Produto'],df['Vendas'])
plt.title('Vendas por Produto(Horizontal)') 
plt.xlabel('Vendas')
plt.ylabel('Produto')
plt.show()git 