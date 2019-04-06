# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:34:49 2019

@author: ruialberto
"""

from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import pandas as pd
import datetime
import numpy as np
#import random
import warnings
warnings.filterwarnings("ignore")


yf.pdr_override()


inicio = datetime.datetime(2019,3,6)
fim = datetime.datetime(2019,4,6)

#nome_ficheiro = 'lista_sp500.txt'
nome_ficheiro = 'euro_new.txt'
#nome_ficheiro = 'euro.txt'
#Abrir ficheiro para leitura
try:
        fhand = open(nome_ficheiro)

except:
        print ('Nao e possivel abrir o ficheiro: ', fhand)


lista = []

#Cria lista com os ticket do SP500
for f in fhand:
    linha = f.strip().split(',')
    ticker = linha[0]
    lista.append(ticker)

    
def obter_precos(ticket):
    try:
        df = pdr.get_data_yahoo(ticket,inicio, fim)
        print(df)
        df.to_csv('machine_learning/dados_actuais_'+ticket+'_050419.csv')
    except:
        print('Nao foi possivel obter dados do ticket: ',ticket)
        return

"""   
def executa_calculos():
    for valor in lista:
        try:
            lista_rsi = obter_precos(valor)
            if lista_rsi[-1] > 20 and lista_rsi[-1] < 35:
            #if lista_rsi[-1] > 71:    
                with open('tmp_rsi_short_euro_020419.txt','a') as file:
                    file.write('{0} : RSI {1}\n'.format(valor,lista_rsi[-1]))
            else:
                print(valor)
        except:
            continue

"""

for quote in lista:
    obter_precos(quote)