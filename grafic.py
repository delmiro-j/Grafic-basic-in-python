# importando matplolib e definindo como "plt"
import matplotlib.pyplot as plt

# variaveis com valores
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho',]
valores = [105235,107697,110256,109236,108859,115000]

#fornecendoum titulos e labels para a coluna e linha da tabela
plt.title('Faturamento no primeiro semestre de 2020')
plt.xlabel('Meses')
plt.ylabel('Faturamento R$')

#construindo o gráfico
plt.plot(meses,valores)
#Limitando o valor máximo e minimo mostrado no gráfico
plt.ylim(100000,120000)
#Mostrando o gráfico
plt.show()