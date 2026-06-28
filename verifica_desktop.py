import subprocess
from pathlib import Path

def verifica_desktop():
    # Executa o comando PowerShell para obter o caminho da área de trabalho
    comando_ps = "[Environment]::GetFolderPath('Desktop')"
    resultado = subprocess.run(
        ["powershell.exe", "-Command", comando_ps], 
        capture_output=True, 
        text=True, 
        check=True
    )

    # O resultado vem como "C:\Users\NomeDoUsuario\Desktop\n", vamos limpar
    caminho_windows = resultado.stdout.strip()

    # Convertemos o caminho do Windows (C:\...) para o formato que o WSL entende (/mnt/c/...)
    caminho_wsl = caminho_windows.replace("C:", "/mnt/c").replace("\\", "/")
    pasta_desktop = Path(caminho_wsl)
    return pasta_desktop

