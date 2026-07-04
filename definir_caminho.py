import sys
from tkinter import filedialog
import customtkinter as ctk

def selecionar_origem(entrada, label_status):
    """Abre o explorador para escolher o arquivo Excel original"""
    caminho_escolhido = filedialog.askopenfilename(
        title="Selecione o arquivo Excel de Origem",
        filetypes=[("Arquivos do Excel", "*.xlsx")]
    )
    if caminho_escolhido:
        entrada.delete(0, ctk.END)
        entrada.insert(0, caminho_escolhido)
        label_status.configure(text="Arquivo de origem selecionado!", text_color="green")

def selecionar_destino(entrada, label_status):
    """Abre o explorador para escolher a pasta onde o novo arquivo será salvo"""
    pasta_escolhida = filedialog.askdirectory(
        title="Selecione a Pasta de Destino"
    )
    if pasta_escolhida:
        entrada.delete(0, ctk.END)
        entrada.insert(0, pasta_escolhida)
        label_status.configure(text="Pasta de destino selecionada!", text_color="green")
