import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("Unificador de PDF em Python")

print(lista_arquivos)