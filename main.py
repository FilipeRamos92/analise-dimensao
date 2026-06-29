import os
import pandas as pd
import openpyxl
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def selecionar_origem():
    """Abre o explorador para escolher o arquivo Excel original"""
    caminho_escolhido = filedialog.askopenfilename(
        title="Selecione o arquivo Excel de Origem",
        filetypes=[("Arquivos do Excel", "*.xlsx")]
    )
    if caminho_escolhido:
        entrada_origem.delete(0, ctk.END)
        entrada_origem.insert(0, caminho_escolhido)
        label_status.configure(text="Arquivo de origem selecionado!", text_color="green")

def selecionar_destino():
    """Abre o explorador para escolher a pasta onde o novo arquivo será salvo"""
    pasta_escolhida = filedialog.askdirectory(
        title="Selecione a Pasta de Destino"
    )
    if pasta_escolhida:
        entrada_destino.delete(0, ctk.END)
        entrada_destino.insert(0, pasta_escolhida)
        label_status.configure(text="Pasta de destino selecionada!", text_color="green")

def executar_automacao():
       
    arquivo_orignal = entrada_origem.get().strip()
    pasta_final = entrada_destino.get().strip()

    if not arquivo_orignal or not pasta_final:
        label_status.configure(text="Erro: Preencha a origem e o destino!", text_color="red")
        return

    label_status.configure(text="Processando... Por favor, aguarde.", text_color="yellow")

    # Força a interface a atualizar o texto antes de travar no processo pesado
    app.update_idletasks()
    
    arquivo_novo = Path(pasta_final) / "Alocação por Porto.xlsx"
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

app = ctk.CTk()
app.title("Automação Análise Porto/Embarcação")
app.geometry("600x400")

# Título Principal
label_titulo = ctk.CTkLabel(app, text="Análise de Porto/Embarcação", font=("Arial", 20, "bold"))
label_titulo.pack(pady=20)

# --- BLOCO 1: ARQUIVO DE ORIGEM ---
label_origem = ctk.CTkLabel(app, text="Arquivo Original:", font=("Arial", 12, "bold"))
label_origem.pack(anchor="w", padx=50, pady=(5, 0))

frame_origem = ctk.CTkFrame(app, fg_color="transparent")
frame_origem.pack(pady=5, fill="x", padx=40)

entrada_origem = ctk.CTkEntry(frame_origem, width=440, placeholder_text="Selecione o arquivo Excel original")
entrada_origem.pack(side="left", padx=(10, 5))

botao_origem = ctk.CTkButton(frame_origem, text="...", width=40, command=selecionar_origem)
botao_origem.pack(side="left")


# --- BLOCO 2: PASTA DE DESTINO ---
label_destino = ctk.CTkLabel(app, text="Salvar em:", font=("Arial", 12, "bold"))
label_destino.pack(anchor="w", padx=50, pady=(15, 0))

frame_destino = ctk.CTkFrame(app, fg_color="transparent")
frame_destino.pack(pady=5, fill="x", padx=40)

entrada_destino = ctk.CTkEntry(frame_destino, width=440, placeholder_text="Selecione onde o novo arquivo será salvo")
entrada_destino.pack(side="left", padx=(10, 5))

botao_destino = ctk.CTkButton(frame_destino, text="...", width=40, command=selecionar_destino)
botao_destino.pack(side="left")


# --- BOTÃO DE EXECUÇÃO ---
botao_rodar = ctk.CTkButton(app, text="Processar e Gerar Arquivo", command=executar_automacao, font=("Arial", 14, "bold"), height=40)
botao_rodar.pack(pady=30)

# Barra de Status
label_status = ctk.CTkLabel(app, text="Status: Aguardando configurações.", font=("Arial", 12, "italic"))
label_status.pack(pady=5)

app.mainloop()
