import PyPDF2
import os

merger = PyPDF2.PdfMerger()

#informe a pasta onde deseja localizar os PDF's
lista_arquivos = os.listdir("arquivos")

print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

#
merger.write("PDF's unificados.pdf")        