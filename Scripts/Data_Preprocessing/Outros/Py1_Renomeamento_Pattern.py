import os
import shutil


def renomear_fotos(diretorio_entrada, diretorio_saida, nome_base, padrao):
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    arquivos = os.listdir(diretorio_entrada)
    fotos = [
        arq
        for arq in arquivos
        if arq.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp"))
    ]
    for i, foto in enumerate(fotos, start=1):
        extensao = os.path.splitext(foto)[1]
        novo_nome = f"{nome_base}_{padrao}{i}{extensao}"
        caminho_foto_original = os.path.join(diretorio_entrada, foto)
        caminho_novo_foto = os.path.join(diretorio_saida, novo_nome)
        shutil.copy(caminho_foto_original, caminho_novo_foto)


# Caminhos e configurações para Outros
diretorio_entrada_outros = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Outros\S2_Conversao"
diretorio_saida_outros = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Outros\S3_Renomeamento_Sintetico"

# Chamada da função para renomear as fotos para Outros
renomear_fotos(diretorio_entrada_outros, diretorio_saida_outros, "Outros", "S")

print("Renomeação completa para Outros!")
