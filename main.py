import openpyxl
import pandas as pd
from pathlib import Path

try:
    from verifica_desktop import verifica_desktop
    pasta_desktop = verifica_desktop()

except Exception as e:
    print(f"Erro ao verificar a área de trabalho: {e}")
    pasta_desktop = Path("/mnt/c/Users/Public/Desktop")  
    
arquivo_orignal = 'base-analise.xlsx';

arquivo_novo = pasta_desktop / 'arquivo_final.xlsx';

aloc = {}

config_tipos = {
    "Cód. Porto": str,
}

abas_criadas = []

df_alocacao = pd.read_excel(arquivo_orignal, sheet_name='Alocação', header=0, index_col=0, dtype=config_tipos)

df_base = pd.read_excel(arquivo_orignal, sheet_name='Base', header=0, index_col=0, dtype=config_tipos)

codigos_porto = df_alocacao['Cód. Porto'].dropna().unique()

wb = openpyxl.load_workbook(arquivo_orignal, data_only=False)

for index, data_aloc in df_alocacao.iterrows():
    aloc[data_aloc['Cód. Embarcação']] = data_aloc['Cód. Porto']

for index, data_aloc in df_alocacao.iterrows():
    nome_aba = data_aloc['Cód. Porto'][:10]

    if nome_aba not in wb.sheetnames:
        wb.create_sheet(title=nome_aba)
        print(f"Aba '{nome_aba}' criada com sucesso!")
        abas_criadas.append(nome_aba)

for index, data_base in df_base.iterrows():
    if data_base['Cód. Porto'] != aloc[data_base['Cód. Embarcação']]:
        if data_base['Cód. Porto'] in abas_criadas:
            aba = wb[aloc[data_base['Cód. Embarcação']]]
            aba.append(data_base.tolist())
            print(f"Dados da linha {index} adicionados à aba '{nome_aba}'.")

wb.save(arquivo_novo)

print(f"\nConcluído! O arquivo '{arquivo_novo}' foi gerado apenas com as abas criadas.")

