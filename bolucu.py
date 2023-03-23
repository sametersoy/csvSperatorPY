import pandas as pd
import csv


df = pd.read_csv(r'./ibozbas_isemri_sayac_okuma.csv', 
                 encoding= 'CP1254',
                 on_bad_lines='skip', 
                 skipinitialspace = True, 
                 chunksize=1000000)

for i,f in enumerate(df):
    f.to_csv(rf'./bolunen_{i}.csv')