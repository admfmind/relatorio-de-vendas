import json


# VENDA DOS TRABALHADORES
with open("dados-vendas.json") as vendas:
    dados_vendas = json.load(vendas)


# ESTOQUE DA LOJA
with open("estoque.json") as estoque:
    estoque = json.load(estoque)

# estoque
print("ESTOQUE ———————————")
for item in estoque:
    print(f"{item['nome-item']}   : {item['total-'+item['nome-item']]}/{item[item['nome-item']]}\n{'_'*19}")
print()


# vendas
local_item = 0
for venda in dados_vendas:
    #porcentagem de vendas do total de itens
    print(f"""+{'—'*30}
|NOME: {venda['vendedor']}
|{'—'*30}
|            VENDEU""")

    for item in estoque:
        print(f"""|
| {item['nome-item']}: {venda['vendido-'+item['nome-item']]}
| {(venda['vendido-'+item['nome-item']] / 100) * item['total-'+item['nome-item']]:.1f}% do estoque
{'-'*30}""")
    print("+",'—'*30,"\n")
