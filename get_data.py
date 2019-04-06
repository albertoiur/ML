# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:25:56 2018

@author: ruialberto
"""

from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
#import pandas as pd
import datetime
#import numpy as np
#import random
import warnings
warnings.filterwarnings("ignore")


yf.pdr_override()



ticket='SAM'
#inicio = datetime.datetime(1980,1,1)
inicio = datetime.datetime(2019,1,20)
fim = datetime.datetime(2019,2,22)


#df = pdr.get_data_yahoo('C', inicio, fim)
df = pdr.get_data_yahoo(ticket,inicio, fim)
df.to_csv('SAM_21190220.csv')
