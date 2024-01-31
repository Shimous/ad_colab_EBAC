# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_gasolina = pd.read_csv('gasolina.csv', sep=',')

grafico = sns.lineplot(df_gasolina, x='dia', y='venda')
grafico.set(title='Preço da gasolina', xlabel='Dia', ylabel='Preço (R$)')
plt.savefig('gasolina.png')