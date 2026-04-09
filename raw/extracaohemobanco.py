import pandas as pd
import os

arquivo = r'raw\municipio.csv'
arquivo_novo = r'clean\clean_data.xlsx'

try:
    df = pd.read_csv(arquivo, sep=';', encoding='utf-8')
    col_municipio = df.columns[0]
    col_total = df.columns[2]

    df[col_municipio] = df[col_municipio].str.replace(r'^\d+\s+', '', regex=True).str.replace('"', '').str.strip()
    df[col_municipio] = df[col_municipio].str.title()
    df.rename(columns={'2026':'Quantidade de Bolsas de Sangue'}, inplace=True)

    df[col_total] = pd.to_numeric(df[col_total], errors='coerce')
    df = df[df[col_total] > 0] 
    
    df[col_total] = df[col_total].astype(int)

    os.makedirs(r'test_\clean', exist_ok=True)
    df.to_excel(arquivo_novo, index=False)
    
except Exception as e:
    print(f" Ocorreu um erro: {e}")