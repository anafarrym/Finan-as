"""
APS Finanças 3 - parte final

VALE3

Ana Flavia de Mello Arrym
Ana Julia Carvalho Marzola
Clarice Barroso
José Carlos Passos
Maria Eduarada Alencar
Sofia Kerimeh
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as mt
import pandas as pd

base_calls = pd.read_excel('Base_APS.xlsx', 'CALLS')
base_puts = pd.read_excel('Base_APS.xlsx', 'PUTS')
close = pd.read_excel('Base_APS.xlsx', 'CLOSE')
strikes_iguais = np.zeros(11)     
precos_puts = np.zeros(5)
precos_calls = np.zeros(5)

#testando para ver se os valores das opções são iguais
for i in range (0, len(base_calls['Strike']), 1):
    for k in range (0, len(base_puts['Strike']), 1):
        if (base_calls['Strike'][i]) == (base_puts['Strike'][k]):
            strikes_iguais[i] = base_calls['Strike'][i]
            precos_calls[i] = base_calls['Preço'][i]
            precos_puts[i] = base_puts['Preço'][i]
        else:
            continue
        
#removendo os espaços em que a igualdade não é válida        
indices = np.where(strikes_iguais ==0.0)
strikes_iguais = np.delete(strikes_iguais, indices)

#trazendo a valor presente aos strikes
ano = 2/12
taxa = 0.1368
vp = np.zeros(5)
quant = len(strikes_iguais)

for i in range (0, quant, 1):
    vp[i] = (strikes_iguais[i])/(mt.exp(taxa*ano))
print(vp)

#paridade put call
lado_calls = np.zeros(5)
lado_puts = np.zeros(5)
for i in range(0, len(vp), 1):
    lado_calls[i] = precos_calls[i] + vp[i]
    lado_puts[i] = precos_puts[i] + strikes_iguais[i] 
print(lado_calls)
print(lado_puts)   

paridade_valida = np.zeros(2)
compraput_vendecall = np.zeros(2)
compracall_vendeput = np.zeros(3)
for i in range(0, len(vp), 1):
        if lado_calls[i] == lado_puts[i]:
            print("paridade válida")
        elif lado_calls[i] > lado_puts[i]:
            print("comprar puts e vender calls")
        else:
            print ("comprar calls e vender puts")

#volatilidade implícita
preco_dia = 75.51
vol_implicita_calls = np.zeros(5)
vol_implicita_puts = np.zeros(5)
for i in range(0, quant, 1):
    vol_implicita_calls[i] = np.sqrt((2*np.pi)/ano*
                                     (precos_calls[i]/preco_dia))
    vol_implicita_puts[i] = np.sqrt((2*np.pi)/ano*
                                    (precos_puts[i]/preco_dia))
print(vol_implicita_calls)
print(vol_implicita_puts)    

#curva smile
plt.subplots()
plt.plot(precos_calls, vol_implicita_calls)
plt.title('smile calls')
plt.xlabel('preços')
plt.ylabel('vol implícita')
plt.show()

plt.subplots()
plt.plot(precos_puts, vol_implicita_puts)
plt.title('smile puts')
plt.xlabel('preços')
plt.ylabel('vol implícita')
plt.show()


    
    