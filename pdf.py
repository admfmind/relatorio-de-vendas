#pip install fpdf
from fpdf import FPDF
import json

with open("estoque.json", "r") as estoque:
    itens = json.load(estoque)

with open("dados-vendas.json", "r") as vendedores:
    vendedores = json.load(vendedores)

"""
A4 -> 210x297cm
"""

#arquivo pdf. orientação vertical. filha A4
pdf = FPDF(orientation="P", unit="mm", format="A4")

#criar nova pagina
pdf.add_page()

#fonte do texto
pdf.set_font("Arial", "", 16)

#adicionar texto
pdf.cell(w=200, h=30, txt="DOCUMENTO DA EMPRESA WORK", ln=True, align="C")
#logo
pdf.image("logo-work.png", x=10, y=10, w=25, h=25)

pdf.cell(w=0, h=15, txt='ESTOQUE DE PRODUTOS', border=1, ln=1, align='C', fill=0)
#tabela de produtos
pdf.cell(w=125, h=15, txt='PRODUTO', border=1, align='C', fill=0)
pdf.cell(w=0, h=15, txt="QUANTIDADE", border=1, ln=1, align='C', fill=0)

for iten in itens:
    #tabela de produtos
    pdf.cell(w=125, h=16, txt=iten["nome-item"], border=1, align='C', fill=0)
    pdf.cell(w=0, h=16, txt=f"{iten[iten['nome-item']]}", border=1,ln=1, align='C', fill=0)

#tabela de vendedores
for CLT in vendedores:
    pdf.add_page()
    #adicionar texto
    pdf.cell(w=200, h=30, txt="DOCUMENTO DA EMPRESA WORK", ln=True, align="C")
    #logo
    pdf.image("logo-work.png", x=10, y=10, w=25, h=25)
    pdf.cell(w=0, h=15, txt=f"VENDAS DE {CLT['vendedor']}", border=1, ln=1, align="C", fill=0)

    pdf.cell(w=100, h=15, txt="NOME DO PRODUTO", border=1, align="C", fill=0)
    pdf.cell(w=0, h=15, txt="VENDIDOS", border=1, ln=1, align="C", fill=0)
    for CLT_item in itens:
        pdf.cell(w=100, h=15, txt=f"{CLT_item['nome-item']}", border=1, align="C", fill=0)
        nome = "nome-item"
        trabalhador =f"{ CLT['vendido-'+CLT_item[nome]]}"
        pdf.cell(w=0, h=15, txt=trabalhador, border=1, ln=1, align="C", fill=0)

#criar pdf
pdf.output("arquivo.pdf")
