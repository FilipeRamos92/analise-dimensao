import customtkinter as ctk
from tkinter import filedialog

class Tela:
    def __init__(self, master, selecionar_origem, selecionar_destino, executar_automacao):
        self.master = master
        self.master.title("Automação de Análise de Dimensão")
        self.master.geometry("600x300")
        self.master.resizable(False, False)
        self.selecionar_origem = selecionar_origem
        self.selecionar_destino = selecionar_destino
        self.executar_automacao = executar_automacao

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Criação dos widgets
        # Origem
        self.label_origem = ctk.CTkLabel(master, text="Arquivo Base:")
        self.label_origem.pack(anchor="w", padx=50, pady=(5, 0))

        self.frame_origem = ctk.CTkFrame(master, fg_color="transparent")
        self.frame_origem.pack(pady=5, fill="x", padx=40)

        self.entrada_origem = ctk.CTkEntry(self.frame_origem, width=440, placeholder_text="Selecione o arquivo (Excel)")
        self.entrada_origem.pack(side="left", padx=(10, 5))

        self.botao_origem = ctk.CTkButton(self.frame_origem, text="...", width=40,command=self.selecionar_origem)
        self.botao_origem.pack(side="left", padx=(10, 5))

        # Destino
        self.label_destino = ctk.CTkLabel(master, text="Pasta de Destino:")
        self.label_destino.pack(anchor="w", padx=50, pady=(15, 0))

        self.frame_destino = ctk.CTkFrame(master, fg_color="transparent")
        self.frame_destino.pack(pady=5, fill="x", padx=40)

        self.entrada_destino = ctk.CTkEntry(self.frame_destino, width=440, placeholder_text="Selecione a pasta de destino")
        self.entrada_destino.pack(side="left", padx=(10, 5))

        self.botao_destino = ctk.CTkButton(self.frame_destino, text="...", width=40, command=self.selecionar_destino)
        self.botao_destino.pack(side="left", padx=(10, 5))

        self.botao_executar = ctk.CTkButton(master, text="Executar", command=self.executar_automacao)
        self.botao_executar.pack(pady=20)

        self.label_status = ctk.CTkLabel(master, text="", text_color="green")
        self.label_status.pack(pady=10)