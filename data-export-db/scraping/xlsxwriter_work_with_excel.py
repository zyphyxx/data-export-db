import xlsxwriter
import os

# Defina o caminho completo para o arquivo incluindo o nome e a extensão .xlsx
path = "D:\\PY-Projects\\data-export-db\\data-export-db\\scraping\\config\\person.xlsx"

# Cria um objeto workbook
workbook = xlsxwriter.Workbook(path)

# Adiciona uma planilha chamada 'nova'
worksheet = workbook.add_worksheet('planilha de teste')

# Escreve no célula A1
worksheet.write("A1", "Nome")
worksheet.write("A2", "Edgar")
worksheet.write("B1", "Idade")
worksheet.write("B2", "31")

# Fecha o workbook para salvar o arquivo
workbook.close()

# Abre o arquivo gerado
os.startfile(path)
