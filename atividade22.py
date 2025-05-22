import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('ecommerce_estatistica.csv')
#Historiograma

plt.hist(df['Preço'], bins=20, alpha=0.7, color='orange')
plt.title("A historiografia dos preços")
plt.xlabel("preços")
plt.ylabel("Quantidade")
plt.grid(True)
# plt.show()

#Grafico de mapa de calor
core = df[['Nota','N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod', 'Nota_MinMax', 'N_Avaliações_MinMax','Desconto_MinMax','Preço_MinMax', 'Marca_Cod','Material_Cod','Temporada_Cod','Marca_Freq', 'Material_Freq']].corr()
plt.title("Mapa de Calor da correlação entre Variáveis")
sns.heatmap(core, annot=True, fmt='.2f')
# plt.show()

# #Grafico de Dispersão
plt.scatter(df['Preço'],df['Preço'])
plt.title("Dispersão do preço")
plt.xlabel("Preço")
plt.ylabel("Preço")
plt.grid(True)
plt.show()

## Grafico de Pizza
x1=df['Temporada'].value_counts().index
y1=df['Temporada'].value_counts().values
plt.pie(y1, labels=x1, autopct='%.2f%%', startangle=180)
plt.title("Porcentagem de Temporadas")
plt.show()

# #Grafico de Barra(Escolhi barra horizontal pelo tamanho do texto)
plt.barh(x1,y1, color='#661906', height=0.8,linewidth=4)
plt.title("Quantidade de Temporadas")
plt.xlabel("Temporadas")
plt.ylabel("Quantidade")
plt.grid(True)
plt.show()
#Grafico de Densidade
sns.kdeplot(df['Nota'], fill=True, color="#95991f")
plt.title("Densidade de Notas")
plt.xlabel("Notas")
plt.ylabel("Quantidade")
plt.grid(True)
plt.show()

#Grafico de Regressão
sns.regplot(x='N_Avaliações', y='N_Avaliações_MinMax', data= df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title("Regressão entre N° de Avaliações pela padronização")
plt.xlabel("n° de avaliações")
plt.ylabel("Padronização")
plt.grid(True)
plt.show()