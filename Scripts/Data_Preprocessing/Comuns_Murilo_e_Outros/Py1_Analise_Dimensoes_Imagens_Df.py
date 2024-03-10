import os
from PIL import Image
import pandas as pd


def processar_imagens(caminho_pasta):
    dimensoes = []
    for nome_arquivo in os.listdir(caminho_pasta):
        if nome_arquivo.lower().endswith(
            (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")
        ):
            try:
                with Image.open(os.path.join(caminho_pasta, nome_arquivo)) as img:
                    dimensoes.append(img.size)  # (largura, altura)
            except Exception as e:
                print(f"Erro ao abrir {nome_arquivo}: {e}")
    df = pd.DataFrame(dimensoes, columns=["Largura", "Altura"])
    return df.groupby(["Largura", "Altura"]).size().reset_index(name="Contagem")


# Caminhos para os diretórios de imagem
caminho_murilo = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pre_Pipeline\Murilo_Original_Bruto"
caminho_outros = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pre_Pipeline\Outros_Sintetico_Bruto"

# Processando as imagens e criando DataFrames
df_murilo = processar_imagens(caminho_murilo)
df_outros = processar_imagens(caminho_outros)

# Imprimindo os resultados
print("Contagem de dimensões para Murilo:")
print(df_murilo)
print("\nContagem de dimensões para Outros:")
print(df_outros)
