import os
import re
from PIL import Image
import pytesseract

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
PASTA_COMPROVANTES = "comprovantes"

valor_busca = input("Digite o valor: ").strip()

# Remove caracteres
valor_busca = re.sub(r"\D", "", valor_busca)

encontrados = []

for arquivo in os.listdir(PASTA_COMPROVANTES):

    if arquivo.lower().endswith((".png", ".jpg", ".jpeg")):

        caminho = os.path.join(PASTA_COMPROVANTES, arquivo)

        try:

            imagem = Image.open(caminho)

            largura, altura = imagem.size

            # Região onde fica o valor
            area_valor = imagem.crop((
                0,
                altura * 0.10,
                largura * 0.60,
                altura * 0.25
            ))

            # Preto e branco
            area_valor = area_valor.convert("L")

            # OCR
            texto = pytesseract.image_to_string(
                area_valor,
                lang="eng",
                config="--psm 6"
            )

            # Apenas números
            texto_numeros = re.sub(r"\D", "", texto)

            # Busca
            if valor_busca in texto_numeros:

                encontrados.append(caminho)

        except Exception as erro:
            print(f"Erro em {arquivo}: {erro}")

print("\n========================\n")

if encontrados:

    print("Comprovantes encontrados:\n")

    for item in encontrados:

        print(f"✔ {os.path.basename(item)}")

        # Abre automaticamente
        os.startfile(item)

else:
    print("Nenhum comprovante encontrado.")