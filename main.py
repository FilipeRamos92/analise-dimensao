import openpyxl
import pandas as pd

arquivo_orignal = 'base-analise.xlsx';

arquivo_novo = 'arquivo_final.xlsx';

config_tipos = {
    "Cód. Porto": str,
}

df_alocacao = pd.read_excel(arquivo_orignal, sheet_name='Alocação', header=0, index_col=0, dtype=config_tipos)

codigos_porto = df_alocacao['Cód. Porto'].dropna().unique()

wb = openpyxl.load_workbook(arquivo_orignal, data_only=False)

for porto in codigos_porto:
    nome_aba = porto[:10]

    if nome_aba not in wb.sheetnames:
        wb.create_sheet(title=nome_aba)
        print(f"Aba '{nome_aba}' criada com sucesso!")

wb.save(arquivo_novo)

print(f"\nConcluído! O arquivo '{arquivo_novo}' foi gerado apenas com as abas criadas.")

