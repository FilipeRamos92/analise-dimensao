import openpyxl
import pandas as pd
from pathlib import Path
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

try:
    from verifica_desktop import verifica_desktop
    pasta_desktop = verifica_desktop()

except Exception as e:
    print(f"Erro ao verificar a área de trabalho: {e}")
    pasta_desktop = Path("/mnt/c/Users/Public/Desktop")  

def executar_automacao():
       
    arquivo_orignal = entrada_arquivo.get().strip()

    if not arquivo_orignal:
        label_status.configure(text="Por favor, insira o nome ou caminho do arquivo original.", text_color="red")
        return

    label_status.configure(text="Processando...", text_color="blue")

    # Força a interface a atualizar o texto antes de travar no processo pesado
    janela.update_idletasks()
    
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

# --- CONSTRUÇÃO DA JANELA VISUAL ---

# Inicializa a janela principal
janela = ctk.CTk()
janela.title("Automação de Alocação por Porto")
janela.geometry("500x350")

# Título do App
label_titulo = ctk.CTkLabel(janela, text="Separador de Abas por Porto", font=("Arial", 20, "bold"))
label_titulo.pack(pady=20)

# Campo: Arquivo Original
label_instrucao = ctk.CTkLabel(janela, text="Nome ou caminho do arquivo original (Excel):", font=("Arial", 12))
label_instrucao.pack(pady=10)

entrada_arquivo = ctk.CTkEntry(janela, width=400, placeholder_text="Digite o nome ou caminho do arquivo aqui...")
entrada_arquivo.pack(pady=10)

# Botão Executar 
botao_rodar = ctk.CTkButton(janela, text="Gerar Arquivo", command=executar_automacao, font=("Arial", 14, "bold"))
botao_rodar.pack(pady=20)

# Linha de Status (Dá o feedback do processo)
label_status = ctk.CTkLabel(janela, text="Aguardando execução...", font=("Arial", 12))
label_status.pack(pady=10)

janela.mainloop()
