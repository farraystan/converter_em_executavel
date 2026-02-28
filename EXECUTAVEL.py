import subprocess,os
from tkinter import Tk, filedialog

# ====== CONFIG =========
local_execução = r"CAMINHO_SUA_PASTA_AQUI"
# =======================

# selecione o arquivo que deseja tornar em executável
def selecionar_arquivo_py():
    root = Tk()
    root.withdraw()
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo Python",
        filetypes=[
            ("Arquivos Python", "*.py"),
            ("Todos os arquivos", "*.*")
        ]
    )
    return arquivo

base = local_execução
venv = os.path.join(base, "scripts", "activate")
arquivo = selecionar_arquivo_py()

cmd = f'cmd /c "{venv} && pyinstaller --onefile {arquivo}"'
subprocess.run(cmd, shell=True, cwd=base)
